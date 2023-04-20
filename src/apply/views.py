from django.shortcuts import render, redirect, get_object_or_404
# from .forms import ApplicationForm
from .models import Apply
from add_course.models import Course
from offers.models import Offer
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import ModelForm
from django import forms

from django.core.mail import send_mail
from django.urls import reverse


class ApplyForm(ModelForm):
    class Meta:
        model = Apply
        fields = ['supplemental_answer_1',
                  'supplemental_answer_2', 'supplemental_answer_3', 'additional_information', ]
        labels = {
            "supplemental_answer_1": "Supplemental Question 1",
            "supplemental_answer_2": "Supplemental Question 2",
            "supplemental_answer_3": "Supplemental Question 3",
        }


class ApplyView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Apply
    template_name = 'apply/apply.html'
    form_class = ApplyForm
    success_url = '/'
    success_message = "Application submitted successfully"
    # context_object_name = 'course'

    def form_valid(self, form):
        if self.request.user.has_already_applied(self.kwargs['app_id']):
            form.add_error(None, "You have already applied for this course")
            return super().form_invalid(form)
        if not self.request.user.can_apply():
            form.add_error(
                None, "You have already reached the maximum number of applications (5)")
            return super().form_invalid(form)
        form.instance.author = self.request.user
        form.instance.course = get_object_or_404(
            Course, id=self.kwargs['app_id'])
        return super().form_valid(form)

    def test_func(self):
        return not self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Course.objects.get(id=self.kwargs['app_id'])
        context['course'] = course

        supplemental_answer_1_field = context['form'].fields.get(
            'supplemental_answer_1')
        if supplemental_answer_1_field and course.supplemental_question_1:
            supplemental_answer_1_field.label = course.supplemental_question_1
        elif supplemental_answer_1_field:
            supplemental_answer_1_field.widget = forms.HiddenInput()

        supplemental_answer_2_field = context['form'].fields.get(
            'supplemental_answer_2')
        if supplemental_answer_2_field and course.supplemental_question_2:
            supplemental_answer_2_field.label = course.supplemental_question_2
        elif supplemental_answer_2_field:
            supplemental_answer_2_field.widget = forms.HiddenInput()

        supplemental_answer_3_field = context['form'].fields.get(
            'supplemental_answer_3')
        if supplemental_answer_3_field and course.supplemental_question_3:
            supplemental_answer_3_field.label = course.supplemental_question_3
        elif supplemental_answer_3_field:
            supplemental_answer_3_field.widget = forms.HiddenInput()

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
            applications = Apply.objects.filter(
                course__author=self.request.user)
            print(applications)
            return applications

    # bug : create_offer can't be found issue
    # solution : move content to send_offer_email instead
    def create_offer():
        # create offer object
        # find the recipient using the application passed
        # from the professor html page
        # application_id = request.GET.get('app_id')

        # sender = request.user
        # application_id = app_id
        # print("application_id: ", application_id)
        # recipient_application = Apply.objects.get(id=application_id)
        # offer = Offer(sender=sender, recipient=recipient_application.author, course=recipient_application.course)
        # offer.save()
        pass

    def send_offer_email(request, **kwargs):
        # send_mail(
        #     'TA Offer Notice From {} {}'.format(request.user.first_name, request.user.last_name),
        #     'Here is the message.',
        #     'tasystem2023@gmail.com',
        #     ['kohke@bc.edu'],
        #     fail_silently=False,
        # )
        sender = request.user
        application_id = kwargs.get('app_id', 0)
        print("application_id: ", application_id)
        recipient_application = Apply.objects.get(id=application_id)
        offer = Offer(sender=sender, recipient=recipient_application.author,
                      course=recipient_application.course)
        offer.save()
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


class ApplicationDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Apply
    template_name = 'apply/application_confirm_delete.html'
    success_url = '/'
    success_message = "Application deleted successfully"

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
