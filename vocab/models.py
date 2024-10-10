from django.db import models

# Create your models here.
class Word(models.Model):
  french = models.CharField(max_length=150)
  english = models.CharField(max_length=150)
  howmanytime = models.IntegerField(default=0)
