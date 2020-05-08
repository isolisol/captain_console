from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('openinghours/', views.opening_hours, name='openinghours'),
    path('aboutus/', views.about_us, name='aboutus')
]
