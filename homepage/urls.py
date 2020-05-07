from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('openinghours/', views.opening_hours, name='opening_hours'),
    path('aboutus/', views.about_us, name='about_us')
]