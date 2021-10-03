from main import app
from models.models import db , User 
from sqlalchemy.exc import IntegrityError


db.create_all(app=app)


user = User(username='Jerry868', email='jerry868@gmail.com')
user.set_password('password')

try:
  db.session.add(user)
  db.session.commit() 
  print('\n\n\n\t\tJerry868 has beeen created')
  
except IntegrityError:
  db.session.rollback()
  print("\n\n\nUser already exists")