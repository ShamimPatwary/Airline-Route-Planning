from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('airports/', views.manage_airports, name='manage_airports'),
    path('airports/delete/<str:code>/', views.delete_airport, name='delete_airport'),
    path('routes/', views.manage_routes, name='manage_routes'),
    path('routes/delete/<int:id>/', views.delete_route, name='delete_route'),
]
