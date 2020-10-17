from rest_framework import serializers 
from .models import organization, contact, address, service, eligibility, financial_info, ijf

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = contact
        fields = ('name',
                  'title',
                  'email',
                  'phone')

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = address
        fields = ('street',
                  'city',
                  'state',
                  'zipcode')

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = service
        fields = ('name',
                  'service_type')

class EligibilitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = eligibility
        fields = ('name',
                  'value')

class FinancialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = financial_info
        fields = ('limit',
                  'turnaround')

class IJFSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ijf
        fields = ('participant_name',
                  'participant_location',
                  'requestinfo')

class OrganizationSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    address = AddressSerializer()
    services = ServiceSerializer(many=True)
    eligibilities = EligibilitySerializer(many=True)
    financial_info = FinancialSerializer()
    ijf = IJFSerializer()

    def create(self, validated_data):
        new_org = organization.objects.create(name = validated_data.pop('name'),
                                              website = validated_data.pop('website'),
                                              email = validated_data.pop('email'),
                                              fax = validated_data.pop('fax'),
                                              phone = validated_data.pop('phone'))

        contact_data = validated_data.pop('contact')
        for item in contact_data:
            #new_contact = contact(org=new_org,
            #                      name=item['name'],
            #                      title=item['title'],
            #                      email=item['email'],
            #                      phone=item['phone'])
            #new_contact.save()
            contact.objects.create(org=new_org, **item)

        address_data = validated_data.pop('address')
        for item in address_data:
            #new_address = contact(org=new_org,
            #                      name=item['street'],
            #                      title=item['city'],
            #                      email=item['state'],
            #                      phone=item['zipcode'])
            #new_address.save()
            address.objects.create(org=new_org, **item)

        services = validated_data.pop('services')
        for item in services:
            service.objects.create(org=new_org, **item)

        eligibilities = validated_data.pop('eligibilities')
        for item in eligibilities:
            eligibility.objects.create(org=new_org)

    class Meta:
        model = organization
        fields = ('name',
                  'website',
                  'email',
                  'fax',
                  'phone',
                  'operation_hours',
                  'contact',
                  'address',
                  'services',
                  'eligibilities',
                  'financial_info',
                  'ijf')