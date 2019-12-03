from django.urls import path

from . import views

app_name = 'sightings'
urlpatterns = [
    # ex: /polls/
    path('', views.list, name='list'),
    path('stats/',views.stats, name='stats'),
    path('<str:unique_squirrel_id>/delete/',views.delete, name='delete'),
]