# Flask Mailroom Application

Running at http://flask-mailroom-navid.herokuapp.com

## What I did



What I did:

1. Add a page with a form for Login form.

2. Add navigation elements in `base.jinja2` to the top of both pages. 

3. Add Sign up form to add new user

4. Add the form for all users that can ask to show only single user donations

5. Only user who logged in can add donation.

6. Publish my work to Heroku. 

7. For all forms I used falsk form to create them which is more powerful than html form.

8. Add logout

9. When user logged in the signup form should not be shown

10. The create form to add donation just show up when the user logged in

11. Logged in user's username has been shwoing up in the up right corner

The application is running on port 5000. open your browser and then open your browser to (http://localhost:5000)

## To Publish to Heroku

All commands to be run from inside the repository directory.
```
$ git init                # Only necessary if this is not already a git repository
$ heroku create
$ heroku config:set SECRET_KEY=KjJPe35tQKY2YLRzm7vhm3aJdqqh8YHR(This Key is sample key, you can make any key that you want and use it in your machine and heroku environemtn)
$ pip install gunicorn psycopg2-binary(make sure that these two modules has been installed)
$ pip freeze > requirements.txt(make sure that you make a list of your installed packages in requirements.txt")
$ echo "web: gunicorn main:app" > Procfile  (You need to create Procfile in your text editor and just add a single line: "web: gunicorn main:app")
$ git add .; git commit -a -m "Initial commit"          ## Only necessary because this is a new git repo. # If you have any changes or files to add, commit them before you push.
$ git push heroku master  # If you have any changes or files to add, commit them before you push. 
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku run python setup.py
$ heroku open
```

what else need to do:

1- Add forget password form
2- If password is forgotten, reset a pass word.



