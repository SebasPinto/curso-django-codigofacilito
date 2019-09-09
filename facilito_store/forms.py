from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                min_length=4,
                                max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control mb-4',
                                    'placeholder': 'User Name',
                                    'icon': 'person'
                                }))
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={
                                    'class': 'form-control mb-4',
                                    'placeholder': 'Email',
                                    'icon': 'email'
                                }))
    password=forms.CharField(required = True,
                                min_length = 8,
                                max_length = 12,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control mb-4',
                                    'placeholder': 'Password',
                                    'icon': 'lock'
                                }))

    password2=forms.CharField(required = True,
                                min_length = 8,
                                max_length = 12,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Repeat Password',
                                    'icon': 'lock'
                                }))


    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('User Name already exists')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')

        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Passwords not matching')


