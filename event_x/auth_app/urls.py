from django.urls import path

from event_x.auth_app.views import UserLoginView, UserRegisterView, ChangeUserPasswordView, EditUserProfileView, \
    UserProfileDetailsView, user_log_out

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login page'),
    path('register/', UserRegisterView.as_view(), name='register page'),
    path('password-change/', ChangeUserPasswordView.as_view(), name='change password'),
    path('edit-profile/<int:pk>/', EditUserProfileView.as_view(), name='edit profile'),
    path('<int:pk>/', UserProfileDetailsView.as_view(), name='profile details'),
    path('logout/', user_log_out, name='log out')
)