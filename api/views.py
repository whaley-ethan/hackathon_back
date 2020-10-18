from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import organization, contact, address, service, eligibility, financial_info, ijf
from .serializers import OrganizationSerializer, ContactSerializer, AddressSerializer, ServiceSerializer, EligibilitySerializer, FinancialSerializer, IJFSerializer
from rest_framework.decorators import api_view

# Create your views here.

class org(APIView):

    def get(self, request, format=None):
        params = request.query_params
        service_param = params.get('service', None)
        military_status = params.get('military_status', None)
        service_era = params.get('service_era', None)
        discharge_status = params.get('discharge_status', None)
        combat_service = params.get('combat_service', None)
        dd_214 =  params.get('dd_214', None)
        disability = params.get('disability', None)
        zipcode = params.get('zipcode', None)
        # distance = params.get('distance', None)
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
        serializer = OrganizationSerializer(data=list_of_orgs)
        serializer.is_valid()
        

        return JsonResponse(serializer.data, safe=False)

    def put(self, request):
        organization_data = JSONParser().parse(request)
        serializer = OrganizationSerializer(data=organization_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class org_list(APIView):
    
    def get(self, request):
        params = request.query_params
        key = params.get('key', 0)
        org = organization.objects.get(id=key)
        serializer = OrganizationSerializer(org)
        return JsonResponse(serializer.data)

    def put(self, request):
        organization_data = JSONParser().parse(request) 
        serializer = OrganizationSerializer(org, data=organization_data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
