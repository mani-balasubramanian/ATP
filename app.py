import tkinter as tk
from tkinter import *

def header():
  w = 800 # width for the Tk root
  h = 650 # height for the Tk root

  # get screen width and height
  ws = root.winfo_screenwidth() # width of the screen
  hs = root.winfo_screenheight() # height of the screen

  # calculate x and y coordinates for the Tk root window
  x = (ws/2) - (w/2)
  y = (hs/2) - (h/2)

  # set the dimensions of the screen 
  # and where it is placed
  root.geometry('%dx%d+%d+%d' % (w, h, x, y))
  root.title("Airlines Booking")
  title = tk.Label(root, text="Airlines Ticket Booking", font=('verdana', 24, 'normal'), pady=2, bd=12, bg="blue", fg="white")
  title.pack(fill=X)

def login_page():
  for widget in F1.winfo_children():
      widget.destroy() 
  F1.configure(text='Login')
  F1.place(relx=.5, rely=.5, anchor=CENTER)

  username_lbl = Label(F1, text="Username:", width=30)
  username_txt = Entry(F1, width=30, textvariable=v_login_username)
  pwd_lbl = Label(F1, text="Password:")
  pwd_txt = Entry(F1, width=30, show="*", textvariable=v_login_pwd)
  login_btn = Button(F1, text="Login",  width=10,command=main_page)
  register_btn = Button(F1, text="Cancel",  width=10, command=registration_page)

  username_lbl.grid(row=0, column=0, padx=20, pady=5)
  username_txt.grid(row=0, column=1, pady=5, padx=10)
  pwd_lbl.grid(row=1, column=0, padx=20, pady=5)
  pwd_txt.grid(row=1, column=1, pady=5, padx=10)
  login_btn.grid(row=2, column=0, pady=5, padx=10)
  register_btn.grid(row=5, column=1, pady=5, padx=10)
  

def registration_page(): 
  for widget in F1.winfo_children():
      widget.destroy()  
  F1.configure(text='Registration')
  F1.place(relx=.5, rely=.5, anchor=CENTER)
  
  username_lbl = Label(F1, text="Username:", width=30)
  username_txt = Entry(F1, width=30, textvariable=v_reg_username)
  pwd_lbl = Label(F1, text="Password:")
  pwd_txt = Entry(F1, width=30, show="*", textvariable=v_reg_pwd)
  phone_lbl = Label(F1, text="Phone:")
  phone_txt = Entry(F1, width=30, textvariable=v_reg_phone)
  add_lbl = Label(F1, text="Address:")
  add_txt = Entry(F1, width=30, textvariable=v_reg_add)
  email_lbl = Label(F1, text="Eamil:")
  email_txt = Entry(F1, width=30, textvariable=v_reg_email)

  username_lbl.grid(row=0, column=0, padx=20, pady=5)
  username_txt.grid(row=0, column=1, pady=5, padx=10)
  pwd_lbl.grid(row=1, column=0, padx=20, pady=5)
  pwd_txt.grid(row=1, column=1, pady=5, padx=10)
  phone_lbl.grid(row=2, column=0, padx=20, pady=5)
  phone_txt.grid(row=2, column=1, pady=5, padx=10)
  add_lbl.grid(row=3, column=0, padx=20, pady=5)
  add_txt.grid(row=3, column=1, pady=5, padx=10)
  email_lbl.grid(row=4, column=0, padx=20, pady=5)
  email_txt.grid(row=4, column=1, pady=5, padx=10)

  register_btn = Button(F1, text="Cancel",  width=10, command=register_page)
  register_btn.grid(row=5, column=1, pady=5, padx=10)

  cancel_btn = Button(F1, text="Cancel",  width=10, command=login_page)
  register_btn.grid(row=5, column=1, pady=5, padx=10)

def register_page():
  

def main_page():

root = tk.Tk()
v_login_username = StringVar()
v_login_pwd = StringVar()
v_reg_username = StringVar()
v_reg_pwd = StringVar()
v_reg_phone = StringVar()
v_reg_add = StringVar()
v_reg_email = StringVar()
F1 = LabelFrame(root, font=('verdana', 12))

header()
login_page()

root.mainloop()
