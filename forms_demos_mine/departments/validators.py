from django.core.exceptions import ValidationError


def validator_for_a_muscle_car(value):
    min_hp = 200
    if value < min_hp:
        raise ValidationError(f"HP must be at least {min_hp}hp")
