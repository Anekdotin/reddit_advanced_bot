from app.createapibot import get_users_api


def startbot():
    """
    This will msg every user in a sub if you havnt msged them before.
      It will avoid mods.  The username will be banned easily so create more bots!
    :return:
    """
    get_users_api.main()



startbot()