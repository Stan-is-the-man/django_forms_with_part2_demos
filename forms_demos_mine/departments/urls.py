from django.urls import path

from forms_demos_mine.departments.views import add_new_name, thank_you, add_new_muscle_car

urlpatterns = [
    path('new-name', add_new_name, name='new name'),
    path('thanks/', thank_you, name='thanks'),
    path('new-car', add_new_muscle_car, name='new muscle car'),



]