from . import  views
from django.urls import path
from .views import *


app_name = 'Login'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('login/', views.LoginClass.as_view(), name='login'),
    path('viewuser/', views.ViewUser.as_view(), name='userview'),
    path('view-pro/', view_product, name='view-pro'),
    path('addpost/', views.AddPost.as_view(), name='addpost')
]