from app.createuserbot import test_login


def startbot():
    """
    This will msg every user in a sub if you havnt msged them before.
      It will avoid mods.  The username will be banned easily so create more bots!
    :return:
    """
    test_login.getauser()



startbot()