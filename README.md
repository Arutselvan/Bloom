# Bloom

## Prerequisites
- Python3.x
- MySQL

## Build instructions
- Clone the repository
```
git clone https://github.com/Arutselvan/Bloom.git
cd Bloom
```
- Install requirements
```
pip install -r requirements.txt
```
- Setup database config
```
cp db.cnf.example db.cnf
```
- Create and run migrations
```
python manage.py makemigrations
python manage.py migrate
```
- Run the server
```
python manage.py runserver
```

