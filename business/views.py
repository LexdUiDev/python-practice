from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response
from business.serializers import BusinessSerializer 
from rest_framework.permissions import IsAuthenticated
from business.models import Business
from utils.pagination import CustomPagination
from utils.permission import IsFemaleUser
# Create your views here.

class BusinessView(generics.GenericAPIView):
    serializer_class= BusinessSerializer
    permission_classes= [IsAuthenticated, ]
    pagination_class= CustomPagination

    def post(self, request):
        serializer=  self.serializer_class(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner= request.user)
        return Response(data= serializer.data, status=201)
    def get_queryset(self):
        user= self.request.user
        user_businesses= Business.objects.filter(owner= user)
        return user_businesses
    
    def get(self, request):
        businesses= self.get_queryset()
        page= self.paginate_queryset(businesses)
        if page: 
            serializer= self.serializer_class(businesses, many=True)
            return Response(data= serializer.data, status= 200)
        serializer= self.serializer_class(businesses, many= True)

        return Response(data= serializer.data, status=200)