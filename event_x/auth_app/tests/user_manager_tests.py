from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

UserModel = get_user_model()


class ManagerTests(django_test.TestCase):
    VALID_USER_DATA = {
        'username': 'testuserbg',
        'password': '123456TestI'
    }

    def test_create_superuser__expect_to_set_successful(self):
        manager = UserModel.objects

        user = manager.create_superuser(username=self.VALID_USER_DATA['username'],
                                        password=self.VALID_USER_DATA['password'])

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_superuser__without_username__expect_to_raise(self):
        manager = UserModel.objects

        with self.assertRaises(ValueError) as username_error:
            manager.create_superuser(username='',
                                     password=self.VALID_USER_DATA['password'])

        self.assertEqual('The given username must be set', username_error.exception.args[0])

    def test_create_superuser__expect_value_Error(self):
        manager = UserModel.objects
        staff = {'is_staff': False}
        superuser = {'is_superuser': False}

        with self.assertRaises(ValueError) as is_not_staff_error:
            manager.create_superuser(username=self.VALID_USER_DATA['username'], password=self.VALID_USER_DATA['password'], **staff)

        with self.assertRaises(ValueError) as is_not_superuser_error:
            manager.create_superuser(username=self.VALID_USER_DATA['username'], password=self.VALID_USER_DATA['password'], **superuser)

        self.assertEqual('Superuser must have is_staff=True.', is_not_staff_error.exception.args[0])
        self.assertEqual('Superuser must have is_superuser=True.', is_not_superuser_error.exception.args[0])