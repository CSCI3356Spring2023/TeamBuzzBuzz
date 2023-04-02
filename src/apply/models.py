from django.db import models
from users.models import CustomUser as User


class ApplyModel(models.Model):
    additional_information = models.TextField(blank=True,null=True)
    course_title = models.CharField(max_length=100)
    email = models.EmailField()
    discussion = models.CharField(max_length=100)
    ta_required = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    additional_information = models.TextField(blank=True,null=True)

