from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
from rest_framework_simplejwt.tokens import RefreshToken

GENDER_CHOICES= [
    ('MALE', 'Male'),
    ('FEMALE', 'Female')
]

USER_CHOICES= [
    ('CUSTOMER', 'custumer'),
    ('RIDER', 'rider'),
    ('STAFF', 'staff'),
    ('ADMIN', 'admin')
]

# Create your models here.

class userManger(BaseUserManager):
    
    def _create_user(self,email,password, **extra_filesd):
        if not email:
            raise ValueError('Email must be provided')
        if not password:
         raise ValueError('Password must be provided')
        user= self.model(email= self.normalize_email(email),user_types='Admin')
        user.password(password)
        user.save()
        return user 
    
    def create_user(self, firstname, lastname, email, phone, password = None, **extra_fied):
        if not email:
            raise TypeError('User should have a email')
        if not firstname:
            raise TypeError('User should have a fisrtname ')
        if not lastname:
            raise TypeError('User should have a lastname')
        

        user=self.model(firstname=firstname, lastname=lastname, email=self.normalize_email(email), phone=phone)
        user.set_password(password)
        user.save

        return user
    def create_superuser(self, fisrtname, lastname, email, phone, password=None):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(email, password)
        user.is_superuser= True
        user.is_staff= True
        user.is_verified=True
        user.role= 'ADMIN'
        user.save

        return user
        




class CustomUser(AbstractBaseUser, PermissionsMixin):
    id= models.UUIDField(primary_key= True,default=uuid.uuid4,editable= False)
    email= models.EmailField(max_length=255,unique= True)
    firstname=models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    date_of_birth=models.DateField()
    phone= models.CharField(max_length=15, unique= True)
    gender= models.CharField(max_length= 6, choices=GENDER_CHOICES)
    nationality= models.CharField(max_length= 100)
    address= models.TextField(null= True, blank= True)
    is_verified= models.BooleanField(default= False)
    is_active= models.BooleanField(default= True)
    is_staff= models.BooleanField(default= False)
    user_type= models.CharField(max_length=10, choices=USER_CHOICES, default=USER_CHOICES[0][0])
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['firstname', 'lastname', 'phone']
    profile_picture= models.ImageField(upload_to='profile picture', null=True,blank=True)
    objects= userManger()


    # def _str_(self):
    #     return f'{self.firstname} - {self.phone}'


    def tokens(self):
        refresh= RefreshToken.for_user(self)
        return{
            'refresh': str(refresh), 
            'access' : str(refresh.access_token)
        
        }
    


    class Meta:
        db_table= 'user'
        