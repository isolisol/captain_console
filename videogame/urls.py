from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="videogame-index"),
    path('<int:id>', views.get_videogame_by_id, name="videogame_detail")
]
