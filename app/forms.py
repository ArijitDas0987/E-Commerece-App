from cProfile import label
from pyexpat import model
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy
from django.contrib.auth import password_validation



class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(label='UserName',widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

    class Meta:
        model=User
        fields=('username','email','password1','password2')
        labels={'email':'Email'}
        
class CustomerLoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password=forms.CharField(label=gettext_lazy('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplte':'current-password', 'class':'form-control'}))


class ChangePasswordForm(PasswordChangeForm):
    old_password=forms.CharField(label=gettext_lazy('Old Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplte':'current-password','autofocus':True, 'class':'form-control'}))
    new_password1=forms.CharField(label=gettext_lazy('New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplte':'new-password', 'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=gettext_lazy('Confirm Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplte':'new-password', 'class':'form-control'}))

