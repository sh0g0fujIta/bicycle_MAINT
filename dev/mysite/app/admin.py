from django.contrib import admin
from .models import Toppage, Bicycle, Part, Color

# Register your models here.

admin.site.register(Toppage)
admin.site.register(Bicycle)
admin.site.register(Part)
admin.site.register(Color)