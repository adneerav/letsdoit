from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
THUMB = 'THUMB',
LARGE = 'LARGE',
BANNER = 'BANNER'
IMAGE_TYPE = (
    (THUMB, _('Thumb')),
    (LARGE, _('Large')),
    (BANNER, _('Banner')),
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

    def __str__(self):
        return self.name


class Content(models.Model):
    name = models.CharField(max_length=150)
    plot = models.CharField(max_length=500)
    type = models.CharField(choices=CONTENT_TYPE, verbose_name='content type', max_length=25)
    genres = models.ManyToManyField(Genre, related_name='contents', related_query_name='content')

    class Meta:
        verbose_name = _('content')
        verbose_name_plural = _('contents')


class ContentImage(models.Model):
    thumb = models.ImageField(upload_to='uploads/content/thumb/', db_column='thumb_image',
                              blank=True, null=True, verbose_name=_('thumb image'))
    type = models.CharField(verbose_name='image type', max_length=25, null=False, blank=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='images',
                                related_query_name='image')

    class Meta:
        verbose_name = _('contentimage')
        verbose_name_plural = _('contentimages')
