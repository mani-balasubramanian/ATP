create database atp;

  use atp;

  create table route
  (
    route_id int not null auto_increment primary key,
    airline varchar2(30) not null,
    from char(3) not null,
    to char(3) not null,
    dep_time date not null,
    duration int not null
  );

  create table route_details
  (
    route_id int not null,
    seat_type char(2) not null,
    cost decimal(9,2)
  );

  create table customer
  (
    username varchar2(30) not null auto_increment primary key, 
    password varchar2(30) not null, 
    phone varchar2(15) not null, 
    address varchar2(30), 
    email varchar2(30) not null
  );

  create table booking
  (
    booking_id not null auto_increment primary key, 
    booking_date date not null, 
    travel_date date not null, 
    airline varchar2(30) not null,
    route_id int not null,
    username varchar2(30) not null, 
    no_of_pas int not null, 
    seat_type char(2) not null, 
    total_cost decimal(9,2)
  );

  create table passenger
  (
    booking_id int not null,
    first_name varchar2(30) not null, 
    last_name varchar2(30) not null,
    phone varchar2(15) not null, 
    address varchar2(30), 
    email varchar2(30) not null
   );
   
