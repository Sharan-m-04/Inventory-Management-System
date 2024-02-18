from django.urls import path

#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.transactions),
  path('delete/<int:t_id>/', views.delete_transaction, name='delete_transaction'),
]