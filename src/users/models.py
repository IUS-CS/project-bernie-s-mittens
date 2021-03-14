from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class User(models.Model):

    # Selection choices
    STATES = [
        ('IN', 'INDIANA'),
        ('KY', 'KENTUCKY'),
    ]

    GROUPS = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    ]

    username = models.CharField(max_length=25)
    home_state = models.CharField(max_length=2, choices=STATES)
    work_state = models.CharField(max_length=2, choices=STATES)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    vaccine_group = models.CharField(max_length=1, choices=GROUPS)
    notify = models.BooleanField()
    is_notified = models.BooleanField()