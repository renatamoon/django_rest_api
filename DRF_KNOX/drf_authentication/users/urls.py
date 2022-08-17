# STANDARD IMPORTS
from django.urls import path
from knox import views as knox_views

# PROJECT IMPORTS
from . import views

urlpatterns = [
    path('login/', views.login_api),
    path('user/', views.get_user_data),
    path('register/', views.register_api),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view())
]
