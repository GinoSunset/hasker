Hasker
==============
It's copy site Stackoverflow with API

Requrements
--------------
* Python 3.7
* Django >= 3

How run
-------------
Whrite `secret_key` in compose
Run in docker:
```shell script
docker-compoer run python manage.py migrate
docker-compose up
```


* Clone repo
* install requirements
```shell script
pip install -r requirements.txt
```
* setup db
```shell script
mange.py migrate
```
* run django service
```shell script
manage.py rnuserver
```

To run test:
-------------------
* install selenium driver for firefox
* run pytest
```shell script
pytest -v
```

Web demo
------------
application will be available in page heroku by url:  https://hasker-simon.herokuapp.com
