from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from allauth.account.forms import LoginForm as AllauthLoginForm, SignupForm as AllauthSignupForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', )


class CustomAllauthLoginForm(AllauthLoginForm, forms.Form):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'] = forms.CharField(label='Email',
                                               widget=forms.EmailField(attrs={'placeholder': 'Email Address'}))


class CustomAllauthSignupForm(AllauthSignupForm, forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = forms.CharField(label='Email',
                                               widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
        self.fields['password1'] = forms.CharField(label='Password',
                                                   widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
        self.fields['password2'] = forms.CharField(label='Confirm Password',
                                                   widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again'}))
