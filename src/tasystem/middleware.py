from django.shortcuts import redirect
from django.urls import reverse
from system_active.models import SystemStatus
from system_active.views import system_closed_view
from django.contrib import messages

class SystemClosedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_staff:
            system_status = SystemStatus.objects.first()
            if request.path != reverse('logout'):
                if system_status and not system_status.system_active:
                    messages.error(request, "System is temporarily closed. Please try again later.")
                    while not (request.path == reverse('system_closed_view')):
                        return redirect('system_closed_view')
                
        response = self.get_response(request)
        return response
