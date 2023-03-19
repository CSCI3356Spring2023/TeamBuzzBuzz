"""tasystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from login.views import login_view
from signup.views import signup_view
from add_course.views import add_course_view

# Can't render add_course if the view is from pages for some reason
urlpatterns = [
    path('', login_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('add_course/', add_course_view, name='add_course'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls),
]
