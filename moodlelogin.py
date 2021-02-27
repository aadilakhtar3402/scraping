from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/login/index.php")

username = input("username: ")
password = getpass.getpass(prompt = "password")
user = driver.find_element_by_name("username")
user.send_keys(username)
pas = driver.find_element_by_name("password")
pas.send_keys(password)

t = driver.find_element_by_id ("login").text
a = ""
b = ""
c = 0

if(t.find("add") != -1):
    for i in t[t.find("add")+4::]:
       if (i.isdigit() == True):
           a = a + i
       else:
           break
    for i in t[t.find("add")+7::]:
        if(i.isdigit() == True):
           b = b + i
    c = int(a) + int(b)
elif (t.find("subtract") != -1):
    for i in t[t.find("subtract")+9::]:
       if (i.isdigit() == True):
           a = a + i
       else:
           break
    for i in t[t.find("add")+12::]:
        if(i.isdigit() == True):
           b = b + i
    c= int(a) - int(b)
elif (t.find("first") != -1):
    for i in t[t.find("first")+12::]:
       if (i.isdigit() == True):
           a = a+i
       else:
           break
    c = int(a)
else :
    for i in t[t.find("second")+16::]:
       if (i.isdigit() == True):
           a = a + i
    c = int(a)

user = driver.find_element_by_name("valuepkg3")
user.send_keys(c)

link = driver.find_element_by_id("loginbtn")
link.click()
