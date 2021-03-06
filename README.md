# JANJ-Activity-Tracker-Server
The backend was made with [Django](https://www.djangoproject.com/)

# Deployment
https://helper-haven-backend.herokuapp.com/

# Setting up the backend
- Ensure you have python3 installed on your machine
- Set up python virtual environment
    - Run pip3 install -r requirements.txt
    - Run python3 manage.py makemigrations 
    - Run python3 manage.py migrate

# Running the backend
- Run python3 manage.py runserver

The backend must be running in order to access it through the API endpoints

# API Endpoints

<h3>
/register/
</h3>

[POST] 
<br>
```
{
    "email": "< user email >",
    "role": "< VOLUNTEER or ORGANIZATION >",
    "username": "< same as email >",
    "password": "< user password  >",
    "password2": "< user password (same as other password field) >"
}
```
<br>
Returns token

<h3>
/login/
</h3>

[POST] 
<br>
```
{
    "username": "< user email (username) >",
    "password": "< user password  >"
}
```
<br>
Returns token

<h3>
account/< email >/
</h3>

[GET] 
<br>
<br>
Returns the profile of the user:
<br>
```
{
    "id": "< user id >",
    "role": "< VOLUNTEER or ORGANIZATION >",
    "email": "< user email >"
}
```

<h3>
edit-account/< email >/
</h3>

[PATCH] 
<br>
<br>
Edits existing user profile (body includes any fields to be modified)

<h3>
volunteer/< email >/
</h3>

[GET] 
<br>
<br>
Returns the volunteer profile of the user:
<br>
```
{
    "first_name": "< first name of volunteer >",
    "last_name": "< last name of volunteer >",
    "email": "< volunteer email (relate to account) >",
    "gender": "< volunteer gender >",
    "dob": "< YYYY-MM-DD >",
    "address": "< volunteer address >",
    "city": "< volunteer city >",
    "state": "< volunteer state >",
    "zip": "< volunteer zip code >",
    "skills": "< list of skills and corresponding levels >",
    "link": "< social media links >"
}
```

<h3>
edit-volunteer/< email >/
</h3>

[PATCH] 
<br>
<br>
Edits existing volunteer profile (body includes any fields to be modified)


<h3>
/log/add/
</h3>

[POST] 
<br>
```
{
    "user_email": "< user email >",
    "event_name": "< string event name >",
    "role": "< describe volunteer role >",
    "hours": "< string >",
    "comments": "< string >"
}
```
<br>
Posts a new entry in the log

<h3>
/log/all/
</h3>

[GET] 
<br>
Gets all of the entries in the log

<h3>
/log/< user_email >/
</h3>

[GET] 
<br>
<br>
Gets entry in the log by specifying user's email (currently case sensitive). Put the actual email in place of "user_email" above.

<h3>
/events/
</h3>

[POST] 
<br>
```
{
    "event_name": "< name of event >",
    "org_name": "< name of organization creating event >",
    "org_email": "< email to identify organization >",
    "contact_name": "< name of point of contact for event >",
    "contact_email": "< email to contact for more info >",
    "contact_number": "< phone number to call for more info >",
    "event_summary": "< summary of event >",
    "role_description": "< description of volunter/participation role >",
    "max_hours": < maximum number of volunteer hours >,
    "date": "< day(s) event is taking place >",
    "time": "< time of day of the event >",
    "location": "< specify physical location or if event is virtual >",
    "link": "< link for more info / registration >",
    "active": "< boolean - true if students can continue to log hours for this event >",
    "upcoming": "< boolean - true if volunteering registration still open for event >",
    "skills": "< prefered skills for volunteers to have >"
}
```
<br>
Creates new event (admin)
<br>
<br>
    
[GET]
<br>
<br>
Get list of all events


