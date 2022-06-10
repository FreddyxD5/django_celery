# Django-Celery mass mailing automate task
## Configuration 
1.- Clone this repository
  `https://github.com/FreddyxD5/django_celery.git`
2.- Create a virtual env 
  `python3 -m venv [name_virtualenv]`
3.- active virutal environment and go to project folder
4.- inside the project folder there's a file with django+libraries used in this project. execute this comand to install.
   `pip install -r requirements.txt` 
5.- You need a .env file. create new one and put in 'django_celery/configuration'
6.- Run the following command
   `python manage.py runserver` 
   
   
 # RabbitMQ
  1.- You need to install erlang and rabbitmq server as a next step to run celery tasks
  2.- Activate Rabbit MQ (Ubuntu 20.04)
    `sudo service rabbitmq-server restart` 
  3.- inside the django project folder run the following comand    
    `celery -A django-celery worker -l INFO`
