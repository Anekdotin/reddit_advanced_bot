
import praw
from app.karmabot.models import Bots
from app.intelbot.models import FunnyStuff, FoodStuff
from app import session
from sqlalchemy import func
import random
import time


subs = ['funny', 'food', 'pizza', 'sushi']

"""
Finds a random user then adds a comment to the top 5 posts
"""


def addcomment(sub, post):
    if sub == 'food' or sub == 'pizza' or sub == 'sushi':
        getquote = session.query(FoodStuff).order_by(func.rand()).first()

        print("sub", sub)
        try:
            post.reply(str(getquote.comment))
        except:
            pass
        print(getquote.comment)
        print("added comment ..")
    elif sub == 'funny':
        getquote = session.query(FunnyStuff).order_by(func.rand()).first()

        print(getquote.id)
        try:
            post.reply(str(getquote.comment))
        except Exception as e:
            print("str(e")
            pass
        print(getquote.comment)
        print("added comment ..")
    else:
        print("failue")
        pass


def main():
    user = session.query(Bots).order_by(func.rand()).first()
    print("*" * 10)
    print("User: ", user.username)
    reddit = praw.Reddit(client_id=user.clientid,
                         client_secret=user.clientsecret,
                         password=user.password,
                         user_agent=user.useragent,
                         username=user.username)

    subz = random.choice(subs)
    submissions = reddit.subreddit(subz).hot(limit=5)

    for s in submissions:
        if s.stickied:
            continue
        else:
            print(s.title)
            addcomment(post=s, sub=subz)
            time.sleep(500)





