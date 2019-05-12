from app.karmabot import get_a_users_karma


def startbot():
    """
    This will msg every user in a sub if you havnt msged them before.
      It will avoid mods.  The username will be banned easily so create more bots!
    :return:
    """
    get_a_users_karma.getkarma()



startbot()