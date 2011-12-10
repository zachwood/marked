from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext, loader

from bookmarks.models import Bookmark
from accounts.models import UserProfile
from django.contrib.auth.models import User

import urllib2
import BeautifulSoup

@login_required
def home(request):
    
    if request.method == 'POST':
        if request.POST['link']:
            link = request.POST['link']
            check_save_url(request, link)

    #marks = Bookmark.objects.filter(owner=request.user).order_by('-added')

    #return render_to_response('home.html', { 'marks': marks, 
            #'local_bookmarklet': False },
            #context_instance=RequestContext(request) )


    user_profile = UserProfile.objects.get(user = request.user)
    return redirect(user_profile)

@login_required
def user_page(request, show_user):
    check_user = get_object_or_404(User, username=show_user)

    if request.user.username == show_user:
        page_owner = True
        marks = Bookmark.objects.filter(owner=request.user).order_by('-added')
    else:
        page_owner = False
        marks = Bookmark.objects.filter(owner__user__username=show_user).filter(public=True).order_by('-added')


    return render_to_response('home.html', { 'marks': marks, 
            'local_bookmarklet': False, 'show_user': show_user, 'page_owner': page_owner },
            context_instance=RequestContext(request) )


@login_required
def public_marks(request, show_user):
    check_user = get_object_or_404(User, username=show_user)

    marks = Bookmark.objects.filter(owner=request.user).filter(public=True).order_by('-added')

    return render_to_response('home.html', { 'marks': marks, 
            'local_bookmarklet': False, 'show_user': show_user },
            context_instance=RequestContext(request) )

@login_required
@csrf_exempt
def bookmarklet_save(request):
    # where the bookmarklet first lands them
    if request.method == 'GET':
        if request.GET['link']:
            link = request.GET['link']

            # check user and save url
            user_profile = get_object_or_404(UserProfile, user = request.user)
            check = Bookmark.objects.filter(url = link, owner = user_profile)

            old_bookmarklet = False

            if not check:
                # if they have the old bookmarklet, load the title the old way
                if 'title' in request.GET:
                    title = request.GET['title']
                else:
                    soup = BeautifulSoup.BeautifulSoup(urllib2.urlopen(link))
                    title = soup.title.string
                    old_bookmarklet = True

            else:
                messages.add_message(request, messages.INFO, 'You have already added this mark')
                return redirect(home)

            if old_bookmarklet:
                messages.add_message(request, messages.INFO, "You're using an old version of our Bookmarklet. "
                        + "Just drag the new version on this site to your bookmarks bar and you're good to go!")
    
    # post vars, AKA time to save the bookmark
    @csrf_protect
    elif request.method == 'POST':
        link = request.POST['link']
        title = request.POST['title']
        privacy = request.POST['privacy']

        if privacy == 'private':
            public = False
        elif privacy == 'public':
            public = True

        user_profile = get_object_or_404(UserProfile, user = request.user)

        m = Bookmark(url = link, owner = user_profile, title = title, public = public)
        m.save()
        messages.add_message(request, messages.INFO, 'Consider that marked')

        return redirect(home)

    # they got here somehow without post or get vars
    @csrf_protect
    else:
        return redirect(home)

    return render_to_response('bookmarks/save.html', { 'title': title, 'link': link }, 
            context_instance=RequestContext(request) )


# UTILS: view related utils below

def check_save_url(request, link):
    pass

