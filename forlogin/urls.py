from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.signupuser,name='signupuser'),
]
