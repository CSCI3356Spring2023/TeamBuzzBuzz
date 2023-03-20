from django.db import models

# Create your models here.
class ApplyModel(models.Model):
    additional_information = models.TextField(blank=True,null=True)