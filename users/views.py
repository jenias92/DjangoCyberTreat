from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ResetPasswordEnterToken
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account {username} Created! Please Sign In')
            return redirect('signin')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def change_password(request):
    if request.method == "POST":
        change_password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if change_password_form.is_valid():
            change_password_form.save()
            messages.success(request, f'Password successfully changed for user {change_password_form.user.username}!')
            return redirect('customers-home-page')

    else:
        change_password_form = PasswordChangeForm(User)
    return render(request, "users/change_password.html", {'form': change_password_form})


def reset_password(request):
    if request.method == "POST":
        reset_password_form = PasswordResetForm(request.POST)
        if reset_password_form.is_valid():
            reset_password_form.save(request=request, email_template_name='users/email_rest_password.html')
            email = reset_password_form.cleaned_data.get("email")
            messages.success(request, f'If the email: {email} exist in our records, '
                                      f'we will send a instruction to reset password!')
            return redirect('customers-home-page')

    else:
        reset_password_form = PasswordResetForm()
    return render(request, "users/change_password.html", {'form': reset_password_form, "button": "Send Reset Email"})


def password_reset_enter_token(request, uidb64):
    check_token = ResetPasswordEnterToken()
    if request.method == "POST":
        check_token = ResetPasswordEnterToken(request.POST)
        if check_token.is_valid():
            token = check_token.cleaned_data.get("verification_code")
            return redirect('reset-password-confirm', uidb64=uidb64, token=token)

    return render(request, "users/change_password.html", {'form': check_token, "button": "Process"})


def password_reset_complete(request):
    messages.success(request, f'Password Reset Done, Please Sign In')
    return redirect('signin')
