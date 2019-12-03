from django.urls import path

from . import views

app_name = 'map'
urlpatterns = [
    # ex: /polls/
    path('', views.map, name='map'),
]