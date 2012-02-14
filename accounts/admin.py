from django.contrib import admin
from accounts.models import UserProfile

class UserAdmin(admin.ModelAdmin):
    fields = ('user',)
    list_display = ('user', 'total_marks',)

admin.site.register(UserProfile, UserAdmin)
