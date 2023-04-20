from django.shortcuts import render
# from .forms import AddCourseForm
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
from django.forms import inlineformset_factory


class CourseCreateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    template_name = 'add_course/add_course.html'
    fields = ['course_title', 'discussion', 'ta_required', 'description',
              'supplemental_question_1', 'supplemental_question_2', 'supplemental_question_3']
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


# def add_course_view(request, *args, **kwargs):
#     my_form = AddCourseForm()
#     if request.method == "POST":
#         my_form = AddCourseForm(request.POST or None)
#         print("Posting Data")
#         if my_form.is_valid():
#             print("cleaned data: ", my_form.cleaned_data)
#             my_form.save()
#         else:
#             print(my_form.errors)

#         my_form = AddCourseForm()

#     context = {
# 		"form" : my_form
# 	}
#     return render(request, 'add_course/add_course.html', context)

# def course_confirmation(request, *args, **kwargs):
