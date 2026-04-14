from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if not user.is_active:
                messages.error(request, _("حسابك غير نشط. يرجى الاتصال بالمسؤول."))
                return render(request, 'accounts/login.html')
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, _("اسم المستخدم أو كلمة المرور غير صحيحة."))
            
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required
def dashboard_redirect(request):
    if request.user.role == 'owner':
        return redirect('dashboard_owner')
    elif request.user.role == 'hr':
        return redirect('dashboard_hr')
    else:
        return redirect('dashboard_employee')