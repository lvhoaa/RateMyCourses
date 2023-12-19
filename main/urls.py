from django.urls import path, include
from . import views 


urlpatterns = [
    path('',views.home),
    path('course/<str:courseCode>',views.courseHome),
    path('ban/<str:username>',views.banBadWords)
]
