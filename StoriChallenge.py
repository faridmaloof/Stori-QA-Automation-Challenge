import argparse
import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

args = argparse.ArgumentParser()
args.add_argument('--browser', help='You can use Chrome, Firefox or Opera for the browser, ')
args = args.parse_args()
print(args.browser)


match args.browser:
    case "Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    case "Firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    case "Opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    case other:
        raise ValueError
driver.maximize_window()

# Open web Page
print('Scenario 1: Open web page')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Suggession country
try:
    print('Scenario 2: Select Country')
    driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("Me")
    time.sleep(2)
    driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")[5].click()
    print("\tResult [",datetime.datetime.now().time(),"]: Success")
except:
    print("\tResult [",datetime.datetime.now().time(),"]: Fail")

# Select option 2
try:
    print('Scenario 3: Select Option 2')
    x = driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")
    drop=Select(x)
    drop.select_by_visible_text("Option2")
    print("\tResult [",datetime.datetime.now().time(),"]: Success")
except:
    print("\tResult [",datetime.datetime.now().time(),"]: Fail")

time.sleep(2)

# Select option 2
try:
    print('Scenario 3: Select Option 3')
    x = driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")
    drop=Select(x)
    drop.select_by_visible_text("Option3")
    print("\tResult [",datetime.datetime.now().time(),"]: Success")
except:
    print("\tResult [",datetime.datetime.now().time(),"]: Fail")

time.sleep(2)

# Open new windows
#try:    
#    print('Scenario 4: Open new windows')
#    current = driver.current_window_handle
#    driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
#    for window_handle in driver.window_handles:
#        if window_handle != current:
#            driver.switch_to.window(window_handle)
#            break
#
#    driver.close()
#    driver.switch_to.window(current)
#except:
#    driver.close()
#    driver.switch_to.window(current)
#    print("\tResult [",datetime.datetime.now().time(),"]: Fail")
#    time.sleep(20)

# Switch tab
#try:    
#    print('Scenario 5: Switch tab')
#    currentTab = driver.current_window_handle
#    driver.find_element(By.CSS_SELECTOR, "#opentab").click()
#    for window_handle in driver.window_handles:
#        if window_handle != currentTab:
#            driver.switch_to.window(window_handle)
#            break
#    driver.close()
#    driver.switch_to.window(currentTab)
#except:
#    print("\tResult [",datetime.datetime.now().time(),"]: Fail")
#    time.sleep(20)

# Switch to alert
try:
    print('Scenario 6: Switch to alert')
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Stori Card")
    driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
    response = driver.switch_to.alert 
#    response.screenshot("switch_tab_example_01.png")
    print("\t\t the first message is: ",response.text)
    response.accept()
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Stori Card")
    driver.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
    response = driver.switch_to.alert
#    response.screenshot("switch_tab_example_02.png")
    if response.text == "Hello Stori Card, Are you sure you want to confirm?":
        print("\tResult [",datetime.datetime.now().time(),"]: Success, the message is: ", response.text)
        response.accept()
    else:
        print("\tResult [",datetime.datetime.now().time(),"]: Fail, the message is: ", response.text)
        response.dismiss()
except Exception as error:
    print("\tResult [",datetime.datetime.now().time(),"]: Fail by except", error)
    time.sleep(20)

# Web Table
try:
    print('Scenario 7: Find in table')
    for row in driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(5) > div:nth-child(1) > fieldset:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr"):
        if "Price" not in row.text:
            if "25" in row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text:                
                print("\t\tInstructor is :", row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text)
        
    print("\tResult [",datetime.datetime.now().time(),"]: Success")
        #print(row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text) 
        #if row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text == "25":
        #    print("\t\tInstructor is :", row.find_element(By.CSS_SELECTOR, "th:nth-child(1)").text)
except Exception as error:
    print("\tResult [",datetime.datetime.now().time(),"]: Fail by except ")

# Web Table Fixed
try:
    print('Scenario 8: Find in table fixed')
    for row in driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(5) > div:nth-child(2) > fieldset:nth-child(2) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr"):
        print("\t\tThe name is :", row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text)
        
    print("\tResult [",datetime.datetime.now().time(),"]: Success")
        #print(row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text) 
        #if row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text == "25":
        #    print("\t\tInstructor is :", row.find_element(By.CSS_SELECTOR, "th:nth-child(1)").text)
except Exception as error:
    print("\tResult [",datetime.datetime.now().time(),"]: Fail by except ", error)

# IFrame
try:
    print('Scenario 9: IFrame')
    driver.switch_to.frame('courses-iframe')
    record = 1
    strings = ""
    for row in driver.find_elements(By.XPATH, "//ul[@class='list-style-two']//li"):
        if record % 2 != 0:
            strings = strings+" "+row.text+"\n\t\t" 
        if "His mentorship program is most after in the software testing community with long waiting period." in row.text:
            print("\tResult [",datetime.datetime.now().time(),"]: Success, this message need show: ", row.text)
        record = record + 1
    print("\t\tThe other message in odd indexes are: \n\t\t",strings.rstrip().lstrip())
except Exception as error:
    print("\tResult [",datetime.datetime.now().time(),"]: Fail by except ", error)
