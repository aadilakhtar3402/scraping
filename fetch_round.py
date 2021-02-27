from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from PIL import ImageGrab

PATH = "C:\\Program Files (x86)\\geckodriver.exe"
driver = webdriver.Firefox(executable_path = PATH)


contest_no = input("Enter contest number ")
link = "https://codeforces.com/contest/" + contest_no + "/problems"
driver.get(link)

os.mkdir("D:/DevClub/scraping/"+contest_no)

q = driver.find_elements_by_class_name("problemindexholder")
for i in q :
    t = i.get_attribute("problemindex")
    os.mkdir("D:/DevClub/scraping/"+contest_no+"/"+t)
    ss = i.find_element_by_class_name("problem-statement")
    ss.screenshot("D:/DevClub/scraping/"+contest_no+"/"+t+"/problem.png")
    s = i.find_elements_by_class_name("input")
    r = i.find_elements_by_class_name("output")
    u = 1
    v = 1
    for j in s:
        f1 = open("D:/DevClub/scraping/"+contest_no+"/"+t+"/input"+str(u)+".txt","w+")
        i3 = j.find_element_by_class_name("title").find_element_by_class_name("input-output-copier")
        i1 = i3.get_attribute("data-clipboard-target")
        i2 = i1[1:]
        inputtext = j.find_element_by_id(i2).text
        f1.write(inputtext)
        f1.close()
        u = u+1
    for l in r:
        f2 = open("D:/DevClub/scraping/"+contest_no+"/"+t+"/output"+str(v)+".txt","w+")
        o3 = l.find_element_by_class_name("title").find_element_by_class_name("input-output-copier")
        o1 = o3.get_attribute("data-clipboard-target")
        o2 = o1[1:]
        outputtext = l.find_element_by_id(o2).text
        f2.write(outputtext) 
        f2.close() 
        v = v+1
driver.quit()   
    
