from django.http import HttpResponseRedirect
from django.shortcuts import render

from forms_demos_mine.departments.forms import NameForm, MuscleCarForm


def add_new_name(request):
    if request.method == 'GET':
        form = NameForm()
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thanks/')

    context = {
        'form': form,
    }
    return render(request, 'add_new.html', context)


def add_new_muscle_car(request):
    if request.method == 'GET':
        model_form = MuscleCarForm()
    if request.method == 'POST':
        model_form = MuscleCarForm(request.POST)
        if model_form.is_valid():
            return HttpResponseRedirect('thanks/')

    context = {
        'model_form': model_form,
    }
    return render(request, 'new_muscle_car.html', context)


def thank_you(request):
    return render(request, 'thank_you.html')
