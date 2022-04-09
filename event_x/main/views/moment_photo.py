from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from event_x.main.forms import CreateMomentPhotoForm
from event_x.main.models import MomentPhoto


class CreateMomentPhotoView(LoginRequiredMixin, views.CreateView):
    form_class = CreateMomentPhotoForm
    template_name = 'main/create-moment-photo.html'
    success_url = reverse_lazy('moments')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditMomentPhotoView(LoginRequiredMixin, views.UpdateView):
    model = MomentPhoto
    fields = ('title', 'description')
    template_name = 'main/edit-moment-photo.html'
    success_url = reverse_lazy('moments')


class MomentPhotoListView(LoginRequiredMixin, views.ListView):
    template_name = 'main/moment-photos.html'
    model = MomentPhoto
    paginate_by = 5


class MomentPhotoDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'main/moment-details.html'
    model = MomentPhoto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context


@login_required
def delete_moment_photo(request, pk):
    moment = MomentPhoto.objects.get(pk=pk)
    moment.delete()
    return redirect('moments')

