# Generated by Django 3.0.4 on 2020-09-30 17:37

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0115_auto_20200930_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='customization_form_content',
        ),
        migrations.AddField(
            model_name='book',
            name='customization_form_disclaimer',
            field=wagtail.fields.RichTextField(blank=True, help_text='This will update ALL books to use this value!', default="<p><b>Disclaimer</b></p><p>The following features and functionality are not available to teachers and students using Google Docs customized content:</p><ul><li><b>Errata updates</b>. OpenStax webview is updated at least twice yearly. Customized Google Docs will not receive these content updates.</li><li><b>Access to study tools</b>. OpenStax webview has in-book search, highlighting, study guides, and more available for free. This functionality will not be available in Google Docs versions.</li><li><b>Formatting. </b>Print books and webview have a specific design and structure format developed for those platforms. These functionalities are not available in the Google Docs versions.</li></ul>"),
        ),
        migrations.AddField(
            model_name='book',
            name='customization_form_heading',
            field=models.CharField(blank=True, help_text='Heading for the CE customization form. This will update ALL books to use this value!', max_length=255, null=True, default="Customization Form"),
        ),
        migrations.AddField(
            model_name='book',
            name='customization_form_next_steps',
            field=wagtail.fields.RichTextField(blank=True, help_text='This will update ALL books to use this value!', default="<p><b>Next Steps</b></p><ol><li>Within two business days, you will receive an email for each module that you have requested access to customize.</li><li>The link provided in the email will be your own copy of the Google Doc that OpenStax generated for you.</li><li>Once you have accessessed the document you can make the changes you desire and share with your students. We recommend using the &quot;Publish to the Web&quot; functionality under the file menu for sharing with students.</li></ol>"),
        ),
        migrations.AddField(
            model_name='book',
            name='customization_form_subheading',
            field=models.CharField(blank=True, help_text='Subheading for the CE customization form. This will update ALL books to use this value!', max_length=255, null=True, default="Please select the modules (up to 10), that you want to customize with Google Docs."),
        ),
    ]
