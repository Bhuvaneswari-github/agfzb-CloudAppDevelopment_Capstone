from django.contrib import admin
# from .models import related models
from .models import CarMake
from .models import CarModel

# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)
# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarMake 
   # model = CarModel
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [CarModelInline]
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [CarModelInline]
# Register models here
