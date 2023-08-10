from django.db import models
from django.conf import settings
from django.utils import timezone, duration, dateformat
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Experience(models.Model):
    role_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    # start_date = models.DateField()
    # end_date = models.DateField()
    # duration = end_date - start_date
#     image = models.ImageField(upload_to='static/images')
#     url = models.URLField(blank=True)
#     skill = models.ArrayField(models.CharField(max_length=100),size=20)
#     bullet = models.CharField(max_length=1000)


