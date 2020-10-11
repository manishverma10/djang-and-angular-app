This app is developed using Python's Framework Django, sqlite3. Django is based on MVT architecture 

This application is based on Employee-Manager relationship.


Setup Guidence:

User should have following things to run this app:

Python version > 3.* you can download from their official website
Django version > 2.* pip install django
Virtual  Environment(pipenv shell, virtualenv, workon) 


Steps to run app:

1. Go to project directory using terminal where is project is going to be placed
2. Activate virtual environment
3. python3 manage.py createsuperuser -------  to create user admin/user and access admin panel
4. python3 manager runsrever ------- to run project
5. http://localhost:8000/list/ ------- is the url to access page, port depends 
6. http://localhost:8000/admin/ --------- to access admin panel
7. http://localhost:8000/list/restrest/ ------- to access rest API(json format as mentioned in req. pdf)


Django ORM to create CEO/Manager using shell:

go to project directory and run 'python3 manage.py shell'

from employee_mgmt.models import Employee #import model
anything = Employee.objects.create(emp_name='anything', role=Employee.CEO) #creating CEO
userA = Employee.objects.create(emp_name='userA', role=Employee.MANAGER, manager=anything) #creating employee with his manager