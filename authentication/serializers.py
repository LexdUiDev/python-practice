from rest_framework import serializers
from user.models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class SignUpSerializer(serializers.ModelSerializer):
    firstname= serializers.CharField(max_length=255)
    lastname= serializers.CharField(max_length=255)
    email= serializers.EmailField()
    password= serializers.CharField(min_length=8, max_length=68, write_only=True)
    gender= serializers.ChoiceField(choices=['MALE', 'FEMALE'])
    phone= serializers.CharField(max_length= 11)
    address= serializers.CharField()
    nationality= serializers.CharField(required=False)
    date_of_birth= serializers.DateField()
    profile_picture= serializers.ImageField(required=False)
    user_type= serializers.ChoiceField(choices=['CUSTOMER', 'RIDER','STAFF', 'ADMIN'])


    class Meta:
        model= CustomUser
        fields=['firstname', 'lastname','password', 'email', 'phone','gender', 'address', 'nationality', 'date_of_birth', 'profile_picture','user_type']


class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    password=serializers.CharField(min_length=8, max_length=68, write_only=True)

    class Meta:
        model= CustomUser
        fields=['id','email', 'password','tokens']


    def validate(self, attrs):
            email= attrs.get('email').lower()
            password= attrs.get('password')
            user= auth.authenticate(email=email, password=password)
            if not user:
                raise AuthenticationFailed('invalid login credentials')
            return{
                'id': user.id,
                'email': user.email,
                'tokens': user.tokens
            }