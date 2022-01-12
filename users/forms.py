from django import forms
# User class works with users table
from django.contrib.auth.models import User
# Forms in django
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # Fields in form django
    username = forms.CharField(
        label='Login',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Login'})
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        help_text='Нельзя вводить символы: @, /, -',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )

    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='Пароль должен состоять из 8 символов и большой буквы',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )

    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторно введите пароль'})
    )

    # In class meta, we write the characteristics (when using UserCreationForm)
    class Meta:
        model = User
        # Fields in form
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # This class updates email and login
    # Form field (used when inheriting form.Forms)
    username = forms.CharField(
        label='Login',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Login'})
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        help_text='Нельзя вводить символы: @, /, -',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )

    class Meta:
        model = User
        # Fields in form
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    # Class for uploading photos in your personal account
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']
