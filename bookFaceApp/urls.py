from django.urls import path
from bookFaceApp import views
 
urlpatterns = [
    path('inventory/', views.InventoryCreateView.as_view()),
    path('list/', views.ProductListCreateView.as_view()),
    path('cart/', views.cartView.as_view()),
    path('sales/', views.salesView.as_view()),
    
    ]
    