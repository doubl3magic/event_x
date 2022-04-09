from django.urls import path

from event_x.main.views.event import EventDetailsView, EventListView
from event_x.main.views.generic import HomeView, AboutView, ContactUsView
from event_x.main.views.moment_photo import MomentPhotoListView, MomentPhotoDetailsView, delete_moment_photo, \
    CreateMomentPhotoView, EditMomentPhotoView

urlpatterns = (
    path('', HomeView.as_view(), name='home page'),
    path('about/', AboutView.as_view(), name='about page'),
    path('conacts/', ContactUsView.as_view(), name='contact us'),

    path('event/<int:pk>/', EventDetailsView.as_view(), name='event details'),
    path('events/', EventListView.as_view(), name='event list'),

    path('moment/create/', CreateMomentPhotoView.as_view(), name='create moment'),
    path('moments/', MomentPhotoListView.as_view(), name='moments'),
    path('moment/<int:pk>/', MomentPhotoDetailsView.as_view(), name='moment details'),
    path('moment/delete/<int:pk>/', delete_moment_photo, name='delete moment'),
    path('moment/edit/<int:pk>/', EditMomentPhotoView.as_view(), name='edit moment photo')
)
