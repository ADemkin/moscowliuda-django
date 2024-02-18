from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email', max_length=254)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['username']

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email is not None and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
