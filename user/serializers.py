from rest_framework import serializers

class UserHomeSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    age=serializers.IntegerField()
    gender=serializers.ChoiceField(choices=['male','female'])
    suscribe=serializers.BooleanField()



class UserSchoolSerializer(serializers.Serializer):
    name=serializers.CharField()
    location=serializers.CharField()


