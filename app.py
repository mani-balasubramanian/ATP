import tkinter as tk
from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
import mysql.connector
import configparser
import datetime
from datetime import timedelta

def header():
  w = 800 # width for the Tk root
  h = 600 # height for the Tk root

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
      v_login_username.set("")
      v_login_pwd.set("")
  F1.configure(text='Login')
  F1.place(relx=.5, rely=.5, anchor=CENTER)

  username_lbl = Label(F1, text="Username:", width=30)
  username_txt = Entry(F1, width=30, textvariable=v_login_username)
  pwd_lbl = Label(F1, text="Password:")
  pwd_txt = Entry(F1, width=30, show="*", textvariable=v_login_pwd)
  login_btn = Button(F1, text="Login",  width=10,command=submit_login)
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
  email_lbl = Label(F1, text="Email:")
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
  
  booking_btn = Button(F1, text="Book Ticket",  width=50, command=flights,font=('verdana', 10))
  history_btn = Button(F1, text="View Bookings",  width=50, command=booking_history,font=('verdana', 10))
  exit_btn = Button(F1, text="Exit",  width=50, command=login_page,font=('verdana', 10))

  booking_btn.grid(row=0, column=0, pady=5, padx=10)
  history_btn.grid(row=1, column=0, pady=5, padx=10)
  exit_btn.grid(row=3, column=0, pady=5, padx=10)

def add_passenger():
  for widget in F1.winfo_children():
    widget.destroy()  
  F1.configure(text='Add Passenger')
  F1.place(relx=.5, rely=.5, anchor=CENTER)
  
  head_lbl1 = Label(F1, text=" ", width=15)
  head_lbl2 = Label(F1, text="Passenger 1", width=15)
  head_lbl3 = Label(F1, text="Passenger 2", width=15)

  fn_lbl = Label(F1, text="First Name:", width=15)
  fn_txt1 = Entry(F1, width=30, textvariable=v_pax_fn1)
  fn_txt2 = Entry(F1, width=30, textvariable=v_pax_fn2)

  ln_lbl = Label(F1, text="Last Name:")
  ln_txt1 = Entry(F1, width=30, textvariable=v_pax_ln1)
  ln_txt2 = Entry(F1, width=30, textvariable=v_pax_ln2)

  phone_lbl = Label(F1, text="Phone:")
  phone_txt1 = Entry(F1, width=30, textvariable=v_pax_phone1)
  phone_txt2 = Entry(F1, width=30, textvariable=v_pax_phone2)

  add_lbl = Label(F1, text="Address:")
  add_txt1 = Entry(F1, width=30, textvariable=v_pax_add1)
  add_txt2 = Entry(F1, width=30, textvariable=v_pax_add2)

  email_lbl = Label(F1, text="Email:")
  email_txt1 = Entry(F1, width=30, textvariable=v_pax_email1)
  email_txt2 = Entry(F1, width=30, textvariable=v_pax_email2)
  
  seat_type_lbl = Label(F1, text="Class:")
  seat_type1 = ttk.Combobox(F1,state="readonly",width=10,values=['EC','BC'], textvariable=v_seat_type1)
  seat_type2 = ttk.Combobox(F1,state="readonly",width=10,values=['EC','BC'], textvariable=v_seat_type2)

  book_btn = Button(F1, text="Book Ticket",  width=10, command=submit_booking)
  cancel_btn = Button(F1, text="Back",  width=10, command=flights)

  head_lbl1.grid(row=0, column=0, padx=20, pady=5)
  head_lbl2.grid(row=0, column=1, padx=20, pady=5)
  head_lbl3.grid(row=0, column=2, padx=20, pady=5)

  fn_lbl.grid(row=1, column=0, padx=20, pady=5)
  fn_txt1.grid(row=1, column=1, pady=5, padx=10)
  fn_txt2.grid(row=1, column=2, pady=5, padx=10)

  ln_lbl.grid(row=2, column=0, padx=20, pady=5)
  ln_txt1.grid(row=2, column=1, pady=5, padx=10)
  ln_txt2.grid(row=2, column=2, pady=5, padx=10)
  
  phone_lbl.grid(row=3, column=0, padx=20, pady=5)
  phone_txt1.grid(row=3, column=1, pady=5, padx=10)
  phone_txt2.grid(row=3, column=2, pady=5, padx=10)

  add_lbl.grid(row=4, column=0, padx=20, pady=5)
  add_txt1.grid(row=4, column=1, pady=5, padx=10)
  add_txt2.grid(row=4, column=2, pady=5, padx=10)

  email_lbl.grid(row=5, column=0, padx=20, pady=5)
  email_txt1.grid(row=5, column=1, pady=5, padx=10)
  email_txt2.grid(row=5, column=2, pady=5, padx=10)

  seat_type_lbl.grid(row=6, column=0, padx=20, pady=5)
  seat_type1.grid(row=6, column=1, pady=5, padx=10)
  seat_type2.grid(row=6, column=2, pady=5, padx=10)
  
  book_btn.grid(row=8, column=1, pady=5, padx=10)
  cancel_btn.grid(row=8, column=2, pady=5, padx=10)

def flights():
  for widget in F1.winfo_children():
    widget.destroy()  
  F1.configure(text='Search Flights')
  F1.place(relx=.5, rely=.5, anchor=CENTER)
  db_conn = connect_db()
  cursor = db_conn.cursor()
  query = ("select distinct start from route order by start")  
  print(query)
  cursor.execute(query)
  from_values = cursor.fetchall()
  query = ("select distinct destination from route order by destination")  
  print(query)
  cursor.execute(query)
  to_values = cursor.fetchall()

  sday = datetime.datetime.today() + timedelta(days=1)
  eday=datetime.datetime.today() + timedelta(days=10)
  date_values = [(sday+timedelta(days=x)).strftime('%Y-%m-%d') for x in range((eday-sday).days)]

  from_lbl = Label(F1, text="From:")
  from_txt = ttk.Combobox(F1,state="readonly",width=10,values=from_values, textvariable=v_from)
  to_lbl = Label(F1, text="To:")
  to_txt = ttk.Combobox(F1,state="readonly",width=10,values=to_values, textvariable=v_to)
  date_lbl = Label(F1, text="Date:")
  date_txt = ttk.Combobox(F1,state="readonly",width=10,values=date_values,textvariable=v_date)
  search_btn = Button(F1, text="Search",  width=10, command=submit_flights)
  cancel_btn = Button(F1, text="Cancel",  width=10, command=menu_page)
    
  from_lbl.grid(row=0, column=0, padx=20, pady=5)
  from_txt.grid(row=0, column=1, pady=5, padx=10)
  to_lbl.grid(row=0, column=2, padx=20, pady=5)
  to_txt.grid(row=0, column=3, pady=5, padx=10)
  date_lbl.grid(row=0, column=4, padx=20, pady=5)
  date_txt.grid(row=0, column=5, pady=5, padx=10)
  search_btn.grid(row=1, column=0, columnspan=3, padx=20, pady=5)
  cancel_btn.grid(row=1, column=3, columnspan=3, pady=5, padx=10) 
  

def submit_login():
  l_login_user = v_login_username.get().strip()
  db_conn = connect_db()
  result=[]
  cursor = db_conn.cursor()
  query = ("select * from customer where username = %s")  
  print(query)
  cursor.execute(query,(l_login_user,))
  result = cursor.fetchall()
  disconnt_db(db_conn)
  if len(result) == 0:
    messagebox.showinfo("Error", "Invalid Username/Password.  If you are a first time user, please register in the app.")
  else:
    menu_page()          

def submit_flights():
  l_from = v_from.get()
  l_to = v_to.get()
  l_date = v_date.get()
  if (l_from == "" or l_to == "" or l_date == ""):
    messagebox.showinfo("Error", "Plese select all required details")
  else:
    db_conn = connect_db()
    result=[]
    cursor = db_conn.cursor()
    query = ("select route_id,airline,start,destination,'" +l_date+"' as dep_date, dep_time from route where start=%s and destination=%s")
    print(query)
    cursor.execute(query,(l_from,l_to))  
    result = cursor.fetchall()
    if len(result) == 0:
      messagebox.showinfo("Error", "No Flights found for the given criteria.")
    else:
      search_results(result)

def search_results(result):
  for widget in F1.winfo_children():
    widget.destroy()  
  F1.configure(text='flight results')
  F1.place(relx=.5, rely=.5, anchor=CENTER)
  header = ['ID','AIRLINE','FROM','TO','DATE','TIME']
  r=0
  c=0
  for h in header:
    lbl = Label(F1, text=h)
    lbl.grid(row=r, column=c, padx=20, pady=5)
    c=c+1
  r=r+1
  
  for res in result: 
    c=0
    for col in res:
      if c==0:
        v_route.set(col)
        rb = Radiobutton(F1, text = col, variable = v_route, value=col)
        rb.grid(row=r, column=c, padx=20, pady=5)
      else:
        lbl = Label(F1, text=col)
        lbl.grid(row=r, column=c, padx=20, pady=5)
      c=c+1
    r=r+1
  search_btn = Button(F1, text="Continue",  width=10, command=add_passenger)
  cancel_btn = Button(F1, text="Cancel",  width=10, command=menu_page)
  search_btn.grid(row=r, column=0, columnspan=3, padx=20, pady=5)
  cancel_btn.grid(row=r, column=3, columnspan=3, pady=5, padx=10) 
 
def submit_registration():
  l_reg_user = v_reg_username.get().strip()
  l_reg_pwd = v_reg_pwd.get().strip()
  l_reg_phone = v_reg_phone.get().strip()
  l_reg_address = v_reg_add.get().strip()
  l_reg_email = v_reg_email.get().strip()
  db_conn = connect_db()
  cursor = db_conn.cursor()
  query = ("select * from customer where username = %s")
  print(query)
  cursor.execute(query,(l_reg_user,))
  result = cursor.fetchall()
  
  if len(result) > 0:
    messagebox.showinfo("Error", "Username Already Exists.  Please choose different username.")
  else: 
    cursor = db_conn.cursor()
    query = ("insert into customer (username,password,phone,address,email) values (%s,%s,%s,%s,%s)")  
    print(query)
    cursor.execute(query,(l_reg_user,l_reg_pwd,l_reg_phone,l_reg_address,l_reg_email,))
    db_conn.commit()
    messagebox.showinfo("Info", "User successfully registered to the system")
  disconnt_db(db_conn)
  login_page()

def submit_booking():
  l_pax_flag1=False
  l_pax_fn1 = v_pax_fn1.get().strip()
  l_pax_ln1 = v_pax_ln1.get().strip()
  l_pax_phone1 = v_pax_phone1.get().strip()
  l_pax_add1 = v_pax_add1.get().strip()
  l_pax_email1 = v_pax_email1.get().strip()
  l_seat_type1 = v_seat_type1.get().strip()
  
  l_pax_flag2=False
  l_pax_fn2 = v_pax_fn2.get().strip()
  l_pax_ln2 = v_pax_ln2.get().strip()
  l_pax_phone2 = v_pax_phone2.get().strip()
  l_pax_add2 = v_pax_add2.get().strip()
  l_pax_email2 = v_pax_email2.get().strip()
  l_seat_type2 = v_seat_type2.get().strip()

  l_passenger_list=[]
  if (l_pax_fn1 != "" and l_pax_ln1 != "" and l_pax_phone1 != "" and l_seat_type1 != ""):
    print ("Adding passenger 1")
    l_passenger_dict={}
    l_passenger_dict["fn"] = l_pax_fn1
    l_passenger_dict["ln"] = l_pax_ln1
    l_passenger_dict["phone"] = l_pax_phone1
    l_passenger_dict["address"] = l_pax_add1
    l_passenger_dict["email"] = l_pax_email1
    l_passenger_dict["seat"] = l_seat_type1
    l_passenger_list.append(l_passenger_dict)
    l_pax_flag1=True
    
  if (l_pax_fn2 != "" and l_pax_ln2 != "" and l_pax_phone2 != "" and l_seat_type2 != ""):
    print ("Adding passenger 2")
    l_passenger_dict={}
    l_passenger_dict["fn"] = l_pax_fn2
    l_passenger_dict["ln"] = l_pax_ln2
    l_passenger_dict["phone"] = l_pax_phone2
    l_passenger_dict["address"] = l_pax_add2
    l_passenger_dict["email"] = l_pax_email2
    l_passenger_dict["seat"] = l_seat_type2
    l_passenger_list.append(l_passenger_dict)    
    l_pax_flag2=True
      
  if len(l_passenger_list) >0 :
    db_conn = connect_db()
    cursor = db_conn.cursor()
    query = ("insert into booking (travel_date,route_id,username,no_of_pas) values (%s,%s,%s,%s)")  
    print(query)
    cursor.execute(query,(v_date.get(),v_route.get(),v_login_username.get(),len(l_passenger_list)))
    
    cost = 0.0
    for p in l_passenger_list:
      query = ("select cost from route_details where seat_type = %s and route_id = %s")
      print(query)
      cursor.execute(query,(p["seat"],v_route.get()))
      result = cursor.fetchone()
      cost = cost + float(result[0])
      query = ("insert into passenger (booking_id,first_name,last_name,phone,address,email,seat_type) values (last_insert_id(),%s,%s,%s,%s,%s,%s)")  
      print(query)
      cursor.execute(query,(p["fn"],p["ln"],p["phone"],p["address"],p["email"],p["seat"]))

    query = "update booking set total_cost = "+str(cost)+" where booking_id=last_insert_id()"
    print(query)
    cursor.execute(query)

    query = ("select last_insert_id()")
    print(query)
    cursor.execute(query)
    result = cursor.fetchone()
    l_booking_id = result[0]
    db_conn.commit()
    disconnt_db(db_conn)
    messagebox.showinfo("Info", "Booking Successful")
    view_booking(l_booking_id)
  else:
    messagebox.showinfo("Info", "Insufficient Passenger Data.")

def view_booking(booking_id):
  for widget in F1.winfo_children():
      widget.destroy()  
  F1.configure(text='Booking')
  F1.place(relx=.5, rely=.5, anchor=CENTER)
  db_conn = connect_db()
  cursor = db_conn.cursor()  
  query = """
  select 
	r.start
	,r.destination
	,r.airline
	,b.travel_date
	,r.dep_time 
	,p.pax
	,b.total_cost
  from route r, booking b, (select booking_id, group_concat(first_name) as pax from passenger group by booking_id) p
  where r.route_id = b.route_id
  and p.booking_id = b.booking_id
  and b.booking_id= """+str(booking_id)
  print(query)
  cursor.execute(query)
  result = cursor.fetchone()

  
  from_lbl = Label(F1, text="From:", width=30)
  from_txt = Label(F1, text=result[0])
  to_lbl = Label(F1, text="To:")
  to_txt = Label(F1, text=result[1])
  airline_lbl = Label(F1, text="Airline:")
  airline_txt = Label(F1, text=result[2])
  traveldt_lbl = Label(F1, text="Date:")
  traveldt_txt = Label(F1, text=result[3])
  traveltime_lbl = Label(F1, text="Time:")
  traveltime_txt = Label(F1, text=result[4])
  pax_lbl = Label(F1, text="Passengers:")
  pax_txt = Label(F1, text=result[5])
  cost_lbl = Label(F1, text="Total Cost:")
  cost_txt = Label(F1, text=result[6])
  
  cancel_btn = Button(F1, text="Close",  width=10, command=flights)

  from_lbl.grid(row=0, column=0, padx=20, pady=5)
  from_txt.grid(row=0, column=1, pady=5, padx=10)
  to_lbl.grid(row=1, column=0, padx=20, pady=5)
  to_txt.grid(row=1, column=1, pady=5, padx=10)
  airline_lbl.grid(row=2, column=0, padx=20, pady=5)
  airline_txt.grid(row=2, column=1, pady=5, padx=10)
  traveldt_lbl.grid(row=3, column=0, padx=20, pady=5)
  traveldt_txt.grid(row=3, column=1, pady=5, padx=10)
  traveltime_lbl.grid(row=4, column=0, padx=20, pady=5)
  traveltime_txt.grid(row=4, column=1, pady=5, padx=10)
  pax_lbl.grid(row=5, column=0, padx=20, pady=5)
  pax_txt.grid(row=5, column=1, pady=5, padx=10)
  cost_lbl.grid(row=6, column=0, padx=20, pady=5)
  cost_txt.grid(row=6, column=1, pady=5, padx=10)  
  cancel_btn.grid(row=7, column=2,pady=5, padx=10) 
  disconnt_db(db_conn)

def booking_history():
  for widget in F1.winfo_children():
      widget.destroy()  
  F1.configure(text='Booking')
  F1.place(relx=.5, rely=.5, anchor=CENTER)
  db_conn = connect_db()
  cursor = db_conn.cursor()  
  query = """
  select 
	b.booking_id
	,b.booking_date
	,r.start
	,r.destination
	,r.airline
	,b.travel_date
	,r.dep_time 
	,b.total_cost
  from route r, booking b
  where r.route_id = b.route_id
  and username='"""+v_login_username.get()+"""' order by booking_id desc"""
  print(query)
  cursor.execute(query)
  result = cursor.fetchall()

  header = ['ID','BOOKING DT','FROM','TO','AIRLINE','TR DATE','TIME','COST']
  r=0
  c=0
  for h in header:
    lbl = Label(F1, text=h)
    lbl.grid(row=r, column=c, padx=20, pady=5)
    c=c+1
  r=r+1
  
  for res in result: 
    c=0
    for col in res:
      lbl = Label(F1, text=col)
      lbl.grid(row=r, column=c, padx=20, pady=5)
      c=c+1
    r=r+1
  cancel_btn = Button(F1, text="Close",  width=10, command=menu_page)
  cancel_btn.grid(row=r, column=3, columnspan=3, pady=5, padx=10) 
  disconnt_db(db_conn)

  
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
  if cnx and cnx.is_connected():
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
v_pax_fn1 = StringVar()
v_pax_ln1 = StringVar()
v_pax_phone1 = StringVar()
v_pax_add1 = StringVar()
v_pax_email1 = StringVar()
v_pax_fn2 = StringVar()
v_pax_ln2 = StringVar()
v_pax_phone2 = StringVar()
v_pax_add2 = StringVar()
v_pax_email2 = StringVar()
v_seat_type1 = StringVar()
v_seat_type2 = StringVar()
v_from = StringVar()
v_to = StringVar()
v_date = StringVar()
v_route = StringVar()
v_booking_id = StringVar()

F1 = LabelFrame(root, font=('verdana', 12))

header()
login_page()

root.mainloop()
