drop database airline;

create database airline;

use airline;

create table route
(
route_id int not null auto_increment primary key,
airline varchar(30) not null,
start char(3) not null,
destination char(3) not null,
dep_time char(5) not null,
duration int not null
);

create table route_details
(
route_id int not null,
seat_type char(2) not null,
cost decimal(9,2),
foreign key(route_id) references route(route_id)
);

create table customer
(
username varchar(30) not null primary key, 
password varchar(30) not null, 
phone varchar(15) not null, 
address varchar(30), 
email varchar(30) not null
);

create table booking
(
booking_id int not null auto_increment primary key, 
booking_date timestamp DEFAULT CURRENT_TIMESTAMP,
travel_date date not null, 
route_id int not null,
username varchar(30) not null, 
no_of_pas int not null,
total_cost decimal(9,2)
);

create table passenger
(
booking_id int not null,
first_name varchar(30) not null, 
last_name varchar(30) not null,
phone varchar(15) not null, 
address varchar(30), 
email varchar(30) not null,
seat_type char(2) not null, 
foreign key (booking_id) references booking(booking_id)
);

-- maa

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','MAA','BLR','06:00',60);
insert into route_details (route_id,seat_type,cost) values (1,'EC',2000);
insert into route_details (route_id,seat_type,cost) values (1,'BC',4000);

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','BLR','MAA','08:00',60);
insert into route_details (route_id,seat_type,cost) values (2,'EC',2000);
insert into route_details (route_id,seat_type,cost) values (2,'BC',4000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','MAA','MUM','09:00',120);
insert into route_details (route_id,seat_type,cost) values (3,'EC',4000);
insert into route_details (route_id,seat_type,cost) values (3,'BC',6000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','MUM','MAA','13:00',120);
insert into route_details (route_id,seat_type,cost) values (4,'EC',4000);
insert into route_details (route_id,seat_type,cost) values (4,'BC',6000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','MAA','BLR','05:00',60);
insert into route_details (route_id,seat_type,cost) values (5,'EC',2000);
insert into route_details (route_id,seat_type,cost) values (5,'BC',4000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','BLR','MAA','10:00',60);
insert into route_details (route_id,seat_type,cost) values (6,'EC',2000);
insert into route_details (route_id,seat_type,cost) values (6,'BC',4000);

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','MAA','MUM','07:00',120);
insert into route_details (route_id,seat_type,cost) values (7,'EC',4000);
insert into route_details (route_id,seat_type,cost) values (7,'BC',6000);

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','MUM','MAA','11:00',120);
insert into route_details (route_id,seat_type,cost) values (8,'EC',4000);
insert into route_details (route_id,seat_type,cost) values (8,'BC',6000);

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','MAA','DEL','14:00',180);
insert into route_details (route_id,seat_type,cost) values (9,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (9,'BC',8000);

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','DEL','MAA','18:00',180);
insert into route_details (route_id,seat_type,cost) values (10,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (10,'BC',8000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','MAA','DEL','15:00',180);
insert into route_details (route_id,seat_type,cost) values (11,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (11,'BC',8000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','DEL','MAA','19:00',180);
insert into route_details (route_id,seat_type,cost) values (12,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (12,'BC',8000);

-- blr


insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','BLR','MUM','09:00',120);
insert into route_details (route_id,seat_type,cost) values (13,'EC',4000);
insert into route_details (route_id,seat_type,cost) values (13,'BC',6000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','MUM','BLR','13:00',120);
insert into route_details (route_id,seat_type,cost) values (14,'EC',4000);
insert into route_details (route_id,seat_type,cost) values (14,'BC',6000);

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','BLR','MUM','07:00',120);
insert into route_details (route_id,seat_type,cost) values (15,'EC',4000);
insert into route_details (route_id,seat_type,cost) values (15,'BC',6000);

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','MUM','BLR','11:00',120);
insert into route_details (route_id,seat_type,cost) values (16,'EC',4000);
insert into route_details (route_id,seat_type,cost) values (16,'BC',6000);

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','BLR','DEL','14:00',180);
insert into route_details (route_id,seat_type,cost) values (17,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (17,'BC',8000);

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','DEL','BLR','18:00',180);
insert into route_details (route_id,seat_type,cost) values (18,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (18,'BC',8000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','BLR','DEL','15:00',180);
insert into route_details (route_id,seat_type,cost) values (19,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (19,'BC',8000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','DEL','BLR','19:00',180);
insert into route_details (route_id,seat_type,cost) values (20,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (20,'BC',8000);

-- mum

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','MUM','DEL','14:00',180);
insert into route_details (route_id,seat_type,cost) values (21,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (21,'BC',8000);

insert into route (airline,start,destination,dep_time,duration) values('INDIGO','DEL','MUM','18:00',180);
insert into route_details (route_id,seat_type,cost) values (22,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (22,'BC',8000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','MUM','DEL','15:00',180);
insert into route_details (route_id,seat_type,cost) values (23,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (23,'BC',8000);

insert into route (airline,start,destination,dep_time,duration) values('AIRINDIA','DEL','MUM','19:00',180);
insert into route_details (route_id,seat_type,cost) values (24,'EC',6000);
insert into route_details (route_id,seat_type,cost) values (24,'BC',8000);

