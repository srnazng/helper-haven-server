from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token

class Event(models.Model):
	event_name = models.CharField(max_length=255, unique=True)
	contact_name = models.CharField(max_length=30, blank=True)
	contact_email = models.EmailField(max_length=60, blank=True)
	contact_number = models.CharField(max_length=30, blank=True)
	event_summary = models.CharField(max_length=1000)
	role_description = models.CharField(max_length=1000)
	max_hours = models.PositiveIntegerField(default=24, blank=True, null=True)
	date = models.CharField(max_length=255, blank=True)
	time = models.CharField(max_length=255, blank=True)
	location = models.CharField(max_length=255, blank=True)
	link = models.URLField(max_length=200, blank=True)
	active = models.BooleanField(default=True)
	upcoming = models.BooleanField(default=True)

	def __str__(self):
		return self.event_name

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    role = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
	    return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
	    return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
	    return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Log(models.Model):
	user_email = models.CharField(max_length=255)
	event_name = models.CharField(max_length=255)
	role = models.CharField(max_length=1000, blank=True)
	hours = models.PositiveIntegerField(default=0)
	comments = models.CharField(max_length=100, blank=True)

class Volunteer(models.Model):
	email = models.CharField(max_length=255, default="", blank=True)
	first_name = models.CharField(max_length=255, default="", blank=True)
	last_name = models.CharField(max_length=255, default="", blank=True)
	gender = models.CharField(max_length=10, default="", blank=True)
	dob = models.DateField(null=True , blank=True)
	address = models.CharField(max_length=255, default="", blank=True)
	city = models.CharField(max_length=255, default="", blank=True)
	state = models.CharField(max_length=255, default="", blank=True)
	zip = models.CharField(max_length=255, default="", blank=True)
	skills = models.CharField(max_length=1000, default="", blank=True)
	link = models.URLField(max_length=255, default="", blank=True)