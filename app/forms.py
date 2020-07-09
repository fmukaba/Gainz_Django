from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Exercise, Workout


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = User
        fields = [ 'first_name', 
                 'last_name', 
                 'email' 
                 ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
   
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # TODO
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

class CreateExerciseForm(forms.Form):
    title = forms.CharField(max_length=50,widget=forms.TextInput, initial=" ")
    sets = forms.IntegerField(initial=1)
    reps = forms.IntegerField(initial=1)
    time = forms.IntegerField(initial=1)
    link = forms.CharField(max_length=1000,widget=forms.TextInput, initial=" ")
    description = forms.CharField(max_length=100, widget=forms.Textarea, initial=" ")
    
    def extract(self):
        errors = self.errors

        if self.is_valid():
            obj = Exercise(
                title=self.cleaned_data['title'],
                sets=self.cleaned_data['sets'],
                reps=self.cleaned_data['reps'],  
                time=self.cleaned_data['time'],      
                link=self.cleaned_data['link'], 
                description=self.cleaned_data['description']         
                )
            return obj
        return None

    # class Meta:
    #     model = Exercise
    #     fields = ['title']
        
    # def clean(self, *args, **kwargs):
    #     # check for duplicated title+reps+sets+time
    #     if not self.cleaned_data.get('title'):
    #         raise forms.ValidationError('Credentials not matched, try again!')
    #     return super(CreateExerciseForm, self).clean(*args, **kwargs)