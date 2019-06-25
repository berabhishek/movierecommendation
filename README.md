# Movie Recommendation

This is an AI based tool that recommends movies based on current user ratings of the movies.

This project is implemented in Python (Django + Tensorflow) as one of the projects under the `100 days of ML challenge`

Currently, the backend of the code is not ready. We expect to go live by the first week of March 2k19. 

# Getting Started

* Clone the repo
* cd inside the project
* Install django

 ```console
foo@bar:~$ pip3 install django
```
* Open `movierecommend/settings.py` and on line no 26 set `DEBUG = True` and on line no 28 set `ALLOWED_HOSTS = []`

* Finally run these commands from the project home directory

```console
foo@bar:~$ python3 manage.py makemigrations
foo@bar:~$ python3 manage.py migrate
foo@bar:~$ python3 manage.py createsuperuser
username: <enter username>
email: <leave blank>
password: <enter password>

foo@bar:~$ python3 manage.py runserver
 ```

* In your browser open http://127.0.0.1:8000