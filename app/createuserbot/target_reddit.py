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
PRIVATE = False

''' You'll need to update based on the coordinates of your setup '''
# open firefox
FIREFOX_ICON_COORDS = (1135, 1970)  # Location of the Firefox icon on the side toolbar (to left click)
PRIVATE_COORDS = (1221, 1876)  # Location of "Open a new Private Window"
NON_PRIVATE_COORDS = (1183, 1849)  # Location of "Open a new regular Window"
PRIVATE_BROWSER = (1472, 1333)  # A place where the background of the Private Window will be
PRIVATE_COLOR = '#25003E'  # The color of the background of the Private Window

# navigate to reddit signupusers
REDDIT_FAV_BUTTON = (1245, 1012)  # Location of the Firefox Search box
SIGNUP_BUTTON = (2815, 1050)  # The button on reddits front page
EMAIL_INPUT = (1855, 1457)  # The input for email
EMAIL_BUTTON = (1879, 1524)  # The input for email
CAPTCHA_COORDS = (1716, 1528)  # Coordinates of the empty CAPTCHA checkbox
CHECK_COORDS = (1717, 1532)  # Location where the green checkmark will be
CHECK_COLOR = '#35B178'  # Color of the green checkmark
AUDIO_COORDS = (1820, 1738)  # Location of the Audio button
AUDIO_CLOSE_CORDS = (657, 78)  # Location of the Audio button
DOWNLOAD_COORDS = (1886, 1576)  # Location of the Download button
FINAL_COORDS = (1836, 1535)  # Text entry box
VERIFY_COORDS = (1806, 1575)  # Verify button

# user info
USERNAME_ON_SIDE = (2137, 1436)  # the username input
USERNAME_INPUT = (1864, 1374)  # the username input
RIGHT_CLICK_COPY = (1916, 1430)  # the username input
PASSWORD_INPUT = (1735, 1443)  # the password input
NEXT_BUTTON = (2382, 1735)  # the finish button


CLOSE_LOCATION = (2989, 9149)



DOWNLOAD_LOCATION = "/home/droid/Downloads/"
''' END SETUP '''

r = sr.Recognizer()


def runCommand(command):
    """
    Run a command and get back its output
    """

    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return proc.communicate()[0].split()[0]


def waitFor(coords, color):
    """
    Wait for a coordinate to become a certain color
    """
    pyautogui.moveTo(coords)
    numWaitedFor = 0
    while color != runCommand(
            "eval $(xdotool getmouselocation --shell); xwd -root -silent | convert xwd:- -depth 8 -crop \"1x1+$X+$Y\" txt:- | grep -om1 '#\w\+'"):
        time.sleep(.1)
        numWaitedFor += 1
        if numWaitedFor > 25:
            return -1
    return 0


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

    print("seeing the color ...")
    pyautogui.moveTo(CHECK_COORDS)
    thecolor = runCommand(
        "eval $(xdotool getmouselocation --shell); xwd -root -silent | convert xwd:- -depth 8 -crop \"1x1+$X+$Y\" txt:- | grep -om1 '#\w\+'")
    print("Color: ", thecolor)
    if CHECK_COLOR in str(thecolor):
        print("theres the color..it let us in")
        return newemail, 1
    else:
        print("Didnt auto pass..going for audio challenge")
        pyautogui.moveTo(AUDIO_COORDS)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(DOWNLOAD_COORDS)
        pyautogui.click()
        time.sleep(3)
        return newemail, 2


def checkCaptcha():
    """
    Check if we've completed the captcha successfully.
    """
    print("seeing the color ...")
    pyautogui.moveTo(CHECK_COORDS)
    thecolor = runCommand(
        "eval $(xdotool getmouselocation --shell); xwd -root -silent | convert xwd:- -depth 8 -crop \"1x1+$X+$Y\" txt:- | grep -om1 '#\w\+'")
    print("Color: ", thecolor)
    if CHECK_COLOR in str(thecolor):
        print("theres the color..it let us in")
        output = 1
    else:
        print("Process failed ....")
        output = 0

    return output


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
    addtodatabase(username=founduser, password=newpassword, appname='', client_id='', client_secret='', user_agent='', email=useremail)


def addtodatabase(username, password, appname, client_id, client_secret, user_agent, email):

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


def runcap():
    try:
        # These files may be left over from previous runs, and should be removed just in case.
        print("Removing old files...")
        os.system(
            'rm ./audio.wav 2>/dev/null')
        os.system('rm ' + DOWNLOAD_LOCATION + 'audio.mp3 2>/dev/null')

        # First, download the file
        useremail, downloadresult = downloadcaptcha()

        # if it just let us in
        if downloadresult == 1:
            print("downloadresult is 1")
            # create username pass, get api
            get_a_user(useremail=useremail)

            result = checkCaptcha()
            return result

        # if it wanted to do captcha
        elif downloadresult == 2:
            # Convert the file to a format our APIs will understand
            print("Converting Captcha...")
            os.system("echo 'y' | ffmpeg -i " + DOWNLOAD_LOCATION + "audio.mp3 ./audio.wav 2>/dev/null")
            with sr.AudioFile('./audio.wav') as source:
                audio = r.record(source)

            print("Submitting To Speech to Text:")
            determined = google(audio)  # Instead of google, you can use ibm or bing here
            print(determined)

            print("Inputting Answer")
            # Input the captcha
            pyautogui.moveTo(FINAL_COORDS)
            pyautogui.click()
            time.sleep(.5)
            pyautogui.typewrite(determined, interval=.15)
            time.sleep(.5)
            pyautogui.moveTo(VERIFY_COORDS)
            pyautogui.click()

            print("Verifying Answer")
            time.sleep(2)

            # Check that the captcha is completed
            result = checkCaptcha()

            # create username pass, get api
            get_a_user(useremail=useremail)

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
    fail = 0
    allowed = 0
    botted = 0
    # Run this forever and print statistics

    resultofcaptcha = runcap()
    if resultofcaptcha == 1:
        success += 1
    elif resultofcaptcha == 2:  # Sometimes google just lets us in
        allowed += 1
    elif resultofcaptcha == 3:  # Sometimes google just lets us in
        botted += 1
    elif resultofcaptcha == 4:  # Sometimes google just lets us in
        fail += 1
    else:
        fail += 1

    print("SUCCESSES: " + str(success) + " FAILURES: " + str(fail) + " Allowed: " + str(allowed), " Botted: " + str(botted))

    # move to next
    pyautogui.moveTo(NEXT_BUTTON)
    pyautogui.click()
    time.sleep(8)

    pyautogui.moveTo(CLOSE_LOCATION)
    pyautogui.click()
