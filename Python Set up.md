# one time installs
These are installs that need to be done on a new computer.
- python
- git
- IDE (currently using pycharm)

# virtual environment
Every project starts with a new virtual environment

development (Windows)
1. create project directory
2. enter the project directory: `cd folder_path`
3. create the virtual environment using python venv: `"C:\Users\chris\AppData\Local\Programs\Python\Python39\python.exe" -m venv venv`
4. activate the environment: `.\venv\Scripts\activate.bat`
5. update/save library dependencies `pip freeze > requirements.txt`


# deployment
[Python Anywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/) (Linux)
1. clone git repo
   1. ideally requirements.txt is included
2. create the virtual environment
3. `mkvirtualenv --python=/usr/bin/python3.8 mysite-virtualenv`
4. `pip install -r requirements.txt`
5. set up web app and WSGI file
   1. select new app with manual config or use old app's Web tab
   2. enter virtualenv name: [mysite-virtualenv]
   3. enter path to code
   4. edit WSGI file
      1. set path variable: `path = '/home/myusername/mysite'`
      2. point to correct settings.py file  `os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'`
6. edit settings file if there isn't a seperate deployment settings
   1. add domain `ALLOWED_HOSTS = ['myusername.pythonanywhere.com',]`
   2. add pointer to static directory (populated by `python manage.py collectstatic`) `STATIC_ROOT = '~/.../static'`
7. set up database: `./manage.py migrate`
8. load to check if worked so far
9. `./manage.py collectstatic`



# git repo
Try to establish version control from the start of the project.
 1. enter the project directory: `cd folder_path`
 2. initialize local git repository: `git init`
 3. add/create .gitignore file
 4. add files/folders to be tracked `git add .gitignore`
 5. commit: `git commit`
    - alternatively `git commit - m "msg"`
 6. create remote repository on github
 7. set up ssh keys if none are available
    - (with configs if you want to have different names)
    - if ssh keys can't be found, try setting the home location:`setx HOME c:\users\chris`
 8. add remote repo location:`git remote add origin git@github.com:DreamBrookStudio/DjangoBasic`
 9. push to github: `git push -u origin master`

# Django
1. `django-admin startproject mysite`
[SEE the Django Tutorial]
