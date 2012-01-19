from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')

    def three_recent_set(self):
        return self.bookmark_set.order_by('-added')[:3]
    def __unicode__(self):
        return u'%s' % self.user

    def get_absolute_url(self):
        return "/profile/%s/" % self.user.username
