from django.db import models
from users.models import CustomUser as User
# Create your models here.


class Apply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    course = models.OneToOneField(
        'add_course.Course', on_delete=models.CASCADE, default=None)
    additional_information = models.TextField(blank=True, null=True)

    supplemental_answer_1 = models.TextField(blank=True, null=True)
    supplemental_answer_2 = models.TextField(blank=True, null=True)
    supplemental_answer_3 = models.TextField(blank=True, null=True)
