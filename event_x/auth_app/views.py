from django.contrib.auth import views as auth_views, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from django.shortcuts import render, redirect

# TO-D0: URL's
from django.urls import reverse_lazy

from event_x.auth_app.forms import CreateProfileForm
from event_x.auth_app.models import Profile

UserModel = get_user_model


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('login page')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/profile_login.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'is_owner': self.object.user.id == self.request.user.id,
        })

        return context


class EditUserProfileView(LoginRequiredMixin, views.UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'picture', 'email')
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('home page')


class ChangeUserPasswordView(LoginRequiredMixin, auth_views.PasswordChangeView):
    model = UserModel
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('home page')


def user_log_out(request):
    logout(request)
    return redirect('home page')