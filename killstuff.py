from subprocess import Popen, PIPE, STDOUT

def killprocess():

    cmdcreatewallet = ["killall", "-9", "firefox"]
    proc = Popen(cmdcreatewallet, stdout=PIPE, stderr=STDOUT, universal_newlines=False)
    verify = proc.communicate()[0].decode('utf-8').strip()
    print(verify)

killprocess()