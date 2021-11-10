# one time installs
These are installs that need to be done on a new computer.
- python
- git
- IDE (currently using pycharm)

# virtual environment
Every project starts with a new virtual environment
1. create project directory
2. enter the project directory: `cd folder_path`
3. create the virtual environment using python venv: `"C:\Users\chris\AppData\Local\Programs\Python\Python39\python.exe" -m venv venv`
4. activate the environment: `.\venv\Scripts\activate.bat`
 
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

> Written with [StackEdit](https://stackedit.io/).
