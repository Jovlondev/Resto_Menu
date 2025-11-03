from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("Foydalanuvchining telefoni kiritilishi shart.")
        user = self.model(
            phone=phone,
            **extra_fields
        )
        user.set_password(str(password))
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuserda is_superuser=True bo‘lishi kerak.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuserda is_staff=True bo‘lishi kerak.')

        return self.create_user(phone=phone, password=password, **extra_fields)


class User(AbstractUser):
    # yangilar
    phone = models.CharField(max_length=15, unique=True)
    fio = models.CharField(max_length=56, verbose_name="F.I.O")
    yosh = models.IntegerField(default=0)

    # abizatelna
    is_staff = models.BooleanField(default=False)  # xodim
    is_superuser = models.BooleanField(default=False)  # admin
    is_active = models.BooleanField(default=True)  # ban, deleted account

    # keraksizlar
    username = None
    email = None
    first_name = None
    last_name = None

    # qo'shimcha
    objects = CustomUserManager()  # ✅ siz yozgan managerdan foydalanamiz!

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['yosh']
