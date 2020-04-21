from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("login", views.LoginAccountView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('settings/', views.settings, name='account_settings'),
]
