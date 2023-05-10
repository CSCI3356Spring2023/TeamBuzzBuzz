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
    #new
    course_number = models.CharField(max_length=100, default=0)
    course_section = models.IntegerField(default=0)
    course_date = models. DateTimeField (null=True)
    homework_graded_in_meetings = models.BooleanField(default=True)
    #end new
    status = models.BooleanField(default=True)
    email = models.EmailField()
    discussion = models.CharField(max_length=100, choices=DISCUSSION)
    ta_required = models.CharField(max_length=100, choices=OPTIONS)
    description = models.CharField(max_length=100)
    num_positions_filled = models.IntegerField(default=0)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, related_name='added_courses')

    supplemental_question_1 = models.CharField(
        max_length=100, default=None, blank=True)
    supplemental_question_2 = models.CharField(
        max_length=100, default=None, blank=True)
    supplemental_question_3 = models.CharField(
        max_length=100, default=None, blank=True)

    current_tas = models.ManyToManyField(
        User, related_name='current_tas', blank=True)

    def __str__(self):
        return self.course_title

    def get_absolute_url(self):
        return reverse('home')

    def at_capacity(self):
        return self.current_tas.count() >= int(self.ta_required)
