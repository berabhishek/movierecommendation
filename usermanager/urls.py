from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns  = [
    path('', views.loginpage, name = "login"),
    path('home',views.home, name = "home"),
    path('verify_login',views.verify_login, name = "verify_login"),
    path('create_account',views.create_account, name = "create_account"),
    path('logout', LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name = "logout")
]