# test task library

## precondition
an empty PostgreSQL database named "library" deployed to localhost:5432

## install requirements:
    pip install -r requirements.txt

## init db
    python manage.py init
    
## run service
    python manage.py runserver
    
# Usage
open in browser:    
    http://127.0.0.1:8000/writers/<id>    
    (e.g. 1, 2, 3)  
    http://127.0.0.1:8000/books/<id>
    
python console:

    import requests
    requests.get('http://127.0.0.1:8000/writers/<id>')
    
command line:
    
    pip install --upgrade httpie
    http http://127.0.0.1:8000/writers/<id>
    
    