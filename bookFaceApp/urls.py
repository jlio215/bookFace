from django.urls import path
from bookFaceApp import views
 
urlpatterns = [
    path('', views.ProductListCreateView.as_view()),    
    #path('<int:pk>/', views.cartDetailView.as_view()),    
]
