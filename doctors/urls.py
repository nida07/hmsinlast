from django.urls import path
from . import views
#app name set for namespacr concept to avoid conflict of naming
app_name='doctors'

urlpatterns = [

    path('d_login', views.d_login, name='d_login'),
    path('d_register', views.d_register, name='d_register'),


    ]