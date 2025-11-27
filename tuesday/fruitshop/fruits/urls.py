from django.contrib import admin
from django.urls import path
from . import views

# start the urlpatterns

urlpatterns = [
    path('raw/', views.raw, name='raw'),

# #     crud operations of fruits
path('create', views.create, name='create'),
path('read/', views.read_all, name='read'),
path('one/<str:pk>', views.read_one, name='one'),
path('update/<str:pk>', views.update, name='update'),
path('delete/<str:pk>', views.update, name='delete'),
path('prodelete/<str:pk>', views.prodelete, name='prodelete'),

]