from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'p-1 border border-gray-300 rounded-sm ml-2'})
        self.fields['password1'].widget.attrs.update({'class': 'p-1 border border-gray-300 rounded-sm ml-2'})
        self.fields['password2'].widget.attrs.update({'class': 'p-1 border border-gray-300 rounded-sm ml-2'})

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'p-1 ml-2 border border-gray-300 rounded-sm'})
        self.fields['password'].widget.attrs.update({'class': 'p-1 ml-2 border border-gray-300 rounded-sm'})


