from django import forms

from event_x.main.models import Event, MomentPhoto


# TODO: Add some widgets to the forms


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class DeleteEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class CreateMomentPhotoForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        moment_photo = super().save(commit=False)

        moment_photo.user = self.user
        if commit:
            moment_photo.save()

        return moment_photo

    class Meta:
        model = MomentPhoto
        fields = ('title', 'photo', 'description', 'event')


class DeleteMomentPhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = MomentPhoto
        fields = ()