from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, PasswordInput, ModelForm


class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)


class UserRegistrationForm(ModelForm):
    password = CharField(label='Password',
                         widget=PasswordInput)
    password2 = CharField(label='Repeat Password',
                          widget=PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Passwords don\'t match.')
        return cd['password2']
