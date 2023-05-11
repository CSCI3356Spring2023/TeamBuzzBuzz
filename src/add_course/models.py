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

    DAYS = [
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('TH', 'Thursday'),
        ('F', 'Friday'),
    ]

    TIMES = [
        ('8:00', '8:00'),
        ('8:30', '8:30'),
        ('9:00', '9:00'),
        ('9:30', '9:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('1:00', '1:00'),
        ('1:30', '1:30'),
        ('2:00', '2:00'),
        ('2:30', '2:30'),
        ('3:00', '3:00'),
        ('3:30', '3:30'),
        ('4:00', '4:00'),
        ('4:30', '4:30'),
        ('5:00', '5:00'),
    ]

    course_title = models.CharField(max_length=100)

    # new
    course_number = models.CharField(max_length=100, default=0)
    course_section = models.IntegerField(default=0)
    course_day = models.CharField(max_length=100, choices=DAYS)
    course_time = models.CharField(max_length=100, choices=TIMES)
    homework_graded_in_meetings = models.BooleanField(default=True)
    office_hours = models.IntegerField(default=0)
    additional_info = models.CharField(max_length=100, default=0)
    # end new

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


class Discussion(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, default=None, related_name='discussions')

    number = models.CharField(max_length=100)

    day = models.CharField(max_length=100, choices=Course.DAYS)
    time = models.CharField(max_length=100, choices=Course.TIMES)

    ta = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, related_name='discussion_ta', blank=True, null=True)

    def __str__(self):
        return self.discussion_section
