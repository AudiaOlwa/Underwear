from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="", max_length=30, 
                               widget=forms.TextInput(attrs={'class':'zmdi zmdi-account material-icons-name  ', 'name':'username', 'placeholder':'Nom d\'utilisateur'}))
    password = forms.CharField(label="", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class':'zmdi zmdi-account material-icons-name ', 'name':'password', 'placeholder':'Mot de passe'}))


