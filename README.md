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
```

Run Migrations
----
```
python migrate.py makemigrations
python migrate.py migrate

python migrate.py makemigrations frontend
python migrate.py migrate frontend

python migrate.py makemigrations inference
python migrate.py migrate inference

python migrate.py makemigrations accounts
python migrate.py migrate accounts
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



