from django.shortcuts import render, redirect, get_object_or_404
from add_course.models import Course
from users.models import CustomUser
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from .models import Offer
from django.contrib import messages
from apply.models import Apply

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
class OfferListView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = 'offer/professor_offer.html'
    ordering = ['time_stamp']
    context_object_name = 'offer_list'

    def test_func(self):
        return self.request.user.is_superuser


class OfferListProfessorView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = 'offer/professor_offer.html'
    ordering = ['time_stamp']
    context_object_name = 'offer_list'

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    # returns the things passed down in the context named 'offer_list'
    def get_queryset(self, *args, **kwargs):
        key = self.kwargs['pk']
        user = CustomUser.objects.get(pk=key)
        offer_list = Offer.objects.filter(sender=user)
        print(offer_list)
        return offer_list


class OfferListStudentView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = 'offer/student_offer.html'
    ordering = ['time_stamp']
    context_object_name = 'offer_list'

    def test_func(self):
        return not self.request.user.is_staff or self.request.user.is_superuser

    def get_queryset(self, *args, **kwargs):
        key = self.kwargs['pk']
        user = CustomUser.objects.get(pk=key)
        offer_list = Offer.objects.filter(recipient=user)
        print("offer: ", offer_list)

        return offer_list

    # offer doesn't save the is_accpeted state
    def acceptOffer(request, **kwargs):
        key = kwargs.get('pk')
        offer = Offer.objects.get(id=key)

        if offer.course.at_capacity():
            messages.error(
                request, f"Course is already at capacity ({offer.course.ta_required})")
        elif request.user.course_working_for:
            messages.error(
                request, f"You are already working for a course ({request.user.course_working_for})")
        else:
            offer.status = True
            offer.course.current_tas.add(offer.recipient)
            offer.course.num_positions_filled +=1
            offer.course.save()
            offer.save()
            request.user.course_working_for = offer.course
            request.user.save()
            messages.success(request, "Offer accepted")

            # check if course is now full and send email to all remainging applicants
            if offer.course.at_capacity():
                recipients = [recipient_application.author for recipient_application in Apply.objects.filter(
                        course=offer.course)]
                recipients = [r for r in recipients if r not in offer.course.current_tas.all()]
                send_mail(
                    f'{offer.course.course_title} is now full',
                    f'Unfortunately, {offer.course.course_title} is now full. We appreciate your interest in the course and hope you apply again next semester.',
                    settings.EMAIL_HOST_USER,
                    recipients,
                    fail_silently=False,
                )

        return redirect('student_offers', pk=request.user.id)

    def rejectOffer(request, **kwargs):
        key = kwargs.get('pk')
        offer = Offer.objects.get(id=key)
        offer.status = False
        offer.save()
        messages.success(request, "Offer rejected")
        return redirect('student_offers', pk=request.user.id)


# messages.success(request, "Offer accepted")
# messages.warning(request, "Course at capacity")
# messages.error(request, "Offer rejected")
# messages.info(request, "Offer sent")
# messages.debug(request, "Offer deleted")
