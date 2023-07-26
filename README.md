# Build a Flask app with a Postgres database.

Your app should be able to do all the CRUD Actions: create, read, update, delete.

## Planning:

Plan 2 models with a One-Many relationship.
Keep it simple to begin with!

Draw class diagrams for the models (don't worry about methods).

Draw what the models would look like as tables in the database. Which are the Primary Keys? Where does the Foreign Key go?

Plan your pages using wireframes.

Plan your Restful Routes:

|VERB  |PATH                    |ACTION |
|:----:|:----------------------:|:-----:|
|GET   |/tasks                  |index  |
|GET   |/tasks/:id             |show   |
|POST  |/tasks                  |create |
|POST  |/tasks/:id             |update |
|POST  |/tasks/:id/delete      |destroy|

Optional ones for displaying forms:
|VERB  |PATH                    |ACTION |
|:----:|:----------------------:|:-----:|
|GET   |/tasks/new              |new    |
|GET   |/tasks/:id/edit        |edit   |



## Set up a Flask app:

A boilerplate app might look like:


```python
# .flaskenv

FLASK_APP=app.py
FLASK_DEBUG=true
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=4999
```

```python
# app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "This is the home page!"
```

`flask run` and check you can see the message on this route.

Bring in SQLAlchemy, Migrate, and configure the app: 

```python
# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://user@localhost:5432/tasks_app"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

Write your models:
```python
models.py

from app import db

class MyClass(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  ...
```

Create your database from your terminal:

```
createdb db_name
```

Initialize the migration folder with:

```
flask db init
```

Migrate and Update (like stage and commit) your database changes:

```
flask db migrate
flask db upgrade
```

Check in your GUI or `psql` that the tables have been created correctly.

Enter some data directly into your database, so you have some data to work with.

Begin working through **one route at a time** in your `controllers` folder and create the relavent `templates` (base + block content). Maybe start with a home page for the route `"/"`.

Don't forget to import and register your blueprints in `app.py`!