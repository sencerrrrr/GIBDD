from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Car, ContactHistory, Region, CarBrand, CarModel, CarNumber
from .forms import UserForm, CarForm, ContactHistoryForm

def index(request):
    return render(request, 'index.html')

def profile(request):
    users = User.objects.all()
    return render(request, 'profile.html', {'users': users})

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserForm()
    return render(request, 'register_user.html', {'form': form})

def register_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car_number_obj = CarNumber(region=car.region)
            car_number_obj.number = CarNumber.generate_number(car.region.number)
            car_number_obj.save()
            car.number = car_number_obj
            car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'register_car.html', {'form': form})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def contact_history_list(request):
    histories = ContactHistory.objects.all()
    return render(request, 'contact_history_list.html', {'histories': histories})
