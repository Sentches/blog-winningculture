# Miami Heat Blog using Django

## Description

This is my first Django project, I really enjoyed using this library because it gives you a lot of power and can save you a lot of valuable time building a web application. My goal was to create a blog about my favorite team in the NBA, the Miami Heat. My biggest challenge was building the comment section, I spent a lot of time trying to understand how to use Django Forms, create Views and how I could link the comment to a post.

## How to Use

1 - Go to the project directory on CMD;

2 - Create a Virtual Enviroment and activate it;

3 - Install Django, ipython, python-decouple with pip install;

4 - Inside the "settings.py" file erase the line 15;

5 - Line 25 change the value of "SECRET_KEY" to a secret key you want to use;

6 - Line 28 change the value of "DEBUG" to "True";

7 - On your terminal inside the VE, open the folder "winningculture" (folder where manage.py should be);

8 - Run "python manage.py makemigrations" and then "python manage.py migrate";

9 - Before you can run the server, first you should create a admin user with "python manage.py createsuperuser";

10 - Now, you can run the server with "python manage.py runserver" and copy the address highlited below and paste it on your browser;

![Screenshot](/tutorial01.jpg)

There it is! To access the admin area, add "/admin" at the end of the URL and start creating some posts!

## Pip List

On this list, you will find every library I had on my virtual enviroment.

- asgiref           3.5.0
- asttokens         2.0.5
- backcall          0.2.0
- black             22.1.0
- click             8.0.3
- colorama          0.4.4
- decorator         5.1.1
- Django            4.0.2
- executing         0.8.2
- ipython           8.0.1
- jedi              0.18.1
- matplotlib-inline 0.1.3
- mypy-extensions   0.4.3
- parso             0.8.3
- pathspec          0.9.0
- pickleshare       0.7.5
- pip               22.0.3
- platformdirs      2.5.0
- prompt-toolkit    3.0.27
- pure-eval         0.2.2
- Pygments          2.11.2
- python-decouple   3.6
- setuptools        60.6.0
- six               1.16.0
- sqlparse          0.4.2
- stack-data        0.1.4
- tomli             2.0.1
- traitlets         5.1.1
- tzdata            2021.5
- wcwidth           0.2.5
- wheel             0.37.1

# Links 

- Linkedin - [Carlos Maia](https://www.linkedin.com/in/carlosmaiaa/)

# Credits 

I watched [this tutorial](https://youtu.be/Dzuiy-JNi-E) made by [Fabio Rucci](https://github.com/fabioruicci) to build my project.
