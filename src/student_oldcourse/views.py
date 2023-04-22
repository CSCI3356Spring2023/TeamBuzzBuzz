from django.shortcuts import render, redirect, get_object_or_404
from add_oldcourse.models import Course
from student_oldcourse.models import OldCourse
from users.models import CustomUser
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist


class StudentOldCoursesView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'show_studentoldcourse/show_studentoldcourse.html'
    ordering = ['course_title']
    context_object_name = 'course_data'

    def get_queryset(self, *args, **kwargs):
        key = self.kwargs['pk']
        print("Key:", key)
        try:
            print('hello')
            user = CustomUser.objects.get(pk=key)
            print("User:", user)
            courses = OldCourse.objects.filter(taker=user)
            print("Courses:", courses)
            return courses
        except ObjectDoesNotExist as e:
            print("Exception:", e)
            return Course.objects.none()

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filtered'] = True
        return context
    

