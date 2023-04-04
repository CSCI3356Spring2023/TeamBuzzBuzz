from django.db import models
from users.models import CustomUser as User

# Create your models here.
class Offer(models.Model):
    ACCEPTED = 'A'
    PENDING = 'IP'
    COMPLETED = 'C'
    STATUS_CHOICES = [
        (ACCEPTED, 'Accepted'),
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]

    OFFER_STATUS = {}

    time_stamp = models.DateTimeField(auto_now_add=True)
    offer_status = models.CharField(choices="", default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    course = models.ForeignKey('add_course.Course', on_delete=models.CASCADE, default=None)
