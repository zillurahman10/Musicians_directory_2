from django.urls import path, include
from . import views

urlpatterns = [
    path('add_album/', views.AddAlbumCreateView.as_view(), name="add_album")
]