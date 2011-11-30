from django.db import models
from accounts.models import UserProfile

class Bookmark(models.Model):
    url = models.URLField(verify_exists=False)
    added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=255, null=False, blank=True)

    def __unicode__(self):
        return u'%s' % self.url
