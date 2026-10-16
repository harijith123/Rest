from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from LeadApp.models import LeadModel
from LeadApp.serilaizer import LeadSerilaizer
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.




class LeadCreatListView(CreateAPIView,ListAPIView):
    serializer_class=LeadSerilaizer
    queryset=LeadModel.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields=['status','source']
    search_fields=['name','email','status','source']
    ordering_fields=['name','addes_date']

class LeadView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=LeadSerilaizer
    queryset=LeadModel.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

# class CountView(APIView):
#     authentication_classes=[authentication.BasicAuthentication]
#     permission_classes=[permissions.IsAuthenticated]
#     def get(self, request, *args, **kwargs):
#         new_leads=LeadModel.objects.filter(status="New")
#         contaccted_leads=LeadModel.objects.filter(status="contacted")
#         converted_leads=LeadModel.objects.filter(status="Converted")
#         lost_leads=LeadModel.objects.filter(status="Lost")
#         new_lead_serializer=LeadSerilaizer(newp)