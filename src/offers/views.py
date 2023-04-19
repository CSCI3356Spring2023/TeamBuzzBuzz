from django.shortcuts import render, redirect, get_object_or_404
from add_course.models import Course
from users.models import CustomUser
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from .models import Offer


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
    
    #offer doesn't save the is_accpeted state
    def acceptOffer(request, *args, **kwargs):
        key = kwargs.get('pk')
        user = CustomUser.objects.get(pk=key)
        offer = Offer.objects.get(recipient=request.user)
        offer.is_rejected = False
        offer.save()
        return redirect('student_offers')
        
    def rejectOffer(request,**kwargs):
        offer = Offer.objects.get(recipient=request.user)
        offer.is_rejected = True
        offer.save()
        return redirect('student_offers')
        
