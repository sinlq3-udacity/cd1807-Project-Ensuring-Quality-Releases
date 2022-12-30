# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time

# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    # options = ChromeOptions()
    # options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys(user)
    driver.find_element(By.CSS_SELECTOR,"#password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,"#login-button").click()
    #driver.find_element(By.CSS_SELECTOR, ".nav")
    driver.find_element( By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()    
    driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR,"#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)").click()
    total = driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge").text
    assert total=="6"
    print('added total 6 items to cart')
    time.sleep(5)
    driver.find_element( By.CSS_SELECTOR,"#remove-sauce-labs-backpack").click()    
    driver.find_element(By.CSS_SELECTOR,"#remove-sauce-labs-bike-light").click()
    driver.find_element(By.CSS_SELECTOR,"#remove-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR,"#remove-sauce-labs-fleece-jacket").click()
    driver.find_element(By.CSS_SELECTOR,"#remove-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR,"#remove-test\.allthethings\(\)-t-shirt-\(red\)").click()
   
    total = driver.find_element(By.CSS_SELECTOR,".shopping_cart_link").text
    assert total==""
    print('removed total 6 items to cart')
    time.sleep(5)
    print ('Closing the browser...')

login('standard_user', 'secret_sauce')


