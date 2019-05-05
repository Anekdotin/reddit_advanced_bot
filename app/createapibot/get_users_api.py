from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from app import session2
from app.createuserbot.models import Bots
import random
from selenium.webdriver.common.action_chains import ActionChains


def main():

    prawsite = "https://praw.readthedocs.io/en/latest/"
    thename = ["Clever app",
               "Mr Bot",
               "HArvbard comp Science rules",
               "NYU student",
               "Russian Bot",
               "F Facebook",
               "Reddit master",
               "Reddit and praw",
               "Learning to spider",
               "Info gather",
               ]

    randomname = random.choice(thename)

    thedescription = ["testing for school",
                      "dsfafasdfdasfsad",
                      "project for fun",
                      "bored at work fun",
                      "4235dfssdaf",
                      "why do i need this",
                      "????",
                      "bot program, to analyze people",
                      "nltk theory",
                      "random stuff",
                      "description"
                      ]

    randomdescription = random.choice(thedescription)

    theabouturl = prawsite
    theredirection = prawsite




    print("1")
    ## basic selenium
    options = Options()
    options.headless = True
    options.add_argument("-private")

    driver = webdriver.Firefox(options=options, executable_path="/home/bot/reddit/venv/lib/python3.5/geckodriver")
    driver.set_window_size(1280, 850)

    try:
        driver.get('https://www.reddit.com/login?dest=https%3A%2F%2Fwww.reddit.com%2F')

    except Exception as e:
        print(str(e))
        driver.save_screenshot('error-pic-connection.png')
    print("2")


    ## query db and get users without an api
    user = session2.query(Bots).filter_by(client_id="").first()

    try:
        ## LOGIN
        # get the form
        form = driver.find_element_by_class_name("AnimatedForm")
        #login to form
        username = form.find_element_by_id("loginUsername")
        username.clear()
        username.send_keys(user.username)
        password = form.find_element_by_id("loginPassword")
        password.clear()
        password.send_keys(user.password)
        submit = form.find_element_by_class_name("AnimatedForm__submitButton")
        submit.click()
        time.sleep(3)
    except Exception as e:
        print(str(e))
        driver.save_screenshot('error-pic-loginform.png')
    print("3")



    try:
        ## GO TO APP
        # go back to reddit
        driver.get('https://www.reddit.com/prefs/apps')
        time.sleep(6)
        form_button = driver.find_element_by_class_name("edit-app-form")
        driver.implicitly_wait(5)
        ActionChains(driver).move_to_element(form_button).click(form_button)
        time.sleep(2)
        driver.save_screenshot("pic-01.png")
    except Exception as e:
        print(str(e))
        driver.save_screenshot('error-pic-editbutton.png')
    print("4")



    ## FILL OUT APP
    #fill out the form
    try:
        get_creeate_app_button = driver.find_element_by_xpath('//*[@id="create-app-button"]')

        print(get_creeate_app_button)
        get_creeate_app_button.click()
        time.sleep(2)
        driver.save_screenshot("pic-011.png")
    except Exception as e:
        print(str(e))
        driver.save_screenshot('error-pic-createappbutton.png')
    print("5")


    try:
        gettable = driver.find_element_by_class_name("preftable")
        driver.implicitly_wait(5)
        ActionChains(driver).move_to_element(gettable)
        time.sleep(2)
        # add the name of the app
        nameinput = gettable.find_element_by_name("name")
        nameinput.send_keys(randomname)
        # description
        descripinput = gettable.find_element_by_name("description")
        descripinput.send_keys(randomdescription)
        # check script button
        scriptbutton = gettable.find_element_by_id("app_type_script")
        scriptbutton.click()
        driver.save_screenshot("pic-22.png")
        # about url
        aboutinput = gettable.find_element_by_name("about_url")
        aboutinput.send_keys(theabouturl)
        # redirect url
        redirectinput = gettable.find_element_by_name("redirect_uri")
        redirectinput.send_keys(theredirection)
        #create app button
        driver.save_screenshot("pic-33.png")
        thebutton = gettable.find_elements_by_xpath("//button[contains(text(), 'create app')]")
        #thebutton = gettable.find_elements_by_xpath('/html/body/div[3]/div[2]/form/button')
        for f in thebutton:
            f.click()
            print(f)
        print(thebutton)
        #thebutton.click()
    except Exception as e:
        print(str(e))
        driver.save_screenshot('error-pic-apiform.png')
    print("6")



    #after it saves..go back in and get our info
    driver.save_screenshot("pic-4.png")
    ##SAVE TO DB
    user.client_id = ""
    user.client_secret = ""
    user.user_agent = ""
    user.appname = ""

    session2.add(user)
    session2.commit()




    driver.quit()


