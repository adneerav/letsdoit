from django.contrib import admin

from movies.models import Genre, Content, ContentImage

# Register your models here.

admin.site.register(Genre)


class AdminContent(admin.ModelAdmin):
    model = Content
    list_display = ['name', 'type']
    search_fields = ('name', 'type')


admin.site.register(Content, AdminContent)

'''
To display listing with model value column(s).
'''


class AdminContentImage(admin.ModelAdmin):
    model = ContentImage
    list_display = ['content_name', 'type']


admin.site.register(ContentImage, AdminContentImage)
