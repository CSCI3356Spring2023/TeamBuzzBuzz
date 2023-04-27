from django.shortcuts import render, redirect, get_object_or_404
from add_course.models import Course
from users.models import CustomUser
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course_list/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(pk=self.kwargs['pk'])
        return context


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'course_list/course_list.html'
    ordering = ['course_title']
    context_object_name = 'course_data'


class ProfessorCoursesView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'course_list/course_list.html'
    ordering = ['course_title']
    context_object_name = 'course_data'

    def get_queryset(self, *args, **kwargs):
        key = self.kwargs['pk']
        print("Key:", key)
        try:
            user = CustomUser.objects.get(pk=key)
            print("User:", user)
            courses = Course.objects.filter(author=user)
            print("Courses:", courses)
            return courses
        except ObjectDoesNotExist as e:
            print("Exception:", e)
            return Course.objects.none()

    # def get_queryset(self, *args, **kwargs):
    #     first, last = self.kwargs['name'].split("_")
    #     print("Name:", self.kwargs['name'], "First:", first, "Last:", last)
    #     try:
    #         user = CustomUser.objects.get(first_name__iexact=first, last_name__iexact=last)
    #         print("User:", user)
    #         courses = Course.objects.filter(author=user)
    #         print("Courses:", courses)
    #         return courses
    #     except ObjectDoesNotExist as e:
    #         print("Exception:", e)
    #         return Course.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtered'] = True
        return context


# @login_required
# def course_list_view(request):
#     course_data = Course.objects.all()

#     context = {
#         'course_data' : course_data,
#         'all_courses' : True
#     }

#     return render(request, 'course_list/course_list.html', context)
