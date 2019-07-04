from django.urls import path
from .views import homepageview,About
urlpatterns = [
path('', homepageview.as_view(), name='home'),
path('about/',About.as_view(),name='about')
]
