import unicodecsv
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionModelAdmin, ExportActionMixin
from import_export.formats import base_formats

from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.utils.html import mark_safe

from extraadminfilters.filters import UnionFieldListFilter

from .models import Errata, BlockedUser, EmailText, InternalDocumentation
from .forms import ErrataForm


class ErrataResource(resources.ModelResource):
    user_faculty_status = Field(attribute='user_faculty_status')
    class Meta:
        model = Errata
        fields = ('id',
                  'created',
                  'modified',
                  'book__title',
                  'number_of_errors',
                  'is_assessment_errata',
                  'assessment_id',
                  'status',
                  'resolution',
                  'archived',
                  'junk',
                  'location',
                  'detail',
                  'internal_notes',
                  'resolution_notes',
                  'resolution_date',
                  'error_type',
                  'resource',
                  'submitted_by_account_id',
                  'user_faculty_status')
        export_order = ('id',
                        'created',
                        'modified',
                        'book__title',
                        'number_of_errors',
                        'is_assessment_errata',
                        'assessment_id',
                        'status',
                        'resolution',
                        'archived',
                        'junk',
                        'location',
                        'detail',
                        'internal_notes',
                        'resolution_notes',
                        'resolution_date',
                        'error_type',
                        'resource',
                        'submitted_by_account_id',
                        'user_faculty_status')


class InlineInternalImage(admin.TabularInline):
    model = InternalDocumentation

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class BlockedUserAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'fullname', 'reason',)

class ErrataAdmin(ExportActionModelAdmin):
    resource_class = ErrataResource
    form = ErrataForm
    list_max_show_all = 10000
    list_per_page = 200
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    actions = ['mark_in_review', 'mark_reviewed', 'mark_archived', 'mark_completed', ExportActionMixin.export_admin_action]
    inlines = [InlineInternalImage, ]
    raw_id_fields = ('submitted_by', 'duplicate_id')
    search_fields = ('id',
                     'book__title',
                     'detail',
                     'location',
                     'submitted_by__first_name',
                     'submitted_by__last_name',
                     'submitted_by__email')


    def get_export_formats(self):
        return [base_formats.CSV]

    """Actions for the Django Admin list view"""
    def mark_in_review(self, request, queryset):
        queryset.update(status='Editorial Review')
    mark_in_review.short_description = "Mark errata as in-review"

    def mark_reviewed(self, request, queryset):
        queryset.update(status='Reviewed')
    mark_reviewed.short_description = "Mark errata as reviewed"

    def mark_archived(self, request, queryset):
        queryset.update(archived=True)
    mark_archived.short_description = "Mark errata as archived"

    def mark_completed(self, request, queryset):
        queryset.update(status='Completed')
    mark_completed.short_description = "Mark errata as completed"

    def get_actions(self, request):
        actions = super(ErrataAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            if 'delete_selected' in actions:
                del actions['delete_selected']

        if not request.user.groups.filter(name__in=['Content Managers']).exists():
            if 'mark_in_review' in actions:
                del actions['mark_in_review']
            if 'mark_reviewed' in actions:
                del actions['mark_reviewed']
            if 'mark_archived' in actions:
                del actions['mark_archived']
            if 'mark_completed' in actions:
                del actions['mark_completed']
        return actions

    def change_view(self, request, object_id, extra_context=None):
        if not request.user.is_superuser or request.user.groups.filter(name__in=['Content Managers']).exists():
            extra_context = extra_context or {}
            extra_context['readonly'] = True
        return super(ErrataAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def _book_title(self, obj):
        return mark_safe(obj.book.title)

    """Model permissions"""
    @method_decorator(csrf_protect)
    def changelist_view(self, request, extra_context=None):
        self.list_display = ['id',
                             '_book_title',
                             'created',
                             'modified',
                             'short_detail',
                             'number_of_errors',
                             'status',
                             'error_type',
                             'resource',
                             'location',
                             'resolution',
                             'archived',
                             'junk']
        self.list_display_links = ['_book_title']
        self.list_filter = (('book', UnionFieldListFilter),
                            'status',
                            'created',
                            'modified',
                            'is_assessment_errata',
                            'modified',
                            'error_type',
                            'resolution',
                            'archived',
                            'junk',
                            'resource')
        self.editable = ['resolution']

        return super(ErrataAdmin, self).changelist_view(request, extra_context)

    @method_decorator(csrf_protect)
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ['openstax_book', 'reviewed_date']
        # CONTENT MANAGERS AND ADMINS
        if request.user.is_superuser or request.user.groups.filter(name__in=['Content Managers']).exists():
            self.readonly_fields = ['id',
                                    'created',
                                    'modified',
                                    'user_name',
                                    'user_email',
                                    'user_faculty_status',
                                    'accounts_link',
                                    ]

            self.save_as = True

        # EDITORIAL VENDORS
        elif request.user.groups.filter(name__in=['Editorial Vendor']).exists():
            self.readonly_fields = ['id',
                                    'created',
                                    'modified',
                                    'user_faculty_status',
                                    'archived',
                                    'junk',
                                    'detail',
                                    ]

            self.save_as = True

        # EVERYONE ELSE (read only)
        else:
            self.readonly_fields = [field.name for field in obj._meta.fields] + \
                   [field.name for field in obj._meta.many_to_many]
            self.save_as = False

        return super(ErrataAdmin, self).get_form(request, obj, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',  # jquery
            'errata/errata-admin-ui.js',  # custom errata javascript
        )

admin.site.register(Errata, ErrataAdmin)
admin.site.register(BlockedUser, BlockedUserAdmin)
admin.site.register(EmailText)
