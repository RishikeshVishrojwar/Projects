from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


number =['1234567890']



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()



def fancode(num):
    driver.get("https://www.fancode.com/login")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[2]/div[3]/div[1]/input').send_keys(num)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[2]/div[3]/div[1]/button').click()
    time.sleep(1)

def ullu(num):
    driver.get("https://ullu.app/#/login")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="mat-input-0"]').send_keys(num)
    driver.find_element(By.XPATH,'//*[@id="app-mat-drawer-content"]/div[2]/app-auth/div/div/div/div/div/div[3]/button').click()
    time.sleep(1)

def housing(num):
    driver.get("https://seller.housing.com/user-login?redirectTo=%2Fdashboard")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app-root"]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/input').send_keys(num)
    driver.find_element(By.XPATH,'//*[@id="app-root"]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/button').click()
    time.sleep(1)

# housing(num)

def rummy(num):
    driver.get("https://www.rummycircle.com/")
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="mobile_input"]').send_keys(num)
    driver.find_element(By.XPATH,'//*[@id="getStarted"]').click()
    time.sleep(2)

for i in range(60):
    for num in number:
        rummy(num)
        fancode(num)
        # ullu(num)
        housing(num)






