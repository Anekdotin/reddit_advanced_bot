

from datetime import datetime
import praw
from app.intelbot.models import WhoMSg
from app import session


now = datetime.utcnow()

# pick a username to spam with
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')

thesubs = ['localbitcoins']


# agorabit messaging
the_message = 'add a message to spam' \



subject = 'hey man'
#

modlist = []
getwork = 1
verbose = 1
howmany = 1


def addthebot(subreddit, username, datestamp):
    imsged = WhoMSg(datestamp=datestamp,
                    subreddit=subreddit,
                    username=username,
                    )

    session.add(imsged)
    session.commit()


def sendauthormsg(submission, sub):
    if verbose == 1:
        print('Author: ', submission.author)

    if getwork == 1:
        dothework_noloop(f=submission, sub=sub)


def printheader(submission, sub):
    if verbose == 1:
        print('')
        print(20 * '#')
        print('sub:', sub)
        print('Title: {},'
              ' ups: {},'
              ' downs: {},'
              ' subid: {}'.format(submission.title,
                                  submission.ups,
                                  submission.downs,
                                  submission.id))
        print("Author: ", submission.author)

        print(20 * '#')


def printcomments(submission, sub):
    comments = submission.comments

    for f in comments:
        if verbose == 1:
            print(10 * '**')
            print('Author:', f.author)
            print('Parent ID:', f.parent())
            print('Comment ID:', f.id)

        if getwork == 1:
            dothework(f, sub=sub)
            getcomments(comment=f, sub=sub)


def getcomments(comment, sub):

        for f in comment.replies:
            if verbose == 1:
                print('REPLY:')
                print(f.author)

            if getwork == 1:
                dothework(f, sub=sub)


def dothework_noloop(f, sub):
    if verbose == 1:
        if f.author in modlist:
            print(20 * '!')
            print(f.author)
            print(20 * '!')
    if getwork == 1:
        seeifuser = session.query(WhoMSg).filter_by(username=str(f.author)).first()
        if seeifuser is None:
            print("no user..proceeding to add", f.author)
            addthebot(datestamp=str(now), subreddit=str(sub), username=str(f.author))
            print("MSG SENT")
            send_msg(reddituser=f.author, msg=the_message, thesubject=subject)
            print("")
        else:
            print("Exists. Not adding to db:", seeifuser.username)
            pass


def dothework(f, sub):
    if f.author in modlist:
        if verbose == 1:
            print(20 * '!')
            print(f.author)
            print(20 * '!')
    if getwork == 1:
        seeifuser = session.query(WhoMSg).filter_by(username=str(f.author)).first()
        if seeifuser is None:
            print("no user..proceeding to add")
            addthebot(datestamp=str(now), subreddit=str(sub), username=str(f.author))
            send_msg(reddituser=f.author, msg=the_message, thesubject=subject)
        else:
            print("Exists. Not adding to db:", seeifuser.username)
            pass


def send_msg(reddituser, msg, thesubject):
    struser = str(reddituser)
    strmsg = str(msg)
    strsubj = (str(thesubject))

    reddit.redditor(struser).message(strsubj, strmsg)
    if verbose == 1:
        print("Sent messge:", struser)


def main():
    for sub in thesubs:
        subreddit = reddit.subreddit(sub)
        hot = subreddit.hot(limit=howmany)

        for moderator in reddit.subreddit(sub).moderator():
            modlist.append(moderator)

        if getwork == 0:
            print("Status: Gathering Intel..")
        else:
            print("Status: Work Enabled. Perming botting...")

        for submission in hot:
            if not submission.stickied:
                printheader(submission=submission, sub=sub)
                sendauthormsg(submission=submission, sub=sub)
                printcomments(submission=submission, sub=sub)
                print('')
                print('')
                print('')

main()
