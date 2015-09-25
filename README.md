# FGABrejaWeb

[ ![Codeship Status for Pi2-FGABreja/FGABrejaWeb](https://codeship.com/projects/c2c3e240-43ce-0133-7734-525e623546c2/status?branch=master)](https://codeship.com/projects/104164)

[![Code Climate](https://codeclimate.com/github/Pi2-FGABreja/FGABrejaWeb/badges/gpa.svg)](https://codeclimate.com/github/Pi2-FGABreja/FGABrejaWeb)

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

