from django.utils import timezone
from django.views import generic as views

from event_x.main.models import Event


class EventDetailsView(views.DetailView):
    template_name = 'main/event-details.html'

    model = Event


class EventListView(views.ListView):
    template_name = 'main/shows-events.html'

    model = Event
    paginate_by = 5

    def get_queryset(self):
        now = timezone.now()
        upcoming = Event.objects.filter(date_of_event__gte=now).order_by('date_of_event')
        return upcoming

