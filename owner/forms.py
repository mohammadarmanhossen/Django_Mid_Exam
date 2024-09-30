from django import forms  # Import the 'forms' module from Django, which is used to create form classes.
from django.contrib.auth.models import User  # Import the 'User' model from Django's built-in authentication system.
from django.contrib.auth.forms import UserCreationForm, UserChangeForm  # Import 'UserCreationForm', a built-in Django form for creating new users.


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    class Meta: # the class Meta inside a form class is used to provide metadata about the form. This metadata tells Django important information about how the form should behave or how it should interact with models.
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User  #built-in model/db for authenctication system
        fields = ['username', 'first_name', 'last_name', 'email']



