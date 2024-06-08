from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('profiel/', views.profile, name="profile"),
]