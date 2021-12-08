from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(state)
admin.site.register(city)
admin.site.register(Country)
admin.site.register(cityLocations)