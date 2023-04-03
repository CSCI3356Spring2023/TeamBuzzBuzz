from django.shortcuts import render, redirect, get_object_or_404
from add_course.models import Course
from users.models import CustomUser as User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


@login_required
def course_list_view(request):
    course_data = Course.objects.all()

    context = {
        'course_data' : course_data,
        'all_courses' : True
    }

    return render(request, 'course_list/course_list.html', context)

@login_required
def professor_courses_view(request, professor_id):
    professor = get_object_or_404(User, email=professor.email)
    course_data = Course.objects.filter(author=professor)
    context = {
        'course_data' : course_data,
        'professor' : professor
    }
    return render(request, 'course_list/course_list.html', context)
