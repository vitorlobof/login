from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('validation/', views.validation, name='validation'),
    path('login_validation/', views.login_validation, name='login_validation'),
    path('logout/', views.logout, name='logout')
]