from app import session2, session
from app.intelbot.models import FunnyStuff, FoodStuff
from app.createuserbot.models import Bots
import praw


"""
This script will get the comments from various subs
It puts them in respective tables
"""


subs = ['funny', 'food', 'pizza', 'sushi']

banstuff = ['**', 'http', '**',
            '/r', 'r/', '/R',
            '/u', 'u/', '/user',
            'removed', '[removed]',
            'ban', '[deleted]', 'fuck',
            "FUCK", 'Fuck']


def addcomment(sub, comment):

    try:
        if sub == 'food' or sub == 'pizza' or sub == 'sushi':
            addcomment_food = FoodStuff(comment=comment)
            session.add(addcomment_food)
            session.commit()

        elif sub == 'funny':
            addcomment_funny = FunnyStuff(comment=comment)
            session.add(addcomment_funny)
            session.commit()
        else:
            pass
    except Exception as e:
        print("Error")
        print(str(e))
        print("")
        session.rollback()
        pass


def main():
    user = session2.query(Bots).filter_by(id=4).first()
    reddit = praw.Reddit(client_id=user.client_id,
                         client_secret=user.client_secret,
                         password=user.password,
                         user_agent=user.user_agent,
                         username=user.username)
    for sub in subs:
        subreddit = reddit.subreddit(sub)
        submissions = subreddit.hot(limit=1)
        for submission in submissions:
            try:
                for comment in submission.comments:
                    if len(comment.body) <= 50:
                        if comment.body in banstuff or comment.body.startswith("r/") or comment.body.startswith("/r"):
                            pass
                        else:
                            x = comment.body
                            addcomment(sub=sub, comment=x)

            except Exception as e:
                print("Error")
                print(str(e))
                print("")
                pass


main()
