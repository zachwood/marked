from django.contrib import admin
from bookmarks.models import Bookmark, Favorite

class BookmarkAdmin(admin.ModelAdmin):
    pass

class FavoriteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Favorite, FavoriteAdmin)
