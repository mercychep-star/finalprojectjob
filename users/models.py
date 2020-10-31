from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    pass


class Account(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True)
    first_name = models.CharField(_('first name'),max_length=200,blank=False)
    last_name = models.CharField(_('last name'),max_length=200,blank=False)
    date_joined = models.DateTimeField(_('date joined'),auto_now_add=True)
    is_active = models.BooleanField(_('active'),default=True)
    is_staff =models.BooleanField(_('is_staff'),default=False)
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')