from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, first_name, last_name, phone_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    def __str__(self):
        return self.email

from django.db import models
from django.conf import settings

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.category.name}'

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Set default value here

    def __str__(self):
        return f"{self.quantity} of {self.category.name}"







class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.conf import settings
from django.db import models


class Address(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)


