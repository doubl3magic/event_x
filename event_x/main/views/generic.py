from django.shortcuts import redirect, render
from django.utils import timezone
from django.views import generic as views

# TODO: REDIRECT
from event_x.main.models import Event, Venue

events = Event.objects.all()
now = timezone.now()
just_added_events = Event.objects.filter(date_of_event__gte=now).order_by('date_of_event')[:3]

venues = Venue.objects.all()


class HomeView(views.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['hide_additional_nav_items'] = True
        context['just_added_events'] = just_added_events
        return context


class AboutView(views.TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['venues'] = venues[:3]

        return context


class ContactUsView(views.TemplateView):
    template_name = 'main/contact-us.html'


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)