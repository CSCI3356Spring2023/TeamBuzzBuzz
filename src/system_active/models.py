from django.db import models

# Create your models here.

class SystemStatus(models.Model):
    system_active = models.BooleanField(default=True)

def __str__(self):
    return "System Status"