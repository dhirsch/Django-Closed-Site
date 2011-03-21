from django import forms

class AuthenticateForm(forms.Form):
    value = forms.CharField(max_length=50)