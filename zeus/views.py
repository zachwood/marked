from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from bookmarks.models import Bookmark, Favorite
from accounts.models import UserProfile
from django.contrib.auth.models import User

@login_required
def home(request):

    total_bookmarks = Bookmark.objects.count()
    total_users = UserProfile.objects.count()

    return render_to_response('zeus/home.html', locals(),
                context_instance=RequestContext(request) )


@login_required
def list_users(request):

    all_users = UserProfile.objects.all()

    return render_to_response('zeus/list_users.html', locals(),
                context_instance=RequestContext(request) )
