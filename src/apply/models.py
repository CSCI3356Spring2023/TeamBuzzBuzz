from django.db import models
from users.models import CustomUser as User

# Create your models here.
class ApplyModel(models.Model):
    additional_information = models.TextField(blank=True,null=True)
    


        
