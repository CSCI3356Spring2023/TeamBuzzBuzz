from django.db import models
from users.models import CustomUser as User
from django.urls import reverse


class Course(models.Model):
    OPTIONS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    )
    DISCUSSION = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]
    course_title = models.CharField(max_length=100)
    email = models.EmailField()
    discussion = models.CharField(max_length=100, choices=DISCUSSION)
    ta_required = models.CharField(max_length=100, choices=OPTIONS)
    description = models.CharField(max_length=100)

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.course_title

    def get_absolute_url(self):
        return reverse('home')


class SupplementalQuestion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text
