from django.contrib import admin
from .models import Toppage, Bicycle, Part

# Register your models here.

admin.site.register(Toppage)
admin.site.register(Bicycle)
admin.site.register(Part)