from . import views
from django.urls import path
#app name set for namespacr concept to avoid conflict of naming
app_name='credentials'

urlpatterns = [

    path('register', views.register, name='register'),
    path('user_register', views.user_register, name='user_register'),
    path('login',views.login,name='login'),
    path('user_login',views.user_login,name='user_login'),
    path('logout',views.logout,name='logout'),
    path('viewuser',views.viewuser,name='viewuser'),
    path('user_biometric_edit',views.user_biometric_edit,name='user_biometric_edit'),
    # path('base',views.base,name='base'),


]
