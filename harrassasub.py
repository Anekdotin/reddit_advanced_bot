from app.workbot import msg_for_agorabit


def startbot():
    """
    This will msg every user in a sub if you havnt msged them before.
      It will avoid mods.  The username will be banned easily so create more bots!
    :return:
    """
    x = msg_for_agorabit.main()
    x()


startbot()