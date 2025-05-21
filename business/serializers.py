from rest_framework import serializers
from business.models import Business


class BusinessSerializer(serializers.ModelSerializer):
    name= serializers.CharField(max_length=100)
    type= serializers.CharField(max_length=250)
    country= serializers.CharField(max_length=250)
    state= serializers.CharField(max_length=250)
    street= serializers.CharField(max_length=200)
    city= serializers.CharField(max_length=100)
    phone= serializers.CharField(max_length=25)
    logo= serializers.ImageField()


    class Meta:
        model= Business
        fields= ['id', 'name', 'logo', 'type','country', 'state', 'phone', 'street', 'created_at', 'city',  ]