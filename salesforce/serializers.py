from collections import OrderedDict
from .models import School, AdoptionOpportunityRecord, Partner, SalesforceForms, ResourceDownload
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ('id',
                  'name',
                  'phone',
                  'website',
                  'type',
                  'adoption_date',
                  'key_institutional_partner',
                  'achieving_the_dream_school',
                  'hbcu',
                  'texas_higher_ed',
                  'undergraduate_enrollment',
                  'pell_grant_recipients',
                  'percent_students_pell_grant',
                  'current_year_students',
                  'all_time_students',
                  'current_year_savings',
                  'all_time_savings',
                  'physical_country',
                  'physical_street',
                  'physical_city',
                  'physical_state_province',
                  'physical_zip_postal_code',
                  'long',
                  'lat',
                  'testimonial',)


class AdoptionOpportunityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionOpportunityRecord
        fields = ('opportunity_id',
                  'account_id',
                  'book_name',
                  'email',
                  'school',
                  'yearly_students',
                  'updated')
        read_only_fields = ('opportunity_id',
                  'account_id',
                  'book_name',
                  'email',
                  'school',
                  'yearly_students')

class PartnerSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(PartnerSerializer, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].read_only = True

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        # if lead sharing is unchecked in salesforce, we hide the formstack_url (which hides request info button on FE)
        if not ret['lead_sharing']:
            ret['formstack_url'] = False

        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(filter(lambda x: x[1] is not False, ret.items()))
        return ret


    class Meta:
        model = Partner
        fields = '__all__'


class SalesforceFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesforceForms
        fields = ('oid', 'debug', 'posting_url')
        read_only_fields = ('oid', 'debug', 'posting_url')


class ResourceDownloadSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        book = validated_data.get('book', None)
        book_format = validated_data.get('book_format', None)
        account_id = validated_data.get('account_id', None)
        resource_name = validated_data.get('resource_name', None)
        try:
            rd = ResourceDownload.objects.get(book=book, account_id=account_id, resource_name=resource_name)
            rd.save()
        except:
            rd = ResourceDownload.objects.create(**validated_data)

        return rd

    class Meta:
        model = ResourceDownload
        fields = ('id', 'book', 'book_format', 'account_id', 'last_access', 'number_of_times_accessed', 'resource_name', 'created')
        read_only_fields = ('id', 'created', 'number_of_times_accessed')
