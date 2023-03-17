from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('landing_page/', views.landing_page, name='landing_page'),
    path('add_course/', views.add_course, name='add_course'),
    path('course_view/', views.course_view, name='course_view'),
    path('apply/', views.apply, name='apply'),
]