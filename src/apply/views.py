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
from django.contrib import messages


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
        user = self.request.user
        course_id = self.kwargs['app_id']
        course = get_object_or_404(Course, id=course_id)

        has_already_applied = user.has_already_applied(course_id)
        print(
            f"User {user} applying for course {course_id}: has_already_applied = {has_already_applied}")

        if has_already_applied:
            form.add_error(None, "You have already applied for this course")
            return super().form_invalid(form)

        if not user.can_apply():
            form.add_error(
                None, "You have already reached the maximum number of applications (5)")
            return super().form_invalid(form)

        form.instance.author = user
        form.instance.course = course
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
        sender = request.user
        application_id = kwargs.get('app_id', 0)
        recipient_application = Apply.objects.get(id=application_id)
        if recipient_application.course.current_tas.count() >= int(recipient_application.course.ta_required):
            messages.error(
                request, f"You have reached the maximum number of TAs for this course ({recipient_application.course.ta_required})")
            return redirect('professor_applications')
        elif Offer.objects.filter(recipient=recipient_application.author, course=recipient_application.course):
            messages.error(
                request, f"{recipient_application.author.first_name} {recipient_application.author.last_name} has already been offered for this course")
            return redirect('professor_applications')
        else:
            offer = Offer(sender=sender, recipient=recipient_application.author,
                          course=recipient_application.course)
            offer.save()
            messages.success(
                request, f"Offer sent to {recipient_application.author.first_name} {recipient_application.author.last_name} successfully. An email has been sent to the student.")
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


class ApplicationReviewView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Apply
    template_name = 'apply/application_review.html'
    success_url = '/'
    success_message = "Application accepted!"

    def test_func(self):
        application = self.get_object()
        return self.request.user == application.course.author or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        application = Apply.objects.get(id=self.kwargs['pk'])
        context['application'] = application
        context['student'] = application.author
        return context

    def get_success_url(self):
        return reverse('professor_applications')
