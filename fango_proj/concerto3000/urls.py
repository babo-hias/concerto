from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path("", include("django.contrib.auth.urls")),
    path('table/', views.table, name='table'),
    path('timeline/', views.timeline, name='timeline'),
    path('artists/', views.artists, name='artists'),
    path('locations/', views.locations, name='locations'),
    path('table/add/', views.add, name='add'),
    path('table/add/addrecord/', views.addrecord, name='addrecord'),
    path('table/add_txt/', views.add_txt, name='add_txt'),
    path('table/add_txt/addrecords_txt/', views.addrecords_txt, name='addrecords_txt'),
    path('table/delete/', views.delete, name='delete'),
    path('table/delete/deleted/<int:id>', views.deleted, name='deleted')
]
