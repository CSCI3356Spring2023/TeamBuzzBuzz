from django.shortcuts import render, redirect, get_object_or_404
from add_course.models import Course
from users.models import CustomUser
from student_oldcourse.models import OldCourse
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course_list/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(pk=self.kwargs['pk'])
        return context


class SuggestedCoursesView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'suggested_old_course/suggested_old_course.html'
    ordering = ['course_title']
    context_object_name = 'course_data'

    def get_queryset(self, *args, **kwargs):
        key = self.kwargs['pk']
        print("Key:", key)
        try:
            user = CustomUser.objects.get(pk=key)
            print("User:", user)
            # .values('course_title', 'author')
            oldcourses = OldCourse.objects.filter(taker=user)
            profs = []
            titles = []
            for x in oldcourses:
                if x.author not in profs:
                    profs.append(x.author)
                if x.course_title not in titles:
                    titles.append(x.course_title)
            print(profs)
            print(titles)
            courses = Course.objects.filter(
                author__in=profs, course_title__in=titles)
            print("Courses:", courses)
            return courses
        except ObjectDoesNotExist as e:
            print("Exception:", e)
            return Course.objects.none()


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'course_list/course_list.html'
    ordering = ['course_title']
    context_object_name = 'course_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for course in context['course_data']:
            course.ta_required = int(course.ta_required)
        return context


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

    def change_course_status(request, **kwargs):
        key = kwargs.get('pk')
        user = CustomUser.objects.get(pk=key)
        course = Course.objects.filter(author=user)

        # close the course and change status to false
        course.status = not course.status
        if course.status == False:
            messages.warning(
                request, f'Course has been closed {course.course_title}')
        else:
            messages.success(
                request, f'Course has been opened {course.course_title}')

        course.save()

        return redirect('professor_courses', pk=key)

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
