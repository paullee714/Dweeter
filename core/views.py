from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def login_user(request):
    if request.method == "POST":
        login_data = request.POST
        username = login_data['username']
        password = login_data['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user=user)
            return redirect('base')
        else:
            return render(request, 'base.html', {'error': '로그인 정보를 확인하세요'})
    else:
        return render(request, 'base.html')


def logout_user(request):
    logout(request)
    return redirect('base')