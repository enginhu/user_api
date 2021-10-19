## A Simple User Management API

Download the repo and navigate to root folder.
```bash
    git clone https://github.com/enginhu/user_api.git
    cd user_api
```

Create a virtual Environment, activate it and install packages from `requirements.txt`

```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

**Make Migrations**
```bash
    python manage.py makemigrations
    python manage.py migrate
```


**Run the app**
```bash
    python manage.py runserver
```

## Endpoints

*You can make requests with Postman*

**Login** 
```
Method: POST
http://localhost:8000/login/
requires username and password, returns an auth token.
```

**Register** 
```
Method: POST
http://localhost:8000/register/
requires username, email, password, password2, first_name and last_name
```

**Logout** 
```
Method: POST
http://localhost:8000/logout/
requires to be logged in.
```

**Profile**
```
Method: GET
http://localhost:8000/profile/<int:pk>/
<int:pk> is user ID.
requires to be logged in. User can display only his/her own profile.
superusers can display all profiles.

Example: http://localhost:8000/profile/2/ 
Displays the details of user with id 2
```

**Users List**
```
Method: GET
http://localhost:8000/users/
Displays a list of registered users.
requires to be a superuser and logged in.
```

**Change Password**
```
Method: PUT
http://localhost:8000/change_password/<int:pk>/ 
<int:pk> is user ID.
requires old_password, password and password2. 

Example: http://localhost:8000/change_password/2/ 
changes the password of user with id 2

```
**Update Profile** 
```
Method: PUT
http://localhost:8000/update_user/<int:pk>/
<int:pk> is user ID.
requires username, email, first_name and last_name

Example: http://localhost:8000/change_password/2/ 
Updates the details of user with id 2
```
