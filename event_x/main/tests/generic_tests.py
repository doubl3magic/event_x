from django import test as django_test
from django.urls import reverse_lazy


class GenericViewsTest(django_test.TestCase):
    HOME_URL = reverse_lazy('home page')
    ABOUT_URL = reverse_lazy('about page')
    CONTACT_URL = reverse_lazy('contact us')

    def test_home_page__expect_correct_template(self):
        response = self.client.get(self.HOME_URL)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_about_page__expect_correct_template(self):
        response = self.client.get(self.ABOUT_URL)
        self.assertTemplateUsed(response, 'main/about.html')

    def test_contact_us__expect_correct_template(self):
        response = self.client.get(self.CONTACT_URL)
        self.assertTemplateUsed(response, 'main/contact-us.html')
