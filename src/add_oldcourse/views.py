from django.shortcuts import render
from .models import Course
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

class OldCourseCreateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    template_name = 'add_oldcourse/add_oldcourse.html'
    fields = ['course_title', 'year', 'semester']
    success_url = '/'
    success_message = "Course added successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_staff