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

from .models import CustomUser, CustomUserProfileImage

# TODO: Add custom field validation error messages


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
        self.fields['first_name'] = forms.CharField(max_length=30,
                                                    label='First Name',
                                                    required=True,
                                                    widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
                                                    error_messages={'required': 'You must provide your first name'})
        self.fields['last_name'] = forms.CharField(max_length=30,
                                                   label='Last Name',
                                                   required=True,
                                                   widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
                                                   error_messages={'required': 'You must provide your last name'})
        self.fields['email'] = forms.CharField(label='Email',
                                               widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
        self.fields['password1'] = forms.CharField(label='Password',
                                                   widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
        self.fields['password2'] = forms.CharField(label='Confirm Password',
                                                   widget=forms.PasswordInput(
                                                       attrs={'placeholder': 'Enter your password again'}
                                                   ))

    def save(self, request):
        user = super(CustomAllauthSignupForm, self).save(request)
        # user_initials = user.first_name[:1] + user.last_name[:1]
        # user.profile_image_url = f'https://ui-avatars.com/api/?name={user_initials}&color=4338CA&background=C7D2FE'
        user.save()
        return user


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


class CustomUserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'birthday', 'phone', 'street_address', 'street_address_2', 'city',
                  'state', 'zip_code', 'biography', 'facebook', 'twitter', 'instagram', 'linkedin', )
        widgets = {
            'birthday': forms.TextInput(attrs={'type': 'date', }),
            'biography': forms.Textarea(attrs={'rows': 5, })
        }


class UploadProfileImageForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfileImage
        fields = ('profile_image', )
