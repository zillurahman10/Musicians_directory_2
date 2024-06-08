from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

choices = (
    ('guiter', 'Guiter'),
    ('piano', 'Piano'),
    ('drum', 'Drum'),
    ('elec_guiter', 'Electric Guiter'),
)

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    phone_number = forms.IntegerField()
    instrument_type = forms.ChoiceField(choices=choices)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'instrument_type']