# from main import app
# from models.models import db , User 
# from sqlalchemy.exc import IntegrityError


# db.create_all(app=app)


# user = User(username='Jerry868', email='jerry868@gmail.com')
# user.set_password('password')

# try:
#   db.session.add(user)
#   db.session.commit() 
#   print('\n\n\n\t\tJerry868 has beeen created')
  
# except IntegrityError:
#   db.session.rollback()
#   print("\n\n\nUser already exists")

from main import app
from models.models import db , User, Log 
from sqlalchemy.exc import IntegrityError


db.create_all(app=app)

#CREATE USER ACCOUNTS (RUN 'python3 initDB.py')
user = User(id=1, username='Jerry868', email='jerry868@gmail.com')
user.set_password('password')
print(user.toDict())

user2 = User(id=2, username='Tamika', email='Tamika@gmail.com')
user2.set_password('password')
print(user2.toDict())
user3 = User(id=3, username='Anthony', email='Anthony@gmail.com')
user3.set_password('password')

user4 = User(id=4, username='Emily', email='Emily@gmail.com')
user4.set_password('password')

user5 = User(id=5, username='Zane', email='Zane@gmail.com')
user5.set_password('password')

text_entry= 'extracted from the planets surface...😎'

#Sample logs
userLog= Log(id=1,  author= user.username, topic= "Cosmic dust and meteorites", text_entry = text_entry, sample_type= 'grey extraterrestrial rock', hardware_used= 'hammer' )

userLog2= Log(id=2,  author= user2.username, topic= "Cosmic dust and meteorites", text_entry = text_entry, sample_type= 'brown extraterrestrial rock', hardware_used= 'hammer' )

userLog3= Log(id=3,  author= user3.username, topic= "Cosmic dust and meteoritesn", text_entry = text_entry, sample_type= 'grey extraterrestrial rock', hardware_used= 'hammer' )

userLog4= Log(id=4,  author= user4.username, topic= "Cosmic dust and meteorites", text_entry = text_entry, sample_type= 'meteorite containing extraterrestrial ribose', hardware_used= 'hammer' )

userLog5= Log(id=5,  author= user5.username, topic= "Cosmic dust and meteorites", text_entry = text_entry, sample_type= 'meteorite containing extraterrestrial ribose', hardware_used= 'hammer' )
try:
  db.session.add(user)
  #db.session.commit()
  print(user.username)

  db.session.add(user2)
  db.session.commit()
  print(user2.username)

  db.session.add(user3)
  db.session.commit()
  print(user3.username)

  db.session.add(user4)
  db.session.commit()
  print(user4.username)

  db.session.add(user5)
  


  db.session.add(userLog)
  db.session.add(userLog2)
  db.session.add(userLog3)
  db.session.add(userLog4)
  db.session.add(userLog5)

  db.session.commit() 
  
  print('\n\n\n\t\tUser accounts created for: {}, {}, {}, {}, {}  '.format(user.username, user2.username, user3.username, user4.username, user5.username ))
  
except IntegrityError:
  db.session.rollback()
  print("\n\n\nUser already exists")
