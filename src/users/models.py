from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class User(models.Model):

    # Selection choices
    STATES = [
        ('IN', 'INDIANA'),
        ('KY', 'KENTUCKY'),
    ]

    ESSENTIAL = [
        ('y', 'Yes'),
        ('n', "No"),
    ]

    GROUPS = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('u', 'Unknown')
    ]

    home_state = models.CharField(max_length=2, choices=STATES)
    work_state = models.CharField(max_length=2, choices=STATES)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    essential = models.CharField(max_length=1, choices=ESSENTIAL)
    vaccine_group = models.CharField(max_length=1, choices=GROUPS)

