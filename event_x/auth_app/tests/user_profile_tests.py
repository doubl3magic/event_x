from datetime import date
from django import test as django_test
from django.contrib.auth import get_user_model
from django.contrib.auth.middleware import get_user
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpRequest
from django.urls import reverse_lazy, reverse

from event_x.auth_app.models import Profile
from event_x.main.models import MomentPhoto

UserModel = get_user_model()


def get_user_data(self):
    request = HttpRequest()
    request.session = self.client.session
    return get_user(request)


class UserProfileViewTests(django_test.TestCase):
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

    VALID_REGISTER_DATA = {
        'username': 'testuserbg',
        'password1': '123456TestI',
        'password2': '123456TestI',
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

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def test_create_user__expect_to_create(self):
        user, _ = self.__create_user_with_profile()

        expected_username = self.VALID_USER_DATA['username']
        actual = user.username

        self.assertEqual(expected_username, actual)
        self.assertFalse(user.is_staff)

    def test_create_profile__expect_to_create(self):

        _, profile = self.__create_user_with_profile()

        expected_first_name = self.VALID_PROFILE_DATA['first_name']
        expected_last_name = self.VALID_PROFILE_DATA['last_name']
        actual_first_name = profile.first_name
        actual_last_name = profile.last_name

        self.assertIsNotNone(profile)
        self.assertEqual(expected_first_name, actual_first_name)
        self.assertEqual(expected_last_name, actual_last_name)

    def test_login_profile__expect_to_login(self):
        self.__create_user_and_login()

        self.client.logout()

        user = get_user_data(self)
        self.assertTrue(user.is_anonymous)

    def test_show_profile_details__expect_correct_template(self):
        _, profile = self.__create_user_with_profile()
        self.__get_response_for_profile(profile)
        self.assertTemplateUsed('accounts/profile_details.html')

    def test_show_profile_details__expect_correct_data(self):
        self.__create_user_and_login()
        user_id = get_user_data(self).id

        response = self.client.get(reverse_lazy('profile details', kwargs={'pk': user_id}))

        expected = user_id
        actual = response.context_data['profile'].user_id

        self.assertEqual(expected, actual)

    def test_edit_profile__expect_to_edit(self):
        self.__create_user_and_login()
        user = get_user_data(self)

        self.VALID_PROFILE_DATA['last_name'] = 'Dimitrov'
        self.client.post(
            reverse_lazy('edit profile', kwargs={'pk': user.id}),
            data=self.VALID_PROFILE_DATA,
        )

        user = get_user_data(self)
        profile = Profile.objects.get(pk=user.id)

        self.assertEqual(self.VALID_REGISTER_DATA['last_name'], profile.last_name)



