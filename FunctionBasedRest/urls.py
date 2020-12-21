from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiView),
    path('list/', views.List, name='list'),
    path('update/<str:pk>/', views.Update, name='update')
]
