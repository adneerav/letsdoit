from django.contrib import admin

from movies.models import Genre, Content, ContentImage

# Register your models here.
admin.site.register(Genre)
admin.site.register(Content)
admin.site.register(ContentImage)