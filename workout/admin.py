from django.contrib import admin
from .models import Workout

# Register your models here.
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('case', 'begin_date', 'end_date', 'workdays',  'is_available')

admin.site.register(Workout, WorkoutAdmin)
