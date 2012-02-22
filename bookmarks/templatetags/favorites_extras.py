from django import template

from bookmarks.models import Bookmark, Favorite
from accounts.models import UserProfile

register = template.Library()

@register.filter
def not_favorited_by(mark_id, user_id):

    user_profile = UserProfile.objects.get(pk = user_id)

    favorite = Favorite.objects.filter(bookmark__id = mark_id, userprofile__user__id = user_id )

    if favorite:
        return False
    else:
        return True


@register.filter
def ellipses(value):
    if(len(value) == 30):
        return "%s..." % value
    else:
        return value

@register.filter
def domain_only(value):
    from urlparse import urlparse
    value = urlparse(value)

    return value.netloc

@register.filter
def domain_link(value):
    from urlparse import urlsplit
    value = urlsplit(value)

    return "%s://%s" % (value.scheme, value.netloc)
