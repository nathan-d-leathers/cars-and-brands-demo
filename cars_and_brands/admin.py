

# Register your models here.
from django.contrib import admin

from .models import Car, Brand
# Register your models here.

admin.site.register((Car, Brand))
