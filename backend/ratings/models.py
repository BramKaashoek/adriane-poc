from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class CustomUser(AbstractUser):
    pass

class Movie(models.Model):
    pass

class Rating(models.Model):
    stars = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    movie = models.ForeignKey(
        Movie,
        related_name="ratings",
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        CustomUser,
        related_name="ratings",
        on_delete=models.CASCADE
    )
