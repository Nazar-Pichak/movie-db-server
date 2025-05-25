from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Person(models.Model):
    ROLE_CHOICES = [
        ('director', 'Director'),
        ('actor', 'Actor'),
    ]

    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)
    biography = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
class Movie(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    year = models.IntegerField(db_index=True)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directed_movies')
    actors = models.ManyToManyField(Person, related_name='acted_movies')
    is_available = models.BooleanField(default=True)
    genres = models.JSONField()
    date_added = models.DateTimeField(auto_now_add=True)
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("E-mail is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    