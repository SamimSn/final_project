# Setup :
### cd final_project
### my_env\Scripts\activate
### pip install -r requirements.txt
### cd TaskManagement
### python manage.py migrate
### python manage.py createsuperuser
### python manage.py runserver

<br>

# Test :
### cd TaskManagement
### python manage.py test

<br>

# Explanation :
- This is a simple TODOList web application which implemenets the CRUD operations.
- My design would be based on the Django.generic veiws, however the project wanted me to use rest_framework. So I used it as much as I could.
- I have implemented user registration as well to make the project more user-friendly.
- I built two API endpoints as the instruction wanted me to.
- create_time and update_time are two additional Task fields.
- styling of UI pages is done via bootstrap
- created tests.py for create/list/detail/update
