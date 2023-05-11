from django.shortcuts import render, redirect, get_object_or_404
# from .forms import AddCourseForm
from .models import Course, Discussion
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django import forms


class CourseCreateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    template_name = 'add_course/add_course.html'
    fields = ['course_title', 'course_number', 'course_section', 'course_day', 'course_time', 'discussion', 'office_hours', 'ta_required', 'homework_graded_in_meetings', 'description',
              'supplemental_question_1', 'supplemental_question_2', 'supplemental_question_3', 'additional_info']
    success_url = '/'
    success_message = "Course added successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class CourseUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    template_name = 'add_course/edit_course.html'
    fields = ['course_title', 'course_number', 'course_section', 'course_day', 'course_time', 'discussion', 'office_hours', 'ta_required', 'homework_graded_in_meetings', 'description',
              'supplemental_question_1', 'supplemental_question_2', 'supplemental_question_3', 'additional_info']
    success_url = '/'
    success_message = "Course updated successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self, *args, **kwargs):
        return self.request.user.is_superuser or self.request.user == self.get_object().author


class DiscussionCreateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Discussion
    template_name = 'add_course/add_discussion.html'
    fields = ['number', 'day', 'time', 'ta']
    success_url = '/'
    success_message = "Discussion added successfully"

    def form_valid(self, form):
        course_id = self.kwargs['pk']
        course = get_object_or_404(Course, id=course_id)
        form.instance.course = course
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        course_id = self.kwargs['pk']
        course = get_object_or_404(Course, id=course_id)
        form.fields['ta'] = forms.ModelChoiceField(
            queryset=course.current_tas.all(), required=False)
        return form

    def test_func(self, *args, **kwargs):
        course = Course.objects.get(id=self.kwargs['pk'])
        return self.request.user.is_superuser or self.request.user == course.author


class DiscussionListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Discussion
    template_name = 'add_course/discussion_list.html'
    context_object_name = 'discussions'
    ordering = ['number']

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs['pk'])
        return Discussion.objects.filter(course=course)

    def test_func(self, *args, **kwargs):
        course = Course.objects.get(id=self.kwargs['pk'])
        return self.request.user.is_superuser or self.request.user == course.author

    def get_context_data(self, **kwargs):
        context = super(DiscussionListView, self).get_context_data(**kwargs)
        context['course'] = get_object_or_404(Course, id=self.kwargs['pk'])
        return context


class DiscussionUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Discussion
    template_name = 'add_course/edit_discussion.html'
    fields = ['number', 'day', 'time', 'ta']
    success_url = '/'
    success_message = "Discussion updated successfully"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        discussion_id = self.kwargs['pk']
        discussion = get_object_or_404(Discussion, id=discussion_id)
        course = discussion.course
        form.fields['ta'] = forms.ModelChoiceField(
            queryset=course.current_tas.all(), required=False)
        return form

    def form_valid(self, form):
        discussion_id = self.kwargs['pk']
        discussion = get_object_or_404(Discussion, id=discussion_id)
        course = discussion.course
        form.instance.course = course
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self, *args, **kwargs):
        discussion = Discussion.objects.get(id=self.kwargs['pk'])
        return self.request.user.is_superuser or self.request.user == discussion.course.author
