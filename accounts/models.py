from django.db import models
from django.contrib.auth.models import User

import time

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')

    def _get_last_added(self):
        return "%i" % self.bookmark_set.filter(public=True).order_by('-added')

    last_added = property(_get_last_added)

    def _get_last_added_unix(self):
        print self.bookmark_set.count()
        if self.bookmark_set.count() > 0:
            mark = self.bookmark_set.all().filter(public=True).order_by('-added')[0]
            epoch = int(time.mktime(mark.added.timetuple())*1000)
        else:
            epoch = 1
        return "%i" % epoch

    last_added_unix = property(_get_last_added_unix)

    def three_recent_set(self):
        return self.bookmark_set.order_by('-added')[:3]

    def _get_total_marks(self):
        return int(self.bookmark_set.count())

    total_marks = property(_get_total_marks)

    def __unicode__(self):
        return u'%s' % self.user

    def get_absolute_url(self):
        return "/profile/%s/" % self.user.username

