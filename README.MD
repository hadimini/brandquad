1. Setup env
* ```python3 -m venv venv```
    
2. activate
* ```source ./venv/bin/activate```

4. install requirements
* ```pip3 install -r ./requirements.py```

4. cd backend

5. Migrate:
* ```./manage.py migrate```
 
5. Create Admin
* ```./manage.py createsuperuser```

6. Run server
* ```./manage.py runserver```


Import data:
* ```../manage.py import_data --url <URL>```


Browse api:

*```localhost:8000/api/```

Swagger: 

*```localhost:8000/swagger/```

Tests:

*```pytest```