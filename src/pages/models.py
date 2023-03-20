from django.db import models

# Create your models here.
class Apply(models.Model):
    title = models.TextField()#connect to course creation 
    positions_open = models.IntegerField()
    expected_hours = models.IntegerField()
    description = models.TextField()
    additional_information = models.TextField(blank=True,null=True) #don't need to have additional information