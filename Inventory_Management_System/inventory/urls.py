from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.inventory),
  path('search/', views.search_products, name='search_products'),
  path('add/', views.add_product, name='add_product'),
  path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
  path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]