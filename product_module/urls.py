from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductlistView.as_view(), name="product-list"),
    path("productfavorite", views.AddToFavView.as_view(), name="product-fav"),
    path("<slug:slug>", views.ProductDetailsView.as_view(), name="product-details"),
]
