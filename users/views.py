from django.shortcuts import render, redirect
# Ипорт класса для форм
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Обрабатывает страницу с регистрацией (html)
def register(request):
    # Проверяет данные из страницы регистрации
    if request.method == "POST":
        # В этом объекте храняться все данные получиные от пользователя
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Сохраняет данные в БД
            form.save()
            # Берет имя пользователя с страницы регистрации
            username = form.cleaned_data.get('username')
            # Cообщение об успешной регистрации пользователя
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Страница регистрации',
            'form': form
        }
    )


# Дикоратор проверяет авторизован ли пользователь
@login_required
def profile(request):
    # Проверка верны ли данные пользователя
    if request.method == "POST":
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        if profileForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен!')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
    }
    return render(request, 'users/profile.html', data)

