from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class=CompanySerializer
    permission_classes=[IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    #companies/{companyId}/emplyees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):   
        try:                
            company=Company.objects.get(pk=pk)
            print(company)
            emps=Employee.objects.filter(company=company)
            print(emps)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists !! Error'
            })
            
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    # permission_classes=[IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
#     [
#     {
#         "url": "http://127.0.0.1:8080/api/v1/companies/1/",
#         "company_id": 1,
#         "name": "Learn Code With Durgesh",
#         "location": "Lucknow",
#         "about": "This company is related to software development and training.",
#         "type": "IT",
#         "added_date": "2022-08-30T10:26:01.500181Z",
#         "active": true
#     },
#     {
#         "url": "http://127.0.0.1:8080/api/v1/companies/2/",
#         "company_id": 2,
#         "name": "TechSoft INDIA",
#         "location": "Lucknow",
#         "about": "This company is related to software development and training.",
#         "type": "Mobiles Phones",
#         "added_date": "2022-08-30T10:26:30.843673Z",
#         "active": true
#     }
# ]