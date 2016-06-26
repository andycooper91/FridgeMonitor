from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Kind, Event, User
from django.template import loader
from django.utils import timezone


def index(request):
    latest_event_list = Event.objects.order_by('-event_date')[:25]
        
    template = loader.get_template('Monitor/index.html')
    context = {
        'latest_event_list' : latest_event_list,
    }
    return HttpResponse(template.render(context,request))
    
def update(request, user_id, kind_id):
    k = get_object_or_404(Kind, pk = kind_id)
    u = get_object_or_404(User, pk = user_id)
    e = Event(user = u, kind = k, event_date = timezone.now())
    e.save()
    return HttpResponseRedirect('/monitor')