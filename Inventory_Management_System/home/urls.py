from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.index)
]