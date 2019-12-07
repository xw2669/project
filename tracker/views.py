from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Squirrel
from django.db.models import Min,Count
from .form import SquirrelForm

# Create your views here.
def list(request):
	sightings = Squirrel.objects.all()
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
	age_attr = data.values_list('age').annotate(Count('age'))
	color_attr = data.values_list('primary_fur_color').annotate(Count('primary_fur_color'))

	return render(request, 'sightings/stats.html',{"long_attr":long_attr,"la_attr":la_attr,"date_attr":date_attr, "age_attr":age_attr,"color_attr":color_attr})

def update(request,unique_squirrel_id):
	data = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
	if request.method == "POST":
		form = SquirrelForm(request.POST, instance=data)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/{unique_squirrel_id}')
	else:
		form = SquirrelForm(instance=data)
	context={
		'form':form,
		'id':unique_squirrel_id
	}
	return render(request,'sightings/update.html',context)

def add(request):
	if request.method == "POST":
		form = SquirrelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/')
	else:
		form = SquirrelForm()
	context={
		'form':form
	}
	return render(request,'sightings/update.html',context)



