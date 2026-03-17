from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import sitemaps

urlpatterns = [
    path('', views.home, name='home'),
    path('houses/', views.houses, name='houses'),
    path('about/', views.about, name='about'),
    path('robots.txt', views.robots_txt, name='robots'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('<slug:city>/', views.houses, name='houses_by_city'),
]