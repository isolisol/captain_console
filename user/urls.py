from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='homepage'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('editprofile', views.edit_profile, name='editprofile'),
    path('editprofileimg', views.edit_photo, name='editimage'),
    path('past_orders', views.past_orders, name='past_orders'),
    path('past_orders/<int:order_id>', views.past_order, name="past_order"),
    path('delete_image', views.delete_profile_img, name="delete_img"),
    path('search_history', views.see_search_history, name="search_history"),
    path('delete_search_history', views.delete_search_history, name="delete_searches")
]
