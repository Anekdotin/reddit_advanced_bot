from app.workbot import upvoteBot


def upvote_comment():
    """
    If you want to upvote a specific post
    set number of upvotes. Dont be greedy
    has timer
    Add sub id
    :return:
    """
    x = upvoteBot.main(number=1, submissionid='7xbrcw')
    return x


upvote_comment()
