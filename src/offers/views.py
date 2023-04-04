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
    template_name = 'offer/offer_list.html'
    ordering = ['time_stamp']
    context_object_name = 'offer_list'
    
    