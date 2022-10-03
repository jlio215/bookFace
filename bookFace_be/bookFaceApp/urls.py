from django.urls import path
from bookFaceApp import views
 
urlpatterns = [
    path('inventory/', views.InventoryCreateView.as_view()),
    path('products/', views.productsHomeView.as_view()),
    path('createProduct/', views.productsView.as_view()),
    path('cart/', views.cartView.as_view()),
    path('sales/', views.salesView.as_view()),
    path('inventory/<int:pk>/', views.InventoryCreateView.as_view()),
    path('products/<int:pk>/', views.productsView.as_view()),
    path('cart/<int:pk>/', views.cartView.as_view()),
    path('sales/<int:pk>/', views.salesView.as_view())

]
