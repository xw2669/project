from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Squirrel
from django.db.models import Min,Count

# Create your views here.
def map(request):
	sightings = Squirrel.objects.all()[:125]
	return render(request,'map/map.html',{'sightings':sightings})

def list(request):
	sightings = Squirrel.objects.all()[:125]
	return render(request,'sightings/list.html',{'sightings':sightings})

def delete(request,unique_squirrel_id):
	del_sighting = Squirrel.objects.filter(unique_squirrel_id=unique_squirrel_id)
	del_sighting.delete()
	return redirect(reverse('sightings:list'))

def stats(request):
	data = Squirrel.objects.all()
	long_attr = data.aggregate(min_longitude = Min('longitude'))
	la_attr = data.aggregate(min_latitude = Min('latitude'))
	date_attr = data.aggregate(min_date = Min('date'))
	return render(request, 'sightings/stats.html',{"long_attr":long_attr,"la_attr":la_attr,"date_attr":date_attr})