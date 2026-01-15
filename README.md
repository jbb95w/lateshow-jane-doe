# Late Show API

This project is a Flask REST API for a Late Show system.  
It manages episodes, guests, and appearances.

## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Run migrations
5. Seed the database
6. Start the server

## Commands

Install dependencies:
pip install -r requirements.txt

Run migrations:
flask --app server.app db upgrade

Seed the database:
python -m server.seed

Run the server:
flask --app server.app run

## Routes

GET /episodes  
GET /episodes/<id>  
GET /guests  
POST /appearances

## Technologies Used

- Python
- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite
- Postman

## Author
jabirrr