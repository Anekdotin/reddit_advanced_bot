from app import session
from app.intelbot.models import FunnyStuff, FoodStuff
import praw



"""
This script will get the comments from various subs
It puts them in respective tables
"""


subs = ['funny', 'food', 'pizza', 'sushi']

banstuff = ['**', 'http', '**',
            '/r', 'r/', '/R',
            'removed', '[removed]',
            'ban', '[deleted]', 'fuck',
            "FUCK", 'Fuck']


def addcomment(sub, comment):

    try:
        if sub == 'food' or sub == 'pizza' or sub == 'sushi':
            addcommentfood = FoodStuff(comment=comment)
            session.add(addcommentfood)
            session.commit()
            print("added to food")
        elif sub == 'funny':
            addcomment = FunnyStuff(comment=comment)
            session.add(addcomment)
            session.commit()
            print("added to funny")

        else:
            pass
    except Exception as e:
        print("Error")
        print(str(e))
        print("")
        session.rollback()
        pass


def main():

    username = 'redbeerdawg12'
    reddit = praw.Reddit(client_id='vJYSY6c--NRTTQ',
                         client_secret='x2JaRHC4HgzgiYmaCHMRioBrO-o',
                         password='richardnixon1975',
                         user_agent='crawling every day',
                         username=username)
    for sub in subs:

        subreddit = reddit.subreddit(sub)
        submissions = subreddit.hot(limit=100)

        for submission in submissions:
            print(submission)
            try:
                for comment in submission.comments:
                    if len(comment.body) <= 50:
                        if comment.body in banstuff:
                            pass
                        else:
                            x = comment.body

                            addcomment(sub=sub,
                                       comment=x)

            except Exception as e:
                print("Error")
                print(str(e))
                print("")
                pass


main()
