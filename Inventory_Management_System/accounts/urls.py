from django.urls import path
#now import the views.py file into this code
from . import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('signup/',views.signup),
    # path('login/',views.login),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',views.logout_view),
]