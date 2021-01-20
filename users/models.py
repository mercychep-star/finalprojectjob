from PIL import Image
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from jobs.models import Job


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('enter the correct email')
        #email = self.normalize_email(email)
       # user = self.model(email=email, **extra_fields)
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_superuser',False)
        user = self._create_user(email,password,**extra_fields)
       # return self._create_user(email,password,**extra_fields)
        return user


    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser mus have is_superuser=True')
        #return self._create_user(email,password,**extra_fields)
        user = self._create_user(email, password, **extra_fields)
        return user





class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=200, blank=False)
    last_name = models.CharField(_('last name'), max_length=200, blank=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('ALL USERS')

    def get_profile_id(self):
        return self.profiles.id

    def count_unread_messages(self):
        return self.invites.filter(unread=True).count()

    def unread_messages(self):
        return self.invites.filter(unread=True).values_list('job_id',flat=True)


class Profile(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE,related_name="profiles")
    image = models.ImageField(upload_to="media/users",default="media/users/about.jpg")
    birth_day = models.DateField(default=None,blank=True,null=True)
    location = models.CharField(max_length=20,blank=True)
    resume = RichTextField(blank=True)
    company = models.CharField(max_length=200,blank=True)
    wish_list = models.ManyToManyField(Job,default=None,blank=True,related_name="wish_list")

    def __str__(self):
        return self.user.first_name + " "+ self.user.last_name+ " "+ self.user.email

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)
        img = Image.open(self.image)
        if img.height > 200 or img.width > 200:
            new_size =(200,200)
            img.thumbnail(new_size)
            img.save(self.image.path)

    class Meta:
        verbose_name_plural= "Users' Profiles"


@receiver(models.signals.post_save,sender= Account)
def post_save_user_signal(sender,instance,created,**kwargs):
    if created:
        instance.save
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=Account)

class Invite(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE, related_name="invites")
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name="invites")
    date = models.DateField(default=None,blank=True,null=True)
    message = RichTextField(blank=True)
    unread = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Invites"

    def __str__(self):
        return self.job.title








