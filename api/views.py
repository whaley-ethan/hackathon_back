from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import organization, contact, address, service, eligibility, financial_info, ijf
from .serializers import OrganizationSerializer, ContactSerializer, AddressSerializer, ServiceSerializer, EligibilitySerializer, FinancialSerializer, IJFSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'PUT'])
def org(request):
    params = request.query_params
    service_param = params.get('service', None)
    military_status = params.get('military_status', None)
    service_era = params.get('service_era', None)
    discharge_status = params.get('discharge_status', None)
    combat_service = params.get('combat_service', None)
    dd_214 =  params.get('dd_214', None)
    disability = params.get('disability', None)
    zipcode = params.get('zipcode', None)
    distance = params.get('distance', None)

    if request.method == 'GET':
        list_of_orgs = organization.objects.all()
        
        if service is not None:
            services = service.objects.filter(name=service_param)
            list_of_orgs = list_of_orgs.filter(services__in=services)
        if military_status is not None:
            eligibilities = eligibility.objects.filter(value=military_status)
            list_of_orgs = list_of_orgs.filter(eligibilities__in=eligibilities)
        if service_era is not None:
            eligibilities = eligibility.objects.filter(value=service_era)
            list_of_orgs = list_of_orgs.filter(eligibilities__in=eligibilities)
        if discharge_status is not None:
            eligibilities = eligibility.objects.filter(value=discharge_status)
            list_of_orgs = list_of_orgs.filter(eligibilities__in=eligibilities)
        if combat_service is not None:
            eligibilities = eligibility.objects.filter(value=combat_service)
            list_of_orgs = list_of_orgs.filter(eligibilities__in=eligibilities)
        if dd_214 is not None:
            eligibilities = eligibility.objects.filter(value=dd_214) # Yes or No
            list_of_orgs = list_of_orgs.filter(eligibilities__in=eligibilities)
        if disability is not None:
            eligibilities = eligibility.objects.filter(value=disability) # Yes or No
            list_of_orgs = list_of_orgs.filter(eligibilities__in=eligibilities)
        

        return JsonResponse(serial_serializer.data, safe=False)

    elif request.method == 'PUT':
        serial_data = JSONParser().parse(request)
        serial_serializer = SerialSerializer(data=serial_data)
        if serial_serializer.is_valid():
            serial_serializer.save()
            return JsonResponse(serial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = serialnum.objects.all().delete()
        return JsonResponse({'message': '{} serialnums were deleted successfully!'.format(count[0])}, 
                            status=status.HTTP_204_NO_CONTENT)

    return

@api_view(['GET', 'PUT', 'DELETE'])
def org_list(request, key):
    serial = serialnum.objects.get(number=key)
    if request.method == 'GET':
        serial_serializer = SerialSerializer(serial)
        return JsonResponse(serial_serializer.data)

    elif request.method == 'PUT':
        serial_data = JSONParser().parse(request) 
        serial_serializer = SerialSerializer(serial, data=serial_data) 
        if serial_serializer.is_valid(): 
            serial_serializer.save() 
            return JsonResponse(serial_serializer.data) 
        return JsonResponse(serial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        serial.delete() 
        return JsonResponse({'message': 'Serial was deleted successfully!'}, 
                            status=status.HTTP_204_NO_CONTENT)

    return

@api_view(['GET'])
def serial_list_published(request):
    serials = serialnum.objects.filter(published=True)      
    if request.method == 'GET': 
        serial_serializer = SerialSerializer(serials, many=True)
        return JsonResponse(serial_serializer.data, safe=False)

    return
