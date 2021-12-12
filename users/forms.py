from django import forms
# Класс User работает с табличкой пользователей
from django.contrib.auth.models import User
# Встроеные формы в джанго
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # Поле в форме (используються при наследовании form.Forms)
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

    # В класе мета прописываем характеристики (при использовании UserCreationForm)
    class Meta:
        model = User
        # Поля в форме
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # Этот клас обновляет email и login
    # Поле в форме (используються при наследовании form.Forms)
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
        # Поля в форме
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    # Класс для загрузки фото в личном кабинете
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']




#some = forms.ModelChoiceField(queryset=User.objects.all())         Поле для списка выбора!!!

''' В Джанго что бы создать форму нужно создать класс и в классе описать какие будут поля в форме'''