from django.db import models
from users.models import CustomUser as User

# Create your models here.
class Offer(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="sent_offers")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="received_offers")
    course = models.ForeignKey('add_course.Course', on_delete=models.CASCADE, default=None)
