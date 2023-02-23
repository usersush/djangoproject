from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from random import randint

no, user, email = 0, '', ''


def signupview(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account "{username}" has been Created! You are now able to login.')
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/signup.html', {'form': form})


def loginview(request):
    global user, email
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            data = User.objects.get(username=username)
            email = data.email
            return redirect('otp')
        else:
            messages.error(request, 'Please enter a correct username and password')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def otpview(request):
    global no, user, email
    if request.method == "POST":
        otp = int(request.POST.get('otp'))
        if otp == no:
            login(request, user)
            messages.success(request, 'Login Successful')
            no, user, email = 0, '', ''
            return redirect('home')
        else:
            messages.error(request, 'Wrong OTP')
    else:
        pass
        # recipients_list = [email]
        # no = randint(100000, 999999)
        # subject = 'Login OTP'
        # message = f'Your Login OTP L-{no}\nDo not share this otp with anyone!!!'
        # email_from = settings.EMAIL_HOST_USER
        # send_mail(subject, message, email_from, recipients_list)
    return render(request, 'user/otp.html')


@login_required()
def profileview(request):
    return render(request, 'user/profile.html')


@login_required()
def edit_profileview(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'You account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/edit_profile.html', context)

