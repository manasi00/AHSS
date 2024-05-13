# Guardian360

Clone the repo
```
git clone https://github.com/manasi00/AHSS.git
```

cd into repo
```
cd AHSS
```

Run Once
----
Create virtual environment
```
python -m venv ahss0001
```

Activate virtual environment
----
```
Set-ExecutionPolicy Unrestricted -Scope Process
./ahss0001/Scripts/activate
```

Install requirements
----
```
pip install ultralytics

pip install deepface

pip install opencv-python

pip install numpy

pip install django

pip install email
```

Run Migrations
----
```
python manage.py makemigrations
python manage.py migrate

python manage.py makemigrations accounts
python manage.py migrate accounts
```


Open 3 terminal in code editor and activate virtual environment by this command
----
```
Set-ExecutionPolicy Unrestricted -Scope Process
./ahss0001/Scripts/activate
```

In first terminal run django
----
```
python manage.py runserver
```

In second terminal run detect.py
----
```
python inference/detect.py
```

In third terminal run find.py
----
```
python inference/find.py
```



----
----
----
Now your app is up and running



