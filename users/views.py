from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Handles the registration page
def register(request):
    # Checks data from the registration page
    if request.method == "POST":
        # All data received from the user is stored in this object.
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Saves data to the database
            form.save()
            # Takes username from registration page
            username = form.cleaned_data.get('username')
            # User registration successful message
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


# Checks if the user is authorized
@login_required
def profile(request):
    # Checking if user data is correct
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

