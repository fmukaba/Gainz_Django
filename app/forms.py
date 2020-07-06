from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(max_length=20,widget=forms.PasswordInput, label="Confirm password")

    # def clean(self):
    #     return super().clean()

    class Meta:
      model = User
      fields = [ 'first_name', 
                 'last_name', 
                 'email' 
                 ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    