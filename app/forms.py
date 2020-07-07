from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import us
from django.contrib.auth import authenticate


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(max_length=20,widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = User
        fields = [ 'first_name', 
                 'last_name', 
                 'email' 
                 ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
   
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Credentials not matched, try again!')
            # TODO These won't work - fix 
            elif not user.check_password(password):
                raise forms.ValidationError('Password incorrect.')
            elif not user.is_active:
                raise forms.ValidationError('This account is not active.')
        return super(LoginForm, self).clean(*args, **kwargs)
    