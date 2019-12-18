## Texada Demo Backend Api


### Setting up in local pc

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



