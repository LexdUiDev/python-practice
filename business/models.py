from django.db import models
import uuid
#from user.models import CustomUser
from django.contrib.auth import get_user_model


# Create your models here.
User= get_user_model()


class Business(models.Model):
    id= models.UUIDField(primary_key= True,default=uuid.uuid4,editable= False)
    name= models.CharField(max_length=100)
    type= models.CharField(max_length=250)
    country= models.CharField(max_length=250)
    state= models.CharField(max_length=250)
    city= models.CharField(max_length=250)
    street= models.CharField(max_length=200)
    phone= models.CharField(max_length=25)
    logo= models.ImageField(upload_to= 'business/')
    is_active= models.BooleanField(default=True)
    owner= models.ForeignKey(User, on_delete= models.CASCADE)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    #def __str__(self):
        #return f'{self.name} by {self.owner.firstname} {self.owner.lastname}'
        