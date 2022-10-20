from django.db import models
from django.template.defaultfilters import slugify

from forms_demos_mine.departments.validators import validator_for_a_muscle_car


class MuscleCar(models.Model):
    MAX_NAME_LEN = 20

    brand = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    modification = models.CharField(
        max_length=MAX_NAME_LEN
    )

    horse_powers = models.IntegerField(validators=[validator_for_a_muscle_car])

    slug = models.SlugField(
        unique=True,
        blank=True, )

    def save(self, *args, **kwargs):
        # Create/Update - in order to use the ID when slug is not provided
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.brand}-{self.modification} ")

        # Update
        return super().save(*args, **kwargs)
