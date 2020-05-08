from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="accessories-index"),
    path('<int:id>', views.get_accessory_by_id, name="accessory_detail")
]
