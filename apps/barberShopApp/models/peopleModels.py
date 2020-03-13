from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class Barber(models.Model):
    MORNING = 'MR'
    AFTERNOON = 'AT'
    WHOLE_DAY = 'WD'
    TURNS = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (WHOLE_DAY, 'Whole day')
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    turn = models.CharField(max_length=2, choices=TURNS, default='MR')
    phone = models.CharField(max_length=9)
    barberShop = models.ForeignKey('Barberia', on_delete=models.SET_NULL, null=True, related_name='barbers')

    def __str__(self):
        return self.first_name + " " + self.last_name


class ClientManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Els usuaris necessiten tenir una adreça d'email")
        if not username:
            raise ValueError("Els usuaris necessiten especificar el nom d'usuari")
        # if not fisrt_name:
        #     raise ValueError("Els usuaris necessiten especificar el sue nom")
        # if not last_name:
        #     raise ValueError("Els usuaris necessiten especificar el seu cognom")

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
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser):

    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    last_login = models.DateTimeField('last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField('Nom', max_length=30)
    last_name = models.CharField('Cognoms', max_length=40)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    object = ClientManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
