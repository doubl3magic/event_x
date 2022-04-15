from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Event(models.Model):
    CONCERT = "Concert"
    THEATRE = "Theatrical"
    FAN_MEET = "Fan meeting"
    SEMINAR = "Seminar"
    CEREMONIES = "Ceremonies"

    TYPES = [(x, x) for x in (CONCERT, THEATRE, FAN_MEET, SEMINAR, CEREMONIES) ]

    NAME_MAX_LENGTH = 40
    LOCATION_MAX_LENGTH = 50

    title = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    picture = models.ImageField()

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    description = models.TextField()

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
    )

    ticket_url = models.URLField()

    date_of_event = models.DateTimeField()

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.title}, {self.type}"


class Venue(models.Model):
    NAME_MAX_LENGTH = 40
    LOCATION_MAX_LENGTH = 50

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    photo = models.ImageField()

    description = models.TextField()

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
    )

    def __str__(self):
        return f"{self.name}"


class MomentPhoto(models.Model):
    TITLE_MAX_LENGTH = 40

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    photo = models.ImageField()
    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.title}, {self.event.title}"