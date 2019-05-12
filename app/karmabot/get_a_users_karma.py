import praw
from app.createuserbot.models import Bots
import time
from app import session2

def getkarma():
    user = session2.query(Bots).all()
    for f in user:
        print("")
        print("")
        print("*" * 10)
        print("User: ", f.username)
        reddit = praw.Reddit(client_id=f.client_id,
                             client_secret=f.client_secret,
                             password=f.password,
                             user_agent="testing a script",
                             username=f.username)
        print(reddit.redditor(f.username).comment_karma)
        userskarma = (reddit.redditor(f.username).comment_karma)
        f.karma = userskarma
        session2.add(f)
        session2.commit()

        time.sleep(5)