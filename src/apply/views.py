from django.shortcuts import render, redirect, get_object_or_404
# from .forms import ApplicationForm
from .models import Apply
from add_course.models import Course
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.core.mail import send_mail 
from django.urls import reverse

class ApplyView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Apply
    template_name = 'apply/apply.html'
    fields = ['additional_information']
    success_url = '/'
    # context_object_name = 'course'

    def form_valid(self, form):
        if self.request.user.has_already_applied(self.kwargs['app_id']):
            form.add_error(None, "You have already applied for this course")
            return self.form_invalid(form)
        if not self.request.user.can_apply():
            form.add_error(None, "You have already reached the maximum number of applications (5)")
            return self.form_invalid(form)
        form.instance.author = self.request.user
        form.instance.course = get_object_or_404(Course, id=self.kwargs['app_id'])
        return super().form_valid(form)
    
    def test_func(self):
        return not self.request.user.is_staff

    def get_context_data(self):
        context = super().get_context_data()
        context['course'] = Course.objects.get(id=self.kwargs['app_id'])
        return context
    
    
class ApplicationsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Apply
    template_name = 'apply/professor_applications.html'
    context_object_name = 'applications'
    
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            applications = Apply.objects.all()
            print(applications)
            return applications
        else:
            applications = Apply.objects.filter(course__author=self.request.user)
            print(applications)
            return applications

    def send_offer_email(request):
    # form.instance.author = self.request.user
    # form.instance.course = get_object_or_404(Course, id=self.kwargs['app_id'])
    # send_mail(
    #     'TA Offer for {}'.format(form.instance.course.course_title),
    #     'Here is the message.',
    #     'kykoh906@gmail.com',
    #     ['kohke@bc.edu'],
    #     fail_silently=False,
    # )

        send_mail(
            'TA Offer Notice',
            'Here is the message.',
            'tasystem2023@gmail.com',
            ['kohke@bc.edu'],
            fail_silently=False,
        )
        return redirect('professor_applications')
        

class StudentApplicationsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Apply
    template_name = 'apply/student_applications.html'
    context_object_name = 'applications'
    
    def test_func(self):
        return not self.request.user.is_staff or self.request.user.is_superuser
    
    def get_queryset(self):
        applications = Apply.objects.filter(author=self.request.user)
        print(applications)
        return applications

    
class ApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Apply
    template_name = 'apply/application_confirm_delete.html'
    success_url = '/'
    
    def test_func(self):
        application = self.get_object()
        return self.request.user == application.author or self.request.user.is_superuser



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

