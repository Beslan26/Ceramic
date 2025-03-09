from django.urls import path
from .views import register, logout
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout_1/", LogoutView.as_view(next_page="/"), name="logout"),
    path('logout/', logout, name='logout'),
]
