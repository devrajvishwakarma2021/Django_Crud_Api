from django.urls import path
from api import views
urlpatterns = [
    # path('', views.apiOverview, name='apiOverview'),
    path('product-list/', views.showall, name='product-list'),
    path('product-detail/<int:pk>/', views.ViewOneProduct, name='product-detail'),
    path('product-create/', views.CreatProduct, name='product-create'),
    path('product-update/<int:pk>/', views.UpdateProduct, name='product-update'),
    path('product-delete/<int:pk>/', views.DeleteProduct, name='product-delete'),


         

]
