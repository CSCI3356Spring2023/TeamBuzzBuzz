from django.db import models

class CourseModel(models.Model):
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