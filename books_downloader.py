from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tkinter import *
from tkinter import ttk


window =Tk()
window.title('Books downloader')
window.geometry('300x100')


title = ttk.Label(master=window, text='Enter the name of the book: ',font= 'calibri 15 bold')
title.pack()

var = StringVar()

input_frame = ttk.Frame(master= window)
entry=Entry(master=input_frame,textvariable=var)
button=ttk.Button(master=input_frame,text='Download',command=window.destroy)
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

window.mainloop()

name1 = var.get()
name = name1.title()


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://libgen.fun/")


driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="searchform"]').send_keys(name)
driver.find_element(By.XPATH,'/html/body/div/div[2]/form/input[2]').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME,'simplebooktitle').click()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, name[0:len(name)//3]).click()
time.sleep(1)
driver.find_element(By.ID,"download-button").click()
time.sleep(8)
driver.find_element(By.PARTIAL_LINK_TEXT,"Save").click()




