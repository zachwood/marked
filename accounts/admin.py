from django.contrib import admin
from accounts.models import UserProfile

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserAdmin)
