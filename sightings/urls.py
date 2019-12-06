from django.urls import path
from . import views

urlpatterns =[ 
    path('', views.all_sightings),
    path('add/', views.add_sightings),
    path('<str:squirrel_id>/', views.update_sightings),
    path('stats/', views.stats),
]
