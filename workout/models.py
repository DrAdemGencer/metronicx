from tkinter import CASCADE
from django.db import models
from case.models import Case

# Create your models here.
class Workout(models.Model):
    case            = models.ForeignKey(Case, on_delete=models.CASCADE)
    workout_id      = models.CharField(max_length=100)
    begin_date      = models.DateField()
    end_date        = models.DateField()
    workdays        = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.workout_id

