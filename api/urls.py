from django.urls import path
from . import views

urlpatterns = [
    path('sendmail/', views.send_email),
    path('sendmailwithtemplate/', views.send_email_with_template)
]