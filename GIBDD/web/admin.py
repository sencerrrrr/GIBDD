from django.contrib import admin
from .models import Role, User, Region, CarNumber

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Region)
admin.site.register(CarNumber)