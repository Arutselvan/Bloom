# Bloom

An effective learning portal based on Bloom's taxonomy. Won 2nd place in Singapore - India Hackathon 2018

## Features
- QA forum with auto tagging of topics
- Identification of weak and strong areas based on questions asked and answered by the user.
- Speech to text input for logging notes/doubts from a lecture
- OCR for notes/documents
- A neuro linguistic processing engine to tag topics, to summarize the concepts in the form of knowledge graphs and recommendation of prerequisites/related topics with links to resources

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

