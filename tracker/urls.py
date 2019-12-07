from django.urls import path

from . import views

app_name = 'sightings'
urlpatterns = [
    # ex: /polls/
    path('', views.list, name='list'),
    path('stats/',views.stats, name='stats'),
    path('add/', views.add, name='add'),
    path('<str:unique_squirrel_id>/', views.update, name='update'),
    path('<str:unique_squirrel_id>/delete/',views.delete, name='delete'),
]