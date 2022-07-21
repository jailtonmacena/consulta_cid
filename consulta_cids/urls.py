from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home.html"),
    path('search_cid/', views.buscar_cids, name="search.html"),
]
