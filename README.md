# Indo-Singapore Hack 2018
## NTU, Singapore

## Prerequisites
- Python3.x
- MySQL

## Build instructions
- Clone the repository
```
git clone git@github.com:coderick14/indo-singapore-hack.git
cd indo-singapore-hack
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

