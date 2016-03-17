from django.db import models
from modelcluster.fields import ParentalKey
from pages.models import AdoptersPages
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
# Create your models here.

class Adopters(models.Model):
    salesforce_id = models.CharField(max_length=255, editable=False)
    name = models.CharField(max_length=255)
    description = RichTextField(null=True)
    website = models.URLField(max_length=255, null=True)

    page = ParentalKey(AdoptersPages,
                       on_delete=models.CASCADE,
                       related_name='organizations')

    api_fields = ('name', 'description', 'website')

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('website'),
    ]

    def __str__(self):
        return self.name

