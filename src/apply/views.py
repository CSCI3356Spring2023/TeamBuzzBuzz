from django.shortcuts import render, redirect, get_object_or_404
# from .forms import ApplicationForm
from .models import Apply
from add_course.models import Course
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ApplyView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Apply
    template_name = 'apply/apply.html'
    fields = ['additional_information']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.course = get_object_or_404(Course, id=self.kwargs['app_id'])
        return super().form_valid(form)
    
    def test_func(self):
        return not self.request.user.is_staff
    
class ApplicationsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Apply
    template_name = 'apply/applications.html'
    context_object_name = 'applications'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            applications = Apply.objects.all()
            print(applications)
            return applications
        else:
            applications = Apply.objects.filter(course__author=self.request.user)
            print(applications)
            return applications

    



# add decorator to make this only accessible to students and admin
# def apply_view(request, app_id):
#     course_data = Course.objects.get(id=app_id)
    
#     print(course_data)
#     form = ApplicationForm()
#     if request.method == "POST":
#         form = ApplicationForm(request.POST or None)
#         print("Posting Data")
#         if form.is_valid():
#             print("cleaned data: ", form.cleaned_data)
#             application = form.save()
#             application.course_title = course_data.course_title
#             application.discussion = course_data.discussion
#             application.description = course_data.description
#             application.email = course_data.email
#             application.ta_required = course_data.ta_required
#             form.save()
#         else:
#             print(form.errors)
        
#         form = ApplicationForm()
#     context = {
#         'course' : course_data,
#         'form' : form
#     }
        
#     return render(request, 'apply/apply.html', context)

