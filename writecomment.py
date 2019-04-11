from app.workbot import commentbot


def writecomment():
    """
    This will write a comment on a specific post
    Add a msg and the sub id
    :return:
    """
    x = commentbot.main(msg='your msg here ',
                        submissionid='7yyczx')
    return x


writecomment()
