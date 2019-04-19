import time
import pyautogui
import speech_recognition as sr
import os
import subprocess

from app.createuserbot.query_api import bing, google, ibm
from app.createuserbot.createuser import create_email, create_password
from app import session2
from app.createuserbot.models import Bots
from app.createuserbot.get_clipboard import getClipboardData
from app.createuserbot.get_cords import cords

PRIVATE = False

''' You'll need to update based on the coordinates of your setup '''
download_location = "/home/bot/Downloads/"
pycharm_location = "/home/bot/.PyCharm2016.1/config/jdbc-drivers/"

r = sr.Recognizer()
# open firefox
FIREFOX_ICON_COORDS = (44, 154)  # Location of the Firefox icon on the side toolbar (to left click)
PRIVATE_COORDS = (1221, 1876)  # Location of "Open a new Private Window"
NON_PRIVATE_COORDS = (119, 181)  # Location of "Open a new regular Window"
PRIVATE_BROWSER = (96, 206)  # A place where the background of the Private Window will be
PRIVATE_COLOR = '#25003E'  # The color of the background of the Private Window

# navigate to reddit signupusers
REDDIT_FAV_BUTTON = (164, 108)  # Location of the Firefox Search box
SIGNUP_BUTTON = (1263, 152)  # The button on reddits front page
EMAIL_INPUT = (581, 460)  # The input for email
EMAIL_BUTTON = (606,552)  # The button for email
CAPTCHA_COORDS = (429, 530)  # Coordinates of the empty CAPTCHA checkbox
CHECK_COORDS = (429, 530)  # Location where the green checkmark will be
CHECK_COLOR = '##FFFFFF'  # Color of the green checkmark
CHECK_COLOR2 = '#007840'  # another color i got
CHECK_COLOR3 = '#3CB47C'  # another color i got

# the audio button
AUDIO_COORDS = (540, 732)  # Location of the Audio button
AUDIO_CLOSE_CORDS = (657, 78)  # Location of the Audio button
DOWNLOAD_COORDS = (592, 610)  # Location of the Download button
OK_RIGHTCLICK_BUTTON_COORDS = (656, 700)  # Location of the ok/save button for right click Download button
CLOSE_TAB_BUTTON_COORDS = (276, 88)  # Location of the tab to close for Download
VERIFY_COORDS = (664, 647)  # Verify button

# the username entry
USERNAME_ON_SIDE = (938, 366)  # the username input
USERNAME_INPUT = (515, 384)  # the username input
RIGHT_CLICK_COPY = (561, 453)  # the username input
PASSWORD_INPUT = (520, 455)  # the password input

#closeup and next
NEXT_BUTTON = (1107, 741)  # the finish button
FINAL_COORDS = (531, 536)  # Text entry box
CLOSE_LOCATION = (16, 10)

''' END SETUP '''


def checkcaptcha():
    """
    Check if we've completed the captcha successfully.
    """
    print("seeing the color ...")
    pyautogui.moveTo(CHECK_COORDS)
    thecolor = runcommand(
        "eval $(xdotool getmouselocation --shell); xwd -root -silent | convert xwd:- -depth 8 -crop \"1x1+$X+$Y\" txt:- | grep -om1 '#\w\+'")
    print("Color: ", thecolor)
    if CHECK_COLOR in str(thecolor)\
            or CHECK_COLOR2 in str(thecolor)\
            or CHECK_COLOR3 in str(thecolor):
        print("theres the color..it let us in")
        output = 1
    else:
        print("Process failed ....")
        output = 0

    return output


def runcommand(command):
    """
    Run a command and get back its output
    """

    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return proc.communicate()[0].split()[0]


def waitfor(coords, color):
    """
    Wait for a coordinate to become a certain color
    """
    pyautogui.moveTo(coords)
    numWaitedFor = 0
    while color != runcommand(
            "eval $(xdotool getmouselocation --shell); xwd -root -silent | convert xwd:- -depth 8 -crop \"1x1+$X+$Y\" txt:- | grep -om1 '#\w\+'"):
        time.sleep(.1)
        numWaitedFor += 1
        if numWaitedFor > 25:
            return -1
    return 0


def get_a_user(useremail):
    # move to username on side...reddit makes this
    print("Entering a Username..")
    pyautogui.moveTo(USERNAME_ON_SIDE)
    pyautogui.click()
    time.sleep(1)
    # copy that new username for database
    pyautogui.moveTo(USERNAME_INPUT)
    pyautogui.doubleClick()
    time.sleep(0.3)
    pyautogui.rightClick()
    time.sleep(0.3)
    pyautogui.moveTo(RIGHT_CLICK_COPY)
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.3)
    founduser = getClipboardData()
    founduser = str(founduser)
    print("Username:", founduser)

    # move to password
    print("Entering a Password..")
    pyautogui.moveTo(PASSWORD_INPUT)
    pyautogui.click()
    time.sleep(1)
    randompassword = create_password()
    newpassword = str(randompassword)
    print("Password: ", newpassword)
    pyautogui.typewrite(newpassword, interval=0.5)

    # create the user even tho no api..incase rest fails
    addtodatabase(username=founduser,
                  password=newpassword,
                  appname='',
                  client_id='',
                  client_secret='',
                  user_agent='',
                  email=useremail)


def addtodatabase(username,
                  password,
                  appname,
                  client_id,
                  client_secret,
                  user_agent,
                  email):

    new_person = Bots(username=username,
                      password=password,
                      appname=appname,
                      client_id=client_id,
                      client_secret=client_secret,
                      user_agent=user_agent,
                      user_email=email,
                      )
    session2.add(new_person)
    session2.commit()
    print("successfully committed")


def downloadcaptcha():
    """
    Navigate to demo site, input user info, and download a captcha.
    """
    pyautogui.FAILSAFE = False
    print("Opening Firefox")
    pyautogui.moveTo(FIREFOX_ICON_COORDS)
    pyautogui.rightClick()
    time.sleep(.3)

    if PRIVATE is True:
        pyautogui.moveTo(PRIVATE_COORDS)
        pyautogui.click()
        time.sleep(5)
    else:
        pyautogui.moveTo(NON_PRIVATE_COORDS)
        pyautogui.click()
        time.sleep(5)

    print("Visiting Reddit..")
    pyautogui.moveTo(REDDIT_FAV_BUTTON)
    pyautogui.click()
    time.sleep(6)

    print("Create a new account..")
    pyautogui.moveTo(SIGNUP_BUTTON)
    pyautogui.click()
    time.sleep(7)

    print("Entering an Email..")
    pyautogui.moveTo(EMAIL_INPUT)
    pyautogui.click()
    time.sleep(5)
    randomemail = create_email()
    newemail = str(randomemail) + "@gmail.com"
    print("User email: ", newemail)
    pyautogui.typewrite(newemail)
    pyautogui.moveTo(EMAIL_BUTTON)
    pyautogui.click()
    time.sleep(8)

    print("clicking captcha")
    pyautogui.moveTo(CAPTCHA_COORDS)
    pyautogui.click()
    time.sleep(10)

    thecolor = checkcaptcha()


    if thecolor == 1:
        print("theres the color..it let us in")
        return newemail, 1
    elif thecolor == 0 :
        # go to audio button
        print("Didnt auto pass..going for audio challenge")
        pyautogui.moveTo(AUDIO_COORDS)
        current_cords = cords()
        print(current_cords)
        pyautogui.click()
        time.sleep(2)

        #left click download
        pyautogui.moveTo(DOWNLOAD_COORDS)
        pyautogui.rightClick()
        time.sleep(3)

        # move to save link as..when you right click
        pyautogui.moveTo(OK_RIGHTCLICK_BUTTON_COORDS)
        pyautogui.click()
        time.sleep(3)
        # move to save link as..when you right click

        # just press enter when the new popup opens
        pyautogui.press("enter")

        # CLOSE the new tab
        pyautogui.moveTo(CLOSE_TAB_BUTTON_COORDS)
        pyautogui.click()
        time.sleep(3)

        return newemail, 2
    else:
        # found out a bot
        return newemail, 3


def removeoldfile():

    # These files may be left over from previous runs,
    # and should be removed just in case.
    print("Removing old files...")
    try:
        os.system('rm ' + download_location + 'audio.wav')
    except:
        pass
    try:

        os.system('rm ' + download_location + 'audio.mp3')
    except:
        pass
    try:
        os.system('rm ' + pycharm_location + 'audio.mp3')
    except:
        pass


def convertfile():
    print("Converting Captcha...")
    # it downloaded to weird location
    os.rename("/home/bot/.PyCharm2016.1/config/jdbc-drivers/audio.mp3", "/home/bot/Downloads/audio.mp3")
    # after it downloads to folder..convert it for google to a .wav
    os.system("ffmpeg -i " + download_location + "audio.mp3 " + download_location + "audio.wav")
    #arch = subprocess.check_output("ffmpeg -i " + download_location + "audio.wav", shell=True)
    #print(arch)
    print("converte?")
    with sr.AudioFile(download_location + 'audio.wav') as source:
        audio = r.record(source)

    print("Submitting To Speech to Text:")
    determined = google(audio)
    # Instead of google, you can use ibm or bing here
    print("Text from google says ..:", determined)

    return str(determined)


def runcap():
    try:
        # remove old file
        removeoldfile()
        # get the download file
        useremail, downloadresult = downloadcaptcha()

        # if it just let us in
        if downloadresult == 1:
            print("downloadresult is 1")
            # create username pass, get api
            get_a_user(useremail=useremail)

            result = checkcaptcha()
            return result

        # if it wanted to do captcha
        elif downloadresult == 2:

            # Convert the file to a format our APIs will understand
            findthetext = convertfile()

            print("Inputting Answer")
            # Input the captcha
            pyautogui.moveTo(FINAL_COORDS)
            pyautogui.click()
            time.sleep(.5)
            pyautogui.typewrite(findthetext, interval=.15)
            time.sleep(.5)
            pyautogui.moveTo(VERIFY_COORDS)
            pyautogui.click()

            print("Verifying Answer")
            time.sleep(2)

            # Check that the captcha is completed
            result = checkcaptcha()

            # create username pass, get api
            get_a_user(useremail=useremail)

            # move to next to save to reddit
            pyautogui.moveTo(NEXT_BUTTON)
            pyautogui.click()
            time.sleep(8)

            # close out finally
            pyautogui.moveTo(CLOSE_LOCATION)
            pyautogui.click()

            return result
        else:
            result = 3
            print("found out im a bot ..beep beep")
            return result

    except Exception as e:
        print(str(e))
        result = 4
        print("found out im a bot ..beep beep")
        return result


def main():
    success = 0
    allowed = 0
    botted = 0
    fail = 0
    # Run this forever and print statistics

    resultofcaptcha = runcap()
    if resultofcaptcha == 1: # Sometimes google just lets us in
        success += 1
    elif resultofcaptcha == 2:  # had to do recapthca
        allowed += 1
    elif resultofcaptcha == 3:  # it knew we botted
        botted += 1
    elif resultofcaptcha == 4:  # error in code
        fail += 1
    else:
        fail += 1

    print(" SUCCESSES: " + str(success) +
          " Allowed: "   + str(allowed) +
          " Botted: "    + str(botted) +
          " Failed: "    + str(fail)
          )

