from app.karmabot import randomcomments


def randomcommentbot():
    """
    This will build user rep over time..put it on a cron
    :return:
    """
    randomcomments.main()


randomcommentbot()

