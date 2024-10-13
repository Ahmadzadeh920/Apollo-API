from django.db import models
from django.contrib.auth.models import AbstractUser

#from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password and extra data.
        """
        if not email:
            raise ValueError(_("the Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    email = models.EmailField(_("email address"), unique=True)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email



# class profile
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,related_name="User", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    linkedin_url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user.email} Profile"
    
    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


