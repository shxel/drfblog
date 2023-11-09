from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, name, body, image, password=None,
                    is_admin=False, is_staff=False, is_active=True,
                    is_superuser=True):
                    
        if not email:
            raise ValueError('Users must have an email address')
        else:
            email=self.normalize_email(email),

            user=self.model(email=email, name=name, body=body,
                            image=image, username=username)
            
            user.set_password(password)
            user.save(using=self._db)

            return user

    def create_superuser(self, email, body,
                        image, name, username,
                        password=None):
        
        user = self.create_user(name=name, email=email, body=body,
                                image=image, username=username,
                                password=password)
        
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='user_images', null=True,
                            blank=True)
    follower = models.ManyToManyField("self", related_name='follow',
                                        null=True, blank=True,
                                        symmetrical=False)
    notifications = models.ManyToManyField("self",related_name='user_notification',
                                        symmetrical=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateField(null=True, blank=True)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['image', 'body', 'name', 'email']

    def __str__(self):
        return self.name
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

