from threading import Thread
import spam

import re
import tkinter as tk
import tkinter as font
from tkinter import *
from tkinter import ttk
import requests
import json
import os
import math

import time
from plyer import notification



def kanryo(text,title):
    notification.notify(
        title=title,
        message=text,
        app_name="BoxFreshSpammer",
        app_icon=resource_path("aaa.ico"),
        timeout=6
    )








import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)





mein = tk.Tk()
mein.title("BoxFreshSpammer Developed by Kodai.")
mein.configure(background='white')
mein.geometry("450x250")
mein.iconbitmap(default=resource_path("aaa.ico"))
#mein.iconbitmap('main.ico')
id_stringvar = StringVar()
id_entry = ttk.Entry(
      mein,
      textvariable=id_stringvar,
      width=20)
id_entry.place(x = 10, y = 100)

content_stringvar = StringVar()
content_entry = ttk.Entry(
      mein,
      textvariable=content_stringvar,
      width=20)
content_entry.place(x = 170, y = 100)

def run_msg():
  kurikaeshi=0
  whi_data=math.floor(int(vl.get()))
  if vl.get()==0.0:
    whi_data=1
  while kurikaeshi!=whi_data:
    status=spam.send(id_entry.get(),content_entry.get())
    time.sleep(0.3)
    kurikaeshi+=1
    if status!="成功":
      return
  kanryo("完了しました。","スパム完了")
  

def run_thread():
  t = Thread(target=run_msg)
  t.start()


replace_lavel = tk.Label(mein, font = ("Yu Gothic UI Semibold", 18), text = "メッセージ内容", fg = 'black', bg = '#ffffff')
replace_lavel.place(x = 160, y = 56)
kaisu_lavel = tk.Label(mein, font = ("Yu Gothic UI Semibold", 19), text = "1", fg = 'black', bg = '#ffffff')
kaisu_lavel.place(x = 140, y = 189)


vl = DoubleVar()
kais = ttk.Scale(
    mein,
    variable=vl,
    orient=HORIZONTAL,
    length=120,
    from_=1,
    to=20,
    command=lambda e: kaisu_lavel.configure(text=math.floor(int(vl.get())))
)
kais.place(x=10,y=200)
 
#Replacer
replacer_ddd = tk.Button(mein, text = "Run!", bg = 'red', fg = '#ffffff',command=run_thread)
replacer_ddd.place(x =310, y = 97)
replacer_ddd.bind(run_thread)
replace_lavel = tk.Label(mein, font = ("Yu Gothic UI Semibold", 19), text = "相手のID", fg = 'black', bg = '#ffffff')
replace_lavel.place(x = 15, y = 56)
replace_lavela = tk.Label(mein, font = ("Yu Gothic UI Semibold", 19), text = "回数", fg = 'black', bg = '#ffffff')
replace_lavela.place(x = 34, y = 155)

#main
title_label = tk.Label(mein, font = ("Yu Gothic UI Semibold", 20), text = "BoxFreshSpammer", fg = 'green', bg = '#ffc038')
title_label.place(x = 10, y = 5)

tk.mainloop()
