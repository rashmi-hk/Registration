
import uuid

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager



class Tracker(models.Model):
    # Set PK for all models
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # tracker columns
    create_datetime = models.DateTimeField(default=now, null=False, blank=False)
    create_user = models.CharField(max_length=50)
    create_program = models.CharField(max_length=200)
    modify_datetime = models.DateTimeField(default=now, null=False, blank=False)
    modify_user = models.CharField(max_length=50)
    modify_program = models.CharField(max_length=200)

    class Meta:
        abstract = True


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email Address'))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=150, null=False, unique=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    middle_initial = models.CharField(max_length=150, null=True)
    company_name = models.CharField(max_length=200, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    image_url = models.CharField(max_length=2000, null=True)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'custom_user'


class UserInfo(Tracker):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2000, null=True)
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "%s | %s" % (self.user_id, self.image_url)

    class Meta:
        managed = True
        db_table = 'user_info'