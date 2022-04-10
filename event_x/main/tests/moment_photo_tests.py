from datetime import date

from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse_lazy

from event_x.auth_app.models import Profile
from event_x.main.models import MomentPhoto, Event

UserModel = get_user_model()


class TestMomentPhotoViews(django_test.TestCase):
    MOMENT_PHOTO_VALID_DATA ={
        'title': 'Photo',
        'photo': SimpleUploadedFile('file.jpg', b'apple'),

    }

    EVENT_VALID_DATA = {
        'title': 'Event',
        'picture': SimpleUploadedFile('file.jpg', b'apple'),
        'description': 'aasss',
        'location': 'Sofia',
        'date_of_event': date(2020, 1, 1),
    }

    VALID_USER_DATA = {
        'username': 'testuserbg',
        'password': '123456TestI'
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'picture': SimpleUploadedFile("file.jpg", b'apple'),
        'date_of_birth': date(2000, 6, 30),
    }

    def __create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)

    def __create_user_with_profile(self):
        user = self.__create_user(**self.VALID_USER_DATA)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user
        )

        return (user, profile)

    def __create_user_and_login(self):
        user, profile = self.__create_user_with_profile()

        return self.client.login(**self.VALID_USER_DATA)

    def __create_moment_photo(self):
        event = Event.objects.create(**self.EVENT_VALID_DATA)
        event.save()
        user, _ = self.__create_user_with_profile()

        moment_photo = MomentPhoto.objects.create(**self.MOMENT_PHOTO_VALID_DATA,
                                                  user=user, event=event)

        return moment_photo

    def test_delete_moment_photo__expect_to_delete(self):
        moment_photo = self.__create_moment_photo()
        moment_photo.save()

        self.client.login(**self.VALID_USER_DATA)
        self.client.get(reverse_lazy('delete moment', kwargs={'pk': moment_photo.pk}))

        self.assertEqual(0, len(MomentPhoto.objects.all()))

    def test_details_get_context_data__expect_correct_data(self):
        moment_photo = self.__create_moment_photo()
        moment_photo.save()

        user_credentials = {
            'username': 'testuserbg2',
            'password': '123456DaiBg',
        }

        self.VALID_USER_DATA = user_credentials

        self.__create_user_and_login()

        response = self.client.get(reverse_lazy('moment details', kwargs={'pk': moment_photo.pk}))

        self.assertFalse(response.context['is_owner'])

