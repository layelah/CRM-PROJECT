from django.urls import path
from . import views

urlpatterns = [
   
    path('inscription',views.page_inscription,name="inscription"),
    path('login',views.page_login,name="login"),
    path('logout',views.logout_user,name="logout"),
]
