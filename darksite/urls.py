from django.urls import path
from . import views
from .views import login_view, register_view, logout_view, home_view, background_image_view
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    path('change-background/', background_image_view, name='change_background'),
]