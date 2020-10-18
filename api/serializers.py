from rest_framework import serializers 
from .models import organization, address, service, eligibility, ijf

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


class IJFSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ijf
        fields = ('participant_name',
                  'participant_location',
                  'requestinfo')

class OrganizationSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    services = ServiceSerializer(many=True)
    eligibilities = EligibilitySerializer(many=True)
    ijf = IJFSerializer()

    def create(self, validated_data):
        new_org = organization.objects.create(name = validated_data.pop('name'),
                                              contact_name = validated_data.pop('contact_name'),
                                              email = validated_data.pop('email'),
                                              website = validated_data.pop('website'),
                                              fax = validated_data.pop('fax'),
                                              phone = validated_data.pop('phone'),
                                              phone_ext = validated_data.pop('phone_ext'),
                                              )

        # address_data = validated_data.pop('address')
        # for item in address_data:
        #     new_address = contact(org=new_org,
        #                          name=item['street'],
        #                          title=item['city'],
        #                          email=item['state'],
        #                          phone=item['zipcode'],
        #                          )
        #     new_address.save()
        #     address.objects.create(org=new_org, **item)

        # services = validated_data.pop('services')
        # for item in services:
        #     service.objects.create(org=new_org, **item)

        # eligibilities = validated_data.pop('eligibilities')
        # for item in eligibilities:
        #     eligibility.objects.create(org=new_org)

    class Meta:
        model = organization
        fields = ('name',
                  'contact_name'
                  'email',
                  'website',
                  'fax',
                  'phone',
                  'address',
                  'services',
                  'eligibilities',
                  'ijf',
                  )