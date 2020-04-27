from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _

GENDER = (
    ('Male', _('male')),
    ('Female', _('female')),
    ('Other', _('other'))
)


class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True,
                                  null=True, verbose_name=_('first name'))
    last_name = models.CharField(max_length=50, blank=True,
                                 null=True, verbose_name=_('last name'))
    country_code = models.CharField(max_length=5, default=91,
                                    verbose_name=_('country code'))
    email = models.CharField(max_length=500, verbose_name=_('email'))
    mobile = models.CharField(max_length=20, verbose_name=_('mobile'))
    password = models.CharField(max_length=500, verbose_name=_('password'))
    photo = models.ImageField(upload_to='uploads/users/', db_column='user_photo',
                              blank=True, default=None, verbose_name=_('profile photo'))
    gender = models.CharField(verbose_name=_('gender'), max_length=12,
                              choices=GENDER, blank=True, null=True)
    birth_date = models.DateField(verbose_name=_('birth date'),
                                  blank=True, null=True)
    is_verified = models.BooleanField(verbose_name=_('is verified'), default=False)
    address_1 = models.CharField(max_length=250, blank=True, null=True)
    address_2 = models.CharField(max_length=250, blank=True, null=True)
