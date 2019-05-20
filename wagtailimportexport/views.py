import io
import json
import re

from django.http import JsonResponse, FileResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import ungettext, ugettext_lazy as _
from django.http import HttpResponse

import requests

from wagtailimportexport.compat import messages, Page
from wagtailimportexport.exporting import (
    export_pages,
    export_snippets,
    export_image_data,
    zip_content,
)
from wagtailimportexport.forms import ExportForm, ImportFromAPIForm, ImportFromFileForm
from wagtailimportexport.importing import import_pages


def index(request):
    return render(request, 'wagtailimportexport/index.html')


def import_from_api(request):
    """
    Import a part of a source site's page tree via a direct API request from
    this Wagtail Admin to the source site

    The source site's base url and the source page id of the point in the
    tree to import defined what to import and the destination parent page
    defines where to import it to.
    """
    if request.method == 'POST':
        form = ImportFromAPIForm(request.POST)
        if form.is_valid():
            # remove trailing slash from base url
            base_url = re.sub(r'\/$', '',
                              form.cleaned_data['source_site_base_url'])
            import_url = (base_url + reverse(
                'wagtailimportexport:export',
                args=[form.cleaned_data['source_page_id']]))
            r = requests.get(import_url)
            import_data = r.json()
            parent_page = form.cleaned_data['parent_page']

            try:
                page_count = import_pages(import_data, parent_page)
            except LookupError as e:
                messages.error(request,
                               _("Import failed: %(reason)s") % {'reason': e})
            else:
                messages.success(
                    request,
                    ungettext("%(count)s page imported.",
                              "%(count)s pages imported.", page_count) %
                    {'count': page_count})
            return redirect('wagtailadmin_explore', parent_page.pk)
    else:
        form = ImportFromAPIForm()

    return render(request, 'wagtailimportexport/import_from_api.html', {
        'form': form,
    })


def import_from_file(request):
    """
    Import a part of a source site's page tree via an import of a JSON file
    exported to a user's filesystem from the source site's Wagtail Admin

    The source site's base url and the source page id of the point in the
    tree to import defined what to import and the destination parent page
    defines where to import it to.
    """
    if request.method == 'POST':
        form = ImportFromFileForm(request.POST, request.FILES)
        if form.is_valid():
            import_data = json.loads(
                form.cleaned_data['file'].read().decode('utf-8-sig'))
            parent_page = form.cleaned_data['parent_page']

            try:
                page_count = import_pages(import_data, parent_page)
            except LookupError as e:
                messages.error(request,
                               _("Import failed: %(reason)s") % {'reason': e})
            else:
                messages.success(
                    request,
                    ungettext("%(count)s page imported.",
                              "%(count)s pages imported.", page_count) %
                    {'count': page_count})
            return redirect('wagtailadmin_explore', parent_page.pk)
    else:
        form = ImportFromFileForm()

    return render(request, 'wagtailimportexport/import_from_file.html', {
        'form': form,
    })


def export_to_file(request):
    """
    Export a part of this source site's page tree, along with all snippets 
    and images, to a ZIP file on this user's filesystem for subsequent 
    import in a destination site's Wagtail Admin
    """
    if request.method == 'POST':
        form = ExportForm(request.POST)
        if form.is_valid():
            content_data = {
                'pages': export_pages(
                    root_page=form.cleaned_data['root_page'],
                    export_unpublished=form.cleaned_data['export_unpublished'],
                    null_users=form.cleaned_data['null_users'],
                    null_images=True,
                ),
                #'snippets': export_snippets(),
                #'images': export_image_data(null_users=form.cleaned_data['null_users']),
            }
            filedata = zip_content(content_data)
            payload = io.BytesIO(filedata)

            # Grab ZIP file from in-memory, make response with correct MIME-type
            response = HttpResponse(payload.getvalue(), content_type = "application/x-zip-compressed")
            # ..and correct content-disposition
            response['Content-Disposition'] = 'attachment; filename=content.zip'

            return response
    else:
        form = ExportForm()

    return render(request, 'wagtailimportexport/export_to_file.html', {
        'form': form,
    })


def export(request, page_id, export_unpublished=False):
    """
    API endpoint of this source site to export a part of the page tree
    rooted at page_id

    Requests are made by a destination site's import_from_api view.
    """
    try:
        if export_unpublished:
            root_page = Page.objects.get(id=page_id)
        else:
            root_page = Page.objects.get(id=page_id, live=True)
    except Page.DoesNotExist:
        return JsonResponse({'error': _('page not found')})

    payload = {
        'pages':
        export_pages(
            root_page=root_page, export_unpublished=export_unpublished)
    }

    return JsonResponse(payload)
