from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    path('contactus/', views.contactus, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('service/', views.service, name='service'),

]
