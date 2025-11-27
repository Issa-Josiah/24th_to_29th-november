from django.urls import path
from . import views
urlpatterns = [
path('One/', views.one, name='main'),
path('Two/', views.two, name='two'),

#     crud operations
path('create/', views.createFruit, name='create'),
path('readAll/', views.two, name='readAll'),
path('readOne/<str:pk>', views.readOneFruits, name='readOne'),
path('update/', views.two, name='update'),
path('delete/', views.two, name='delete'),
]
