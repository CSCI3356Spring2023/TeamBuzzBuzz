from django.db import models
from users.models import CustomUser as User
from django.urls import reverse

class Course(models.Model):
    SEMESTER = [
        ('FALL', 'Fall'),
        ('Spring', 'Spring'),
    ]
    course_title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    semester = models.CharField(max_length=100, choices=SEMESTER)

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='added_old_courses')

    def __str__(self):
        return self.course_title
    
    def get_absolute_url(self):
        return reverse('home')
