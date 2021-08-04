# Bloom

An effective learning portal based on Bloom's taxonomy. Won 2nd place in Singapore - India Hackathon 2018
https://www.youtube.com/watch?v=nHmCC767CxE

## Features
- QA forum with auto tagging of topics
- Identification of weak and strong areas based on questions asked and answered by the user.
- Speech to text input for logging notes/doubts from a lecture
- OCR for notes/documents
- A NLP engine to tag topics, to summarize the concepts in the form of knowledge graphs and recommendation of prerequisites/related topics with links to resources

## Screenshots
![Screenshot (2)](https://user-images.githubusercontent.com/18646185/87219754-af707d00-c37b-11ea-92b4-a33b98d580d5.png)
![Screenshot (10)](https://user-images.githubusercontent.com/18646185/87219750-ada6b980-c37b-11ea-8b64-8de3a2ab70a9.png)

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

