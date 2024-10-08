from django import forms
from accounts.models import SiteUser

class SiteUserSignupForm(forms.ModelForm):
  class Meta:
    model = SiteUser
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    labels = {'username':'Pseudo', 'first_name':'Prénom', 'last_name':'Nom', 'email':'email', 'password':'Mot de passe'}
    widgets = {'password':forms.PasswordInput()}


class SiteUserUpdateForm(forms.ModelForm):
  class Meta:
    model = SiteUser
    fields = ['username', 'first_name', 'last_name', 'email']
    labels = {'username':'Pseudo', 'first_name':'Prénom', 'last_name':'Nom', 'email':'email'}
    