from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('houses/', views.houses, name='houses'),
    path('about/', views.about, name='about'),
    path('<slug:city>/', views.houses, name='houses_by_city'),
]