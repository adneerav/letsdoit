from django.utils.timezone import now

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
THUMB = 'THUMB',
LARGE = 'LARGE',
BANNER = 'BANNER'
IMAGE_TYPE = (
    ('THUMB', _('Thumb')),
    ('LARGE', _('Large')),
    ('BANNER', _('Banner')),
)

MOVIE = 'Movie',
WEB_SERIES = 'WebSeries',
DAILY_SHOP = 'DailyShop',

CONTENT_TYPE = (
    ('Movie', _('Movie')),
    ('WebSeries', _('WebSeries')),
    ('DailyShop', _('DailyShop'))
)


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('genre'))
    added_date = models.DateTimeField(auto_now_add=True, editable=False)

    '''
    To display data in admin panel listing with name.
    Not like Object(1),Object(2).
    '''

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_name(self):
        return self.name


class Content(models.Model):
    name = models.CharField(max_length=150)
    plot = models.CharField(max_length=500)
    date_of_release = models.DateTimeField(blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True, editable=False)
    type = models.CharField(choices=CONTENT_TYPE, verbose_name='content type', max_length=25)
    genres = models.ManyToManyField(Genre, related_name='contents', related_query_name='content')

    def __str__(self):
        return self.name



class ContentImage(models.Model):
    thumb = models.ImageField(upload_to='uploads/content/thumb/', db_column='thumb_image',
                              blank=True, null=True, verbose_name=_('thumb image'))
    type = models.CharField(choices=IMAGE_TYPE, verbose_name='image type', max_length=25, null=False, blank=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='images',
                                related_query_name='image')
    added_date = models.DateTimeField(auto_now_add=True, editable=False)

    @property
    def content_name(self):
        return self.content.name

    @property
    def image_url(self):
        return self.image_url

    @property
    def image_type(self):
        return self.type
