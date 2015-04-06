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

Now we can check that the url and the view works. It should report "template not found", and it does. 

We create a templates folder in `useraccounts` and another `useraccounts` folder in that as allways. And then we add the login.html file in that, with just a simple "Hello Login!" text for testing.

## Refactoring template again

Here we meet a new issue. We do not want the header in the login view, and neither in the register view we are creating later. We need to refactor again, and this time we create `site_base.html` template. This template will contain what we need on all pages. After that, we then must make one base template for useraccounts pages (login and register) and one for the other pages.

The new `theme/site_base.html`:

https://github.com/apparator/djangoexample1/blob/lecture12/schoolregister/theme/templates/theme/site_base.html

The new `theme/base.html`

https://github.com/apparator/djangoexample1/blob/lecture12/schoolregister/theme/templates/theme/base.html

After that we create a `useraccounts/base.html` for use in `login.html` and later `register.html`:

https://github.com/apparator/djangoexample1/blob/lecture12/schoolregister/useraccounts/templates/useraccounts/base.html

## Back to user handling

Now we update ´login.html´ so that it uses our new ´base.html´. It then looks like this (but without the form):

https://github.com/apparator/djangoexample1/blob/lecture12/schoolregister/useraccounts/templates/useraccounts/login.html

We find a suited form at 'getbootstrap.com', and that is what we add next.

This form has some extra styling, which we will put in a separate styling used only for useraccount views. We add this in the folder `useraccounts/static/useraccount/css` and we call the file `style.css`:

https://github.com/apparator/djangoexample1/blob/lecture12/schoolregister/useraccounts/static/useraccounts/css/style.css

### Actual login

Now we are ready to update the view so that it actually logs a user in. Everything inside `if request.method == 'POST':` in `views.py` is for this purpose:
 
https://github.com/apparator/djangoexample1/blob/lecture12/schoolregister/useraccounts/views.py

Now, if we have a user we can actually see that the header is showing my username. See in the top right corner. In this line:

https://github.com/apparator/djangoexample1/blob/lecture12/schoolregister/theme/templates/theme/base.html#L24

we are using `{% if user.is_anonymous %}` to show a different menu for logged in and anonymous users. 

In your assignement you need to show different things for anonymous and authenticated users, so pay attention to how this is done.

Now we should make it possible to log out. How do we do that? 

We add a new url as shown in this file:

https://github.com/apparator/djangoexample1/blob/lecture12/schoolregister/useraccounts/urls.py

Then we need a view for this, which we have made here:

https://github.com/apparator/djangoexample1/blob/lecture12/schoolregister/useraccounts/views.py

Last, we need to add a logout option for users that are authenticated. This is a possible way to do it in our `useraccounts/views.py`:

```python
def user_logout(request):
    logout(request)
    return redirect('frontpage')
```

Now we can log in and out and see that the header menu on the right side changes.









