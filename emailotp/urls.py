from django.urls import path
from . import views

urlpatterns = [
    path('api/send-otp/', views.send_otp),
    path('api/verify-otp/', views.verify_otp),
]
