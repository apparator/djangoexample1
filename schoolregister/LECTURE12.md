# Lecture 12 - Handling users and authentication

```bash
python manage.py startapp useraccounts
```

Add 'useraccounts' to `settings.py`.

Add this line to `schoolregister/urls.py`:

```python
    url(r'^useraccounts/', include('useraccounts.urls')),
```

Create new file `useraccounts/urls.py` and add the following:

```python
from django.conf.urls import patterns, url
from useraccounts import views

urlpatterns = patterns('',
    url(r'^login$', views.user_login, name='user_login'),
)
```

Add to `useraccounts/views.py`:

```python
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def user_login(request):
    return render(request, 'useraccounts/login.html')
```

