from django.contrib import admin
from .models import User, Bicycle, Part

# Register your models here.

admin.site.register(User)
admin.site.register(Bicycle)
admin.site.register(Part)