from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
    path('signup/',views.signup),
    path('login/',views.login),
    path('logout/',views.logout_view),
]