from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from authentication.serializers import SignUpSerializer, LoginSerializer
from user.models import CustomUser



# Create your views here.
class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    def post(self, request):
        Serializer= self.serializer_class(data=request.data)
        Serializer.is_valid(raise_exception=True)
        email= Serializer.validated_data.get('email').lower()
        phone= Serializer.validated_data.get('phone')
        email_exist= CustomUser.objects.filter(email= email).first()
        password = Serializer.validated_data.get('password')


        if email_exist:
            return Response(data={'error': 'Email already exist'}, status=400)
        
        phone_exist= CustomUser.objects.filter(phone= phone).first()

        if phone_exist:
            return Response(data={'message': 'phone already exist'}, status=400)
        
        Serializer.save(email=email)
    
        user= Serializer.save()
        user.set_password(password)
        user.save()
        print(user.email, user.password)
        return Response(Serializer.data, status=201)
    


class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    def post(self, request):
        Serializer=self.serializer_class(data=request.data)
        Serializer.is_valid(raise_exception=True)

        return Response(data= Serializer.data, status= 201)

