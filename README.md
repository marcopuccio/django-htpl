# HTPL

Simple app made of django generic views, which make possible to use the Django template features during frontend development process :)


### Requirements

Htpl is developed and require Django>=1.9 and Python > 2.7

### How to install it

It can be installed via pip running the next command.
```
pip install git+http://github.com/marcopuccio/django-htpl.git
```

After installation, you must include it in your ```settings.py```. You can add it via the app config file, or the appname
```
INSTALLED_APPS = [
    ...
    # Via config file
    'htpl.apps.HtplConfig',
    ...
    # Via appname
    'htpl',
]
```
Then add it in ```urls.py```:
```
urlpatterns = [
    ...
    url(r'', include('htpl.urls')),
    ]
```

**Congrats, it's ready!***
