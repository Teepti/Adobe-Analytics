from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import time
import collections

def register(driver):
        #maximizing window
        driver.maximize_window()
        #Applying implicit wait
        driver.implicitly_wait(1000)
        #create instance of Actionchains to do mouse and keyboard events
        action = ActionChains(driver)
        #Navigating to URL
        driver.get("http://otsuka:Site123!@rexultihcc20q2covidpostlaunch.test-otsuka.acsitefactory.com/")
        #Steps to do for Registration process
        driver.find_element_by_class_name("block-covid19localsiteblock2-modal-close").click()
        firstLevelMenu = driver.find_element_by_id("header_Registration")
        action.move_to_element(firstLevelMenu).perform()
        driver.find_element_by_xpath("//*[@id='block-mainnavigation']/ul/li[5]/ul/li[1]/a").click()
        #driver.implicitly_wait(10)
        driver.find_element_by_class_name("block-covid19localsiteblock2-modal-close").click()
        element = driver.find_element_by_class_name("option")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        driver.find_element_by_id("otsuka_sign_up_form_submit").click()
        driver.execute_script("window.scrollTo(0,1893);")
        driver.find_element_by_name("firstName").send_keys("gfgj")
        driver.find_element_by_name("lastName").send_keys("gfgj")
        driver.find_element_by_name("email").send_keys("gfgj@klh.com")
        driver.find_element_by_name("emailConfirm").send_keys("gfgj@klh.com")
        ele1 = driver.find_element_by_class_name("option")
        driver.execute_script("arguments[0].scrollIntoView();", ele1)
        ele1.click()
        driver.find_element_by_id("otsuka_sign_up_form_submit").click()
        changed_url = driver.current_url
        wait = WebDriverWait(driver,20)
        wait.until(EC.url_changes(changed_url))
        