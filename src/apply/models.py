from django.db import models
from users.models import CustomUser as User
# Create your models here.

class Apply(models.Model):
    additional_information = models.TextField(blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    

