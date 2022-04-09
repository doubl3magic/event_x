from django.views import generic as views

from event_x.main.models import Event


class EventDetailsView(views.DetailView):
    template_name = 'main/event-details.html'

    model = Event


class EventListView(views.ListView):
    template_name = 'main/shows-events.html'

    model = Event
    paginate_by = 5


