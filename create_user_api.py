from app.createapibot import get_users_api

from subprocess import Popen, PIPE, STDOUT

def killprocess():

    cmdcreatewallet = ["killall", "-9", "firefox"]
    proc = Popen(cmdcreatewallet, stdout=PIPE, stderr=STDOUT, universal_newlines=False)
    verify = proc.communicate()[0].decode('utf-8').strip()
    print(verify)



def startbot():
    """
    This will msg every user in a sub if you havnt msged them before.
      It will avoid mods.  The username will be banned easily so create more bots!
    :return:
    """
    get_users_api.main()


killprocess()
startbot()
killprocess()