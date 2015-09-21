# FGABrejaWeb

### Setting up development environment

```
$ sudo apt-get install python3 python3-pip
$ sudo pip3 install -r requirements.txt
```

```
$ cp settings/databases settings/databases.py
$ cp settings/security settings/security.py
```

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

