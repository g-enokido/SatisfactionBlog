from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [path('new/', SignUpView.as_view(), name='signup'),
               path('settings/', views.Create_blog, name='blog_settings'), ]
