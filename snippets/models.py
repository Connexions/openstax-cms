from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet


class Subject(models.Model):
    name = models.CharField(max_length=255)

    api_fields = ('name', )

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

register_snippet(Subject)


class FacultyResource(models.Model):
    heading = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    unlocked_resource = models.BooleanField(default=False)

    api_fields = ('heading', 'description', 'unlocked_resource')

    panels = [
        FieldPanel('heading'),
        FieldPanel('description'),
        FieldPanel('unlocked_resource'),
    ]

    def __str__(self):
        return self.heading

register_snippet(FacultyResource)


class StudentResource(models.Model):
    heading = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    unlocked_resource = models.BooleanField(default=True)

    api_fields = ('heading', 'description', 'unlocked_resource')

    panels = [
        FieldPanel('heading'),
        FieldPanel('description'),
        FieldPanel('unlocked_resource'),
    ]

    def __str__(self):
        return self.heading

register_snippet(StudentResource)


class Role(models.Model):
    display_name = models.CharField(max_length=255)
    salesforce_name = models.CharField(max_length=255)

    api_fields = ('display_name',
                  'salesforce_name')

    panels = [
        FieldPanel('display_name'),
        FieldPanel('salesforce_name'),
    ]

    def __str__(self):
        return self.display_name

register_snippet(Role)


class Version(models.Model):
    version = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    api_fields = ('version',
                  'created')

    panels = [
        FieldPanel('version'),
    ]

    def __str__(self):
        return self.version

register_snippet(Version)
