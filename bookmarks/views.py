from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, loader

from bookmarks.models import Bookmark
from accounts.models import UserProfile

@login_required(login_url='/accounts/login/')
def home(request):
    
    if request.method == 'POST':
        if request.POST['link']:
            link = request.POST['link']
            check_save_url(request, link)

    marks = Bookmark.objects.filter(owner=request.user).order_by('-added')

    return render_to_response('home.html', { 'marks': marks, 'local_bookmarklet': False },
            context_instance=RequestContext(request) )


@login_required
def bookmarklet_save(request):
    if request.method == 'GET':
        print request.GET['link']
        if request.GET['link']:
            link = request.GET['link']
            check_save_url(request, link)

    # redirect URL goes here...
    # for now, it's just the same as the home....
    return redirect(home)


# UTILS: view related utils below

def check_save_url(request, link):

    user_profile = UserProfile.objects.get(user = request.user)
    check = Bookmark.objects.filter(url = link, owner = user_profile)
    print link

    if not check:
        m = Bookmark(url = link, owner = user_profile)
        m.save()
        messages.add_message(request, messages.INFO, 'Consider that marked')
    else:
        messages.add_message(request, messages.INFO, 'You have already added this mark')
