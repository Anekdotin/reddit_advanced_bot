from app import session2
from app.karmabot.models import Bots


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

