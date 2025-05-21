from django.urls import path
from business.views import BusinessView



urlpatterns= [
    path('', BusinessView.as_view())

]