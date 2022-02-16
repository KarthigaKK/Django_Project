from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home,name='blog-home'), # home page empty route pattern from urls.py
    path('about/',views.about,name='blog-about'),
]