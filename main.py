from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions
import time, pyautogui as pya, keyboard, random

webdriver_location="msedgedriver.exe"
options=EdgeOptions()
options.use_chromium=True
options.binary_location=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
browser=Edge(options=options,executable_path=webdriver_location)
running=False

keybind=input("\n\n\n[!!] -Start typeing keybind, press on start of test: ")

while True:
     try:
          if keyboard.is_pressed(keybind) == True and running == False:
               browser.get("https://www.typing.com/student/typing-test/1-minute")
               runningEFE=True
               newtype=""
               typestring=[]
               print('-Reading...')
               elements=browser.find_elements_by_class_name('screenBasic-letter')
               print("-Typing...")
               for e in elements:
                    text=e.get_attribute("textContent")
                    print(text)
                    if "\xa0" in text:
                         text=str(text).replace("\xa0"," ")
                    if "\n" in text:
                         text=str(text).replace("\n"," ")
                    typestring.append(text)
               for c in typestring:
                    newtype=str(newtype)+str(c)
               time.sleep(0.1)
               body=browser.find_element_by_xpath('/html/body')
               body.send_keys(str(newtype))
               print(str(newtype))
               runningEFE=False
               print("-Ready!")
     except Exception as e:
          print("-Error occured: "+str(e))
