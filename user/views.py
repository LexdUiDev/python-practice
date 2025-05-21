from django.shortcuts import render
from rest_framework import views, status, generics
from rest_framework.response import Response
from user.serializers import UserHomeSerializer,UserSchoolSerializer




class UserHomeView(generics.GenericAPIView):
    serializer_class = UserHomeSerializer
    def get(self,request):
        text={'message':'Welcome Home'}
        return Response(data = text, status= status.HTTP_200_OK)
    

    def post(self, request):
        return Response(data={'message':'Data received'}, status=201)
    
    def delete(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request):
        return Response(data={'message':'Data received'}, status=200)
    

class UserSchoolView(generics.GenericAPIView):
    serializer_class = UserSchoolSerializer

    def post(self, request):
        return Response(data={'message': 'Done'}, status=201)
    


class UserAreaView(views.APIView):
    def get(self, request):
        return Response(data={'message ': 'ok'}, status=200)

        
    
