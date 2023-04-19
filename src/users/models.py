from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.apps import apps


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, first_name, last_name, gpa, year, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, gpa=gpa, year=year, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, gpa, year, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, gpa, year, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    year = models.PositiveIntegerField(default=2023)

    # user_id = models.CharField(max_length=50, unique=True)

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="custom_user_set",
        related_query_name="custom_user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="custom_user_set",
        related_query_name="custom_user",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gpa', 'year', 'is_staff']

    def can_apply(self):
        if not self.is_staff:
            Apply = apps.get_model('apply', 'Apply')
            applications = Apply.objects.filter(author=self).count()
            if applications < 5:
                return True
        return False

    def has_already_applied(self, course_id):
        if not self.is_staff:
            Apply = apps.get_model('apply', 'Apply')
            applications = Apply.objects.filter(
                author=self, course=course_id).count()
            if applications > 0:
                return True
        return False
