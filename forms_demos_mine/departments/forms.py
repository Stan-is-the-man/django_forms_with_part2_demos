from django import forms

from forms_demos_mine.departments.models import MuscleCar


class NameForm(forms.Form):
    NAME_MAX_LEN = 50

    gender_options = (
        (1, 'Man'),
        (2, 'Woman'),
        (3, 'Who knows')
    )

    job_place_options = (
        (1, 'home office'),
        (2, 'on site'),
        (3, 'hybrid')
    )

    your_name = forms.CharField(
        label='Add first name',
        help_text='eng only',
        max_length=NAME_MAX_LEN,
    )

    your_last_name = forms.CharField(
        label='Add last name',
        help_text='eng only',
        max_length=NAME_MAX_LEN,
    )

    gender_radio_select = forms.ChoiceField(
        label='Choose your damn gender:',
        choices=gender_options,
        widget=forms.RadioSelect
    )
    #
    # gender_select = forms.ChoiceField(
    #     label='Choose your damn gender:',
    #     choices=gender_options,
    #     widget=forms.Select
    # )

    # gender_select_multiple = forms.ChoiceField(
    #     label='Choose your damn gender:',
    #     choices=gender_options,
    #     widget=forms.SelectMultiple
    # )

    work_place = forms.ChoiceField(
        choices=job_place_options,
        widget=forms.Select,

    )


# Form from a model
class MuscleCarForm(forms.ModelForm):
    class Meta:
        model = MuscleCar
        fields = '__all__'
        # change the displayed field name
        labels = {'horse_powers': 'kN'}
        # help text
        help_texts = {'modification': 'model'}

        # or specify which ones:
        # fields = ['brand', 'horse_powers']
