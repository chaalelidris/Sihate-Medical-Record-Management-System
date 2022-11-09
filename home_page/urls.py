from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),

    path("login/", views.user_login, name="login"),
    path("login-mobile/", views.user_login_mobile, name="login-mobile")
    #path("contact", views.contact, name="contact"),
]
