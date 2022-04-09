from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from event_x.auth_app.managers import EventXUserManager
from event_x.common.validators import validate_only_letters


class EventXUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = EventXUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 3
    LAST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 3

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters
        )
    )

    picture = models.ImageField(
        #validators=[MaxFileSizeInMbValidator(6)],
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    date_of_birth = models.DateTimeField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        EventXUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

