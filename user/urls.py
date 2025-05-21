from django.urls import path
from user.views import UserHomeView, UserSchoolView, UserAreaView




urlpatterns = [
    path ('home/', UserHomeView.as_view()),
    path('School/',UserSchoolView.as_view()),
    path('area/',UserAreaView.as_view())

]