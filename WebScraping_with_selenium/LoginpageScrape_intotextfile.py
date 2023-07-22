from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def get_driver():
    # Set options to make browsing easier
    options =  webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

# Function for clean the text
def clean_text(text):
    output = float(text.split(": ")[1])
    return output

#//*[@id="id_username"]
def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    driver.find_element(by="id",value = "id_password").send_keys("automatedautomated" + Keys.RETURN)

    time.sleep(2)
    #/html/body/nav/div/a
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    #print(driver.current_url)
    time.sleep(2)
    text = driver.find_element(by="xpath",value = "/html/body/div[1]/div/h1[2]").text

    return clean_text(text)

print(main())