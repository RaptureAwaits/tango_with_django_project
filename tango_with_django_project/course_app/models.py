from django.db import models
import datetime

class Year(models.Model):
    year = models.IntegerField(default=1)

    def __str__(self):
        return str(self.year)

class Course(models.Model):
    year = models.ForeignKey(Year, default=1, on_delete=models.PROTECT)
    title = models.CharField(max_length=128, default='Unnamed')
    start = models.DateField(default=datetime.date.min)
    desc = models.CharField(max_length=128, default='A course for GAs')

    def __str__(self):
        return self.title
