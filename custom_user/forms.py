from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from allauth.account.forms import (
    LoginForm,
    SignupForm,
    SetPasswordForm,
    ResetPasswordForm,
    ChangePasswordForm,
    ResetPasswordKeyForm
)

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', )


class CustomAllauthLoginForm(LoginForm, forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'] = forms.CharField(label='Email',
                                               widget=forms.EmailInput(attrs={'placeholder': 'Email address'}))


class CustomAllauthSignupForm(SignupForm, forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = forms.CharField(label='Email',
                                               widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
        self.fields['password1'] = forms.CharField(label='Password',
                                                   widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
        self.fields['password2'] = forms.CharField(label='Confirm Password',
                                                   widget=forms.PasswordInput(
                                                       attrs={'placeholder': 'Enter your password again'}
                                                   ))


class CustomAllauthSetPasswordForm(SetPasswordForm, forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(label='Password',
                                                   widget=forms.PasswordInput(
                                                       attrs={'placeholder': 'Password'}
                                                   ))
        self.fields['password2'] = forms.CharField(label='Confirm Password',
                                                   widget=forms.PasswordInput(
                                                       attrs={'placeholder': 'Enter your password again'}
                                                   ))


class CustomAllauthResetPasswordForm(ResetPasswordForm, forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = forms.CharField(label='Email',
                                               widget=forms.EmailInput(attrs={'placeholder': 'Email address'}))


class CustomAllauthChangePasswordForm(ChangePasswordForm, forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['oldpassword'] = forms.CharField(label='Old Password',
                                                     widget=forms.PasswordInput(
                                                         attrs={'placeholder': 'Your old password'}
                                                     ))
        self.fields['password1'] = forms.CharField(label='New Password',
                                                   widget=forms.PasswordInput(
                                                       attrs={'placeholder': 'Your new password'}
                                                   ))
        self.fields['password2'] = forms.CharField(label='Confirm New Password',
                                                   widget=forms.PasswordInput(
                                                       attrs={'placeholder': 'Confirm your new password'}
                                                   ))


class CustomAllauthResetPasswordKeyForm(ResetPasswordKeyForm, forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(label='New Password',
                                                   widget=forms.PasswordInput(
                                                       attrs={'placeholder': 'Your new password'}
                                                   ))
        self.fields['password2'] = forms.CharField(label='Confirm New Password',
                                                   widget=forms.PasswordInput(
                                                       attrs={'placeholder': 'Confirm your new password'}
                                                   ))
