from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from bookmarks.models import Bookmark
from accounts.models import UserProfile

@login_required(login_url='/accounts/login/')
def home(request):
    
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user = request.user)

        check = Bookmark.objects.filter(url = request.POST['link'])
        print check

        if not check:
            m = Bookmark(url = request.POST['link'], owner = user_profile)
            m.save()
            messages.add_message(request, messages.INFO, 'Consider that marked')
        else:
            messages.add_message(request, messages.INFO, 'You have already added this mark')

    marks = Bookmark.objects.filter(owner=request.user).order_by('-added')

    return render_to_response('home.html', { 'marks': marks },
            context_instance=RequestContext(request) )
