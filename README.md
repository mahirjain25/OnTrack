# OnTrack

Requirements:

1. Python >= 3.5

2. Pipenv (For virtual environent set-ups): 
Install via ```pip3 install pipenv```
Then cd to OnTrack/ontrack and run ```pipenv shell``` and install the rest of the dependancies as listed in this document.

3. Django 2.0: 
To run the server, change directory to ```OnTrack/ontrack/ontrack``` and run ```python3 manage.py runserver```


**PRE-REQUISITES**
Install MySQL using the following commands:

```
sudo apt-get update
sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
 ```

followed by

```
sudo mysql_install_db
sudo mysql_secure_installation
sudo pip install mysqlclient
```

Once you have MySQL setup, change directory to `/ontrack/ontrack' and run ```mysql -u root -p < script.sql``` 

In ```ontrack/ontrack/ontrack/settings.py``` , make the following changes:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ontrack',
        'USER' : 'django',
        'PASSWORD' : 'password',
        'HOST': '',
        'PORT': '',

    }
} 
```



