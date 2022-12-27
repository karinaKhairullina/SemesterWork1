from django import forms
from .models import Serials
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Form(forms.ModelForm):
    class Meta:
        model = Serials
        fields = ('title', 'link')
        labels = {
            'title': 'Название',
            'link': 'Ссылка'
        }

    def __int__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

