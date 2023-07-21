from selenium import webdriver
import time

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

    driver.get("https://automated.pythonanywhere.com")
    return driver

# Function for clean the text
def clean_text(text):
    output = float(text.split(": ")[1])
    return output
 
# main
def main():
    driver = get_driver()
    time.sleep(2)
    
    element = driver.find_element(by="xpath",value = "/html/body/div[1]/div/h1[1]")

    getting_dynamic_value = driver.find_element(by="xpath",value = "/html/body/div[1]/div/h1[2]")
    return clean_text(getting_dynamic_value.text)

print(main())


    