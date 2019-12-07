from django.shortcuts import render,redirect
from django.urls import reverse
from tracker.models import Squirrel
from django.db.models import Min,Count

# Create your views here.
def map(request):
	sightings = Squirrel.objects.all()[:125]
	return render(request,'map/map.html',{'sightings':sightings})
