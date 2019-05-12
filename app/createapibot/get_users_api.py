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



    ## query db and get users without an api
    user = session2.query(Bots).filter_by(client_id="").first()
    print("user", user)
    if user is not None:

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
            # driver.save_screenshot('error-pic-connection.png')

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
            #driver.save_screenshot('login-success.png')
            time.sleep(5)
        except Exception as e:
            print(str(e))
            session2.delete(user)
            session2.commit()
            #driver.save_screenshot('error-pic-loginform.png')


        try:
            ## GO TO APP
            # go back to reddit
            driver.get('https://www.reddit.com/prefs/apps')
            time.sleep(6)
            form_button = driver.find_element_by_class_name("edit-app-form")
            driver.implicitly_wait(5)
            ActionChains(driver).move_to_element(form_button).click(form_button)
            #driver.save_screenshot('apspage-success.png')
            time.sleep(2)
        except Exception as e:
            print(str(e))
            #driver.save_screenshot('error-pic-editbutton.png')
            session2.delete(user)
            session2.commit()

        ## FILL OUT APP
        #fill out the form
        try:
            get_creeate_app_button = driver.find_element_by_xpath('//*[@id="create-app-button"]')
            get_creeate_app_button.click()
            time.sleep(2)
        except Exception as e:
            print(str(e))
            #driver.save_screenshot('error-pic-createappbutton.png')


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
            # about url
            aboutinput = gettable.find_element_by_name("about_url")
            aboutinput.send_keys(theabouturl)
            # redirect url
            redirectinput = gettable.find_element_by_name("redirect_uri")
            redirectinput.send_keys(theredirection)
            #create app button
            thebutton = gettable.find_elements_by_xpath("//button[contains(text(), 'create app')]")
            for f in thebutton:
                f.click()

        except Exception as e:
            print(str(e))
            #driver.save_screenshot('error-pic-apiform.png')

        ##SAVE TO DB
        try:
            # secret
            get_secret_text = driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li/div[4]/div[1]/form/table/tbody/tr[1]/td')
            thetextofsecret = get_secret_text.text
            user.client_secret = str(thetextofsecret)

            # client id
            get_id_ofapp = driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li/div[2]/h3[2]')
            get_id_ofapptext = get_id_ofapp.text
            user.client_id = str(get_id_ofapptext)

            # client agent is crawler and ai of username
            user.user_agent = ""

            user.appname = randomname

            session2.add(user)
            session2.commit()
            print("api added")
            print("user: ", user.username)
            print("user secret: ", user.client_secret)
            print("user id: ", user.client_id)
        except Exception as e:
            print(str(e))
            #driver.save_screenshot('error-get-secret-and-id.png')

        driver.quit()

    else:
        pass

