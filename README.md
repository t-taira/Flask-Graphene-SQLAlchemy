# Flask-Graphene-SQLAlchemy

https://github.com/alexisrolland/flask-graphene-sqlalchemy/wiki/Flask-Graphene-SQLAlchemy-Tutorial


# setup
```
pipenv install
pipenv run python setup.py
```

# run
```
pipenv run python app.py
```

Access http://localhost:5000/graphql

## query

```
{
  employeeList{
    edges{
      node{
        name
        role {
          name
        }
        department{
          name
        }
      }
    }
  }
}
```
