import tkinter as tk
from tkinter import *
import mysql.connector
import configparser

def header():
  w = 600 # width for the Tk root
  h = 400 # height for the Tk root

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
  login_btn = Button(F1, text="Login",  width=10,command=menu_page)
  register_btn = Button(F1, text="Register",  width=10, command=registration_page)

  username_lbl.grid(row=0, column=0, padx=20, pady=5)
  username_txt.grid(row=0, column=1, pady=5, padx=10)
  pwd_lbl.grid(row=1, column=0, padx=20, pady=5)
  pwd_txt.grid(row=1, column=1, pady=5, padx=10)
  login_btn.grid(row=2, column=0, pady=5, padx=10)
  register_btn.grid(row=2, column=1, pady=5, padx=10)
  

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
  register_btn = Button(F1, text="Register",  width=10, command=submit_registration)
  cancel_btn = Button(F1, text="Cancel",  width=10, command=login_page)

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

  register_btn.grid(row=5, column=0, pady=5, padx=10)
  cancel_btn.grid(row=5, column=1, pady=5, padx=10)

def menu_page():
  for widget in F1.winfo_children():
    widget.destroy()  
  F1.configure(text='Menu')
  F1.place(relx=.5, rely=.5, anchor=CENTER)
  
  booking_btn = Button(F1, text="Book Ticket",  width=50, command=search_flights,font=('verdana', 10))
  history_btn = Button(F1, text="View Bookings",  width=50, command=submit_registration,font=('verdana', 10))
  passenger_btn = Button(F1, text="Add Passengers",  width=50, command=add_passenger,font=('verdana', 10))
  exit_btn = Button(F1, text="Exit",  width=50, command=login_page,font=('verdana', 10))

  booking_btn.grid(row=0, column=0, pady=5, padx=10)
  history_btn.grid(row=1, column=0, pady=5, padx=10)
  passenger_btn.grid(row=2, column=0, pady=5, padx=10)
  exit_btn.grid(row=3, column=0, pady=5, padx=10)

def add_passenger():
  for widget in F1.winfo_children():
    widget.destroy()  
  F1.configure(text='Add Passenger')
  F1.place(relx=.5, rely=.5, anchor=CENTER)
  
  fn_lbl = Label(F1, text="First Name:", width=30)
  fn_txt = Entry(F1, width=30, textvariable=v_pax_fn)
  ln_lbl = Label(F1, text="Last Name:")
  ln_txt = Entry(F1, width=30, show="*", textvariable=v_pax_ln)
  phone_lbl = Label(F1, text="Phone:")
  phone_txt = Entry(F1, width=30, textvariable=v_pax_phone)
  add_lbl = Label(F1, text="Address:")
  add_txt = Entry(F1, width=30, textvariable=v_pax_add)
  email_lbl = Label(F1, text="Eamil:")
  email_txt = Entry(F1, width=30, textvariable=v_pax_email)
  add_btn = Button(F1, text="Add",  width=10, command=submit_passenger)
  cancel_btn = Button(F1, text="Cancel",  width=10, command=menu_page)

  fn_lbl.grid(row=0, column=0, padx=20, pady=5)
  fn_txt.grid(row=0, column=1, pady=5, padx=10)
  ln_lbl.grid(row=1, column=0, padx=20, pady=5)
  ln_txt.grid(row=1, column=1, pady=5, padx=10)
  phone_lbl.grid(row=2, column=0, padx=20, pady=5)
  phone_txt.grid(row=2, column=1, pady=5, padx=10)
  add_lbl.grid(row=3, column=0, padx=20, pady=5)
  add_txt.grid(row=3, column=1, pady=5, padx=10)
  email_lbl.grid(row=4, column=0, padx=20, pady=5)
  email_txt.grid(row=4, column=1, pady=5, padx=10)

  add_btn.grid(row=5, column=0, pady=5, padx=10)
  cancel_btn.grid(row=5, column=1, pady=5, padx=10)

def search_flights():
  for widget in F1.winfo_children():
    widget.destroy()  
  F1.configure(text='Search Flights')
  F1.place(relx=.5, rely=.5, anchor=CENTER)
  
  scrollbar = Scrollbar(root)
  scrollbar.pack(side=RIGHT, fill=Y)

  from_lbl = Label(F1, text="From:")
  from_txt = Listbox(F1, height=1, width=10,yscrollcommand=scrollbar.set)
  to_lbl = Label(F1, text="To:")
  to_txt = Listbox(F1, height=1, width=10,yscrollcommand=scrollbar.set)
  date_lbl = Label(F1, text="Date:")
  date_txt = Entry(F1, width=10 , textvariable=v_date)
  search_btn = Button(F1, text="Search",  width=10, command=search_result)
  cancel_btn = Button(F1, text="Cancel",  width=10, command=menu_page)
    
  from_lbl.grid(row=0, column=0, padx=20, pady=5)
  from_txt.grid(row=0, column=1, pady=5, padx=10)
  to_lbl.grid(row=0, column=2, padx=20, pady=5)
  to_txt.grid(row=0, column=3, pady=5, padx=10)
  date_lbl.grid(row=0, column=4, padx=20, pady=5)
  date_txt.grid(row=0, column=5, pady=5, padx=10)
  search_btn.grid(row=1, column=0, columnspan=3, padx=20, pady=5)
  cancel_btn.grid(row=1, column=3, columnspan=3, pady=5, padx=10)  

def search_result():
  pass
  
def submit_passenger():
  db_conn = connect_db()
  disconnt_db(db_conn)
  pass
  
def submit_registration():
  db_conn = connect_db()
  disconnt_db(db_conn)
  pass


def connect_db():
  config = configparser.RawConfigParser()
  config.read('db_config.cfg')
  conn_dict = dict(config.items('MYSQL'))
  print("Connecting to db "+ conn_dict['database'])

  cnx = mysql.connector.connect(user=conn_dict['user'], 
                                password=conn_dict['password'],
                                host=conn_dict['host'],
                                database=conn_dict['database'])
  return cnx

def disconnt_db(cnx):
  print("Disconnecting from db")
  cnx.close()
  
#Main script starts here

root = tk.Tk()
v_login_username = StringVar()
v_login_pwd = StringVar()
v_reg_username = StringVar()
v_reg_pwd = StringVar()
v_reg_phone = StringVar()
v_reg_add = StringVar()
v_reg_email = StringVar()
v_pax_fn = StringVar()
v_pax_ln = StringVar()
v_pax_phone = StringVar()
v_pax_add = StringVar()
v_pax_email = StringVar()
v_from = StringVar()
v_to = StringVar()
v_date = StringVar()

F1 = LabelFrame(root, font=('verdana', 12))

header()
login_page()

root.mainloop()
