from django.contrib.auth import authenticate, login
from django.shortcuts import render

def user_login(request):
    return render(request, 'useraccounts/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                pass
        else:
            # Return an 'invalid login' error message.
            pass
    elif request.method == 'GET':
        return render(request, 'useraccounts/login.html')
