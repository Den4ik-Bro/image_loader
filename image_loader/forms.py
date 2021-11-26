from django import forms
from .models import Image
from django.contrib.auth import get_user_model

User = get_user_model()


class ImageLoadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            'title',
            'image',
        )


class RegistrationUserForm(forms.ModelForm):
    password_1 = forms.CharField(widget=forms.PasswordInput(), label='Введите пароль')
    password_2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = User
        fields = \
            (
                'username',
                'first_name',
                'last_name',
                'email',
        )