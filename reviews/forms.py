from django import forms
from .models import UserRegister,Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input-group'}))
    email = forms.EmailField(max_length=70, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input-group'}))
    password1 = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input-group', 'id': 'password'}))
    password2 = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'input-group', 'id': 'password'}))

    class Meta:
        model = UserRegister
        fields = ['username', 'email', 'password1', 'password2']
        error_messages = {
        "password_mismatch": "Conform Password Does not match with Password"
    }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserRegister.objects.filter(email=email).exists():
            raise ValidationError('This email address is already in use.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UserRegister.objects.filter(username=username).exists():
            raise ValidationError('This username is already in use.')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(self.error_messages['password_mismatch'], code='password_mismatch')
        return password2


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, required=True ,widget=forms.TextInput(attrs={'placeholder':'Username','class':'input-group'}))
    password = forms.CharField(max_length=128,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input-group', 'id': 'password'}))

    class Meta:
        model= User
        fields=['username','password']

class Reviews_Form(forms.ModelForm):
    class Meta:
        model = Review
        fields= ['Review']