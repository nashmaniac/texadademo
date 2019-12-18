## Texada Demo Backend Api


### How to set up in local pc

----
Please follow the following instruction to run locally

Disclaimer: This instructions is written based on macos environment

* Open a terminal
* Run `git clone git@github.com:nashmaniac/texadademo.git` to clone the repository in your local
* Run `cd texadademo` to enter the folder in terminal
* Create a virtual environment by running `virtualenv venv -p /usr/local/bin/python3`
* Activate the virtual environment with `source venv/bin/activate`
* Run `pip install -r requirements.txt` to install all the dependencies
* Make sure you have postgres installed in your local and is accessible
* Now make sure you have the following `environment variables` set in your envirnoment. Here are the samples
    * `export ALLOWED_HOSTS='0.0.0.0'`
    * `export DATABASE_NAME='texada'`
    * `export DATABASE_USERNAME='db_user_name'`
    * `export DATABASE_PASSWORD='db_user_password'`
    * `export static_url='texada'`
* Run `python manage.py migrate` to run migration files to make sure the database has necessary tables and columns
* Run `python manage.py runserver`
* The development server should be running at `http://0.0.0.0:8000`

--- 
### Project Structure

```
texadademo
├── Dockerfile                  # dockerfile to containerize application
├── README.md
├── core                        # core app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py           # abstract models to be inherited by others
│   ├── tests.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── response.py         # response module to handle rest framework response
│   │   └── utls.py
│   └── views.py
├── manage.py                   # manager file
├── products                    # products app
│   ├── __init__.py
│   ├── admin.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── urls.py             # api url mapper
│   │   └── v1                  # v1 api for products app
│   │       ├── __init__.py
│   │       ├── serializers     # serializers to serialize models and validate data
│   │       │   ├── __init__.py
│   │       │   ├── product.py
│   │       │   └── tracking.py
│   │       ├── urls.py         # v1 urls for products app
│   │       └── views
│   │           ├── __init__.py
│   │           ├── product.py
│   │           └── tracking.py
│   ├── apps.py
│   ├── datalayers              # abstraction layer in between view and models
│   │   ├── __init__.py
│   │   └── product.py
│   ├── migrations              # migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models                  # models
│   │   ├── __init__.py
│   │   ├── product.py
│   │   └── tracking.py
│   ├── tests                   # sample tests for TDD development
│   │   ├── __init__.py
│   │   └── product.py
│   ├── urls.py                 # product app urls
│   └── views.py
├── requirements.txt            # dependency file
├── templates
└── texadademo
    ├── __init__.py
    ├── asgi.py
    ├── settings.py             # settings file
    ├── urls.py                 # main url mapper
    └── wsgi.py                 # wsgi file

```  


