from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
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
    def create_user(self, email, username, first_name = None, last_name = None, password=None):
        if not email:
            raise ValueError("Els usuaris necessiten tenir una adreça d'email")
        if not username:
            raise ValueError("Els usuaris necessiten especificar el nom d'usuari")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser):

    email = models.EmailField(max_length=60, unique=True, help_text=None)
    username = models.CharField('Nom d\'usuari',max_length=30, unique=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    last_login = models.DateTimeField('last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    Home = 'H'
    Dona = 'D'
    Altre = 'A'
    SEXE = [(Home, 'Home'), (Dona, 'Dona'), (Altre, 'Altre')]

    first_name = models.CharField('Nom', max_length=30)
    last_name = models.CharField('Cognoms', max_length=40)

    phone = models.CharField('Telèfon', max_length=9, null=True)
    sexe = models.CharField('Sexe', max_length=10, choices=SEXE, default='Altre' )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = ClientManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class ClientTest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
