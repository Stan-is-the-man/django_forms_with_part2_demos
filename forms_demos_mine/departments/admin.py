from django.contrib import admin

from forms_demos_mine.departments.models import MuscleCar


@admin.register(MuscleCar)
class MuscleCarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'modification', 'horse_powers', 'slug',)
