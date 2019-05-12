
import praw
from app.createuserbot.models import Bots
from app.intelbot.models import FunnyStuff, FoodStuff
from app import session, session2
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
        except Exception as e:
            print(str(e))
            pass
        print("Comment: ", getquote.comment)
        print("")

    elif sub == 'funny':
        getquote = session.query(FunnyStuff).order_by(func.rand()).first()
        print(getquote.id)
        try:
            post.reply(str(getquote.comment))
        except Exception as e:
            print(str(e))
            pass
        print("Comment: ", getquote.comment)

    else:
        print("No Sub Found")
        pass


def main():
    user = session2.query(Bots).filter(Bots.client_id != "").order_by(func.rand()).first()
    print("")
    print("")
    print("*" * 10)
    print("User: ", user.username)
    reddit = praw.Reddit(client_id=user.client_id,
                         client_secret=user.client_secret,
                         password=user.password,
                         user_agent=user.user_agent,
                         username=user.username)

    subz = random.choice(subs)
    submissions = reddit.subreddit(subz).hot(limit=2)

    for s in submissions:
        if s.stickied:
            continue
        else:
            print("Title: ", s.title)
            addcomment(post=s, sub=subz)

            currentcount = user.post_count
            newcount = int(currentcount) + 1
            user.post_count = newcount
            print("new user post count: ", newcount)
            session2.add(user)
            session2.commit()
            print("")
            time.sleep(500)





