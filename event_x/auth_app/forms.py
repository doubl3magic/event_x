from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from event_x.auth_app.models import Profile


class CreateProfileForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LEN,
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LEN,
    )

    picture = forms.ImageField(
        #validators=[MaxFileSizeInMbValidator(6)],
    )

    email = forms.EmailField()

    date_of_birth = forms.DateField()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2' , 'first_name', 'last_name', 'picture')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'picture': forms.FileInput(
                attrs={
                    'placeholder': 'Upload Image Up to 6MB',
                }
            )
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Last Name',
                }
            ),
            'picture': forms.FileInput(
                attrs={
                    'placeholder': 'Upload Image Up to 6MB',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter Email',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'min': '1930-01-01',
                }
            )
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()

    class Meta:
        model = Profile
        fields = ()