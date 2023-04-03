from django.db import models
from users.models import CustomUser as User


class ApplyModel(models.Model):
    additional_information = models.TextField(blank=True,null=True)

