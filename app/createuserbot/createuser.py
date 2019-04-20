from app import session2
from app.createuserbot.models import Bots
import string
import random


def create_email(chars=string.ascii_uppercase + string.digits):
    thesize = random.randint(12, 22)
    return ''.join(random.choice(chars) for _ in range(thesize))


def create_password(chars=string.ascii_uppercase + string.digits):
    thesize = random.randint(20, 30)
    return ''.join(random.choice(chars) for _ in range(thesize))


def addtodatabase_manually():
    """
    Add a bot to the database manually after you visit reddit
    """
    new_person = Bots(username='rundsafdsas',
                      password='redditmanredditman',
                      appname='dssadfdshgjj',
                      client_id='q8oX8unzP9EjfA',
                      client_secret='1y7e4V2jV8Nt5AmF5umHy01t9js',
                      user_agent='dsafsadf',
                      )
    session2.add(new_person)
    session2.commit()

