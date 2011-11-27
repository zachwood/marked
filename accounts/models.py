from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')

    def __unicode__(self):
        return u'%s' % self.user
