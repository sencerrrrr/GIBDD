from django.contrib import admin
from .models import Role, User, Region, CarNumber, CarBrand, CarModel, Car, ContactHistory, CarOwner

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Region)
admin.site.register(CarNumber)
admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(ContactHistory)
admin.site.register(CarOwner)
