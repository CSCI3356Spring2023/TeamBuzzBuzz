from django.db import models
from users.models import CustomUser as User
from add_oldcourse.models import Course
from django.urls import reverse

class OldCourse(models.Model):
    SEMESTER = [
        ('FALL', 'Fall'),
        ('Spring', 'Spring'),
    ]
    course_title = models.CharField(max_length=100, default = None)
    year = models.CharField(max_length=100, default = None)
    semester = models.CharField(max_length=100, choices=SEMESTER, default = None)

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='old_courses_creator')
    taker = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='old_courses_taker')
    def __str__(self):
        return self.course_title
    
    def get_absolute_url(self):
        return reverse('home')