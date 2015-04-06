from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.shortcuts import redirect

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect to a success page.
            return redirect('frontpage')
        else:
            # render login again, but display error message
            context['login_failed'] = True
    # request.method == 'GET':
    return render(request, 'useraccounts/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('frontpage')

def user_register(request):
    pass