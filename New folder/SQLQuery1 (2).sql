CREATE TABLE  round_flight (
Round_flight_id    int   primary key ,
Return_date  Date ,    

Constraint  round_flight_FK foreign key (Round_flight_id)
References     flight (Flight_id)  
);


CREATE TABLE  one_way_flight (
One_way_id    int   primary key ,
Constraint  one_way_flight_FK foreign key (One_way_id)
References     flight (Flight_id)  
);


CREATE TABLE  stop_over_flight (
stop_over_id int primary key ,
Trinsit1   varchar(20)  not null ,
Trinsit2   varchar(20)  not null , 

Constraint  stop_over_flight_FK foreign key (stop_over_id)
References     flight (Flight_id)  
);


CREATE TABLE  charter_flight (
Charter_flight_id  int primary key ,
Company_name  varchar(20)  not null ,
Num_of_passenger int  not null ,
Constraint   charter_flight_FK foreign key (Charter_flight_id)
References     flight (Flight_id)  
);


CREATE TABLE  user_phone 
(
User_phone  varchar(15)  not null , 
User_id  int  ,
primary key (User_phone , User_id ) ,
Constraint   user_phone_fk foreign key (User_id)
References    [user] (user_id)  
); 


CREATE TABLE  booking (
Booking_id  int  primary key ,
Flight_id  int ,
Constraint  booking_flight_FK foreign key (Flight_id) 
References     flight (Flight_id)  
);


CREATE TABLE passenger_booking 
(
Passenger_id  int , 
Booking_id int ,
Constraint  passenger_booking_FK foreign key (Passenger_id) 
References     passenger(Passenger_id )  ,

Constraint  booking_air_flight_FK foreign key (Booking_id) 
References     booking (Booking_id) 
);



select * from [User] ;

INSERT INTO [User ] 
([User_id] , Address , Password , Nationality , Gender , First_name , last_name , Date_of_birth , [User_name] , Email )
VALUES (1 , '456 Elm St.','password123', 'Canada', 'Female',  'Jane', 'Smith', '1990-03-15', 'janesmith', 'janesmith@email.com');
alter table [user] 
alter column Email varchar (30) ;

INSERT INTO [User ] 
       ([User_id] , Address , Password , Nationality , Gender , First_name , last_name , Date_of_birth , [User_name] , Email )
VALUES (2, '123 Main St.', 'password1123', 'USA', 'Male', 'John', 'Doe', '1985-05-10', 'johndoe', 'johndoe@email.com') ,
       (3, '789 Oak St.', 'password789', 'UK', 'Male', 'David', 'Jones', '1988-11-22', 'davidjones', 'davidjones@email.com') ,
	   (4, '321 Pine St.', 'newpassword123', 'Australia', 'Female', 'Sarah', 'Lee', '1995-07-04', 'sarahlee', 'sarahlee@email.com') ,
	   (5, '654 Maple St.', 'mypassword456', 'Mexico', 'Male', 'Carlos', 'Garcia', '1992-09-18', 'carlosgarcia', 'carloa@email.com') ,
       (6, '987 Cedar St.', 'password987', 'France', 'Female', 'Sophie', 'Martin', '1987-12-01', 'sophiemartin', 'sophiemartin@email.com') ,
	   (7, '246 Main St.', 'newpassword456', 'Germany', 'Male', 'Max', 'Schneider', '1993-06-25', 'maxschneider', 'maxschneider@email.com') ,
	   (8, '789 Oak St.', 'mypassword123', 'UK', 'Female', 'Emma', 'Wilson', '1998-02-12', 'emmawilson', 'emmawilson@email.com') ,
	   (9, '456 Maple St.', 'password789', 'Canada', 'Male', 'William', 'Brown', '1991-05-20', 'williambrown', 'williambrown@email.com') ,
	   (10, '123 Cedar St.', 'newpassword456', 'USA', 'Female', 'Emily', 'Taylor', '1994-08-05', 'emilytaylor', 'emilytaylor@email.com');



INSERT INTO [User] 
       ([User_id] , Address , Password , Nationality , Gender , First_name , last_name , Date_of_birth , [User_name] , Email )
VALUES (11, '123 fesal St.', 'captin1', 'USA', 'Male', 'mohammad', 'fawzy', '1985-05-10', 'mohammadfawzy', 'mohammadfawzy@email.com') ,
       (12, '789 bolaq St.', 'captin2', 'egept', 'Male', 'ali', 'ibraheem', '1988-11-22', 'aliibraheem4', 'aliibrah5@email.com') ,
	   (13, '321 haram St.', 'captin3', 'iraq', 'Female', 'Sarah', 'ali', '1995-07-04', 'saraali88', 'sarahlee@email.com') ,
	   (14, '456 elsalam St.','captin4', 'Canada', 'Female',  'mona', 'Smith', '1990-03-15', 'monasmith', 'monasmith@email.com') , 
	   (15, '654 shams St.', 'captin5', 'Mexico', 'Male', 'omar', 'Garcia', '1992-09-18', 'omarsgarcia', 'omargra@email.com') ,
       (16, '987 ali St.', 'captin6', 'somal', 'Female', 'sara', 'omar', '1987-12-01', 'saraomar', 'sophiemartin@email.com') ,
	   (17, '246 Main St.', 'captin7', 'Germany', 'Male', 'Max', 'amr', '1993-06-25', 'maxamr', 'maxamr89@email.com') ,
	   (18, '789 Oak St.', 'captin8', 'UK', 'Female', 'alaa', 'Wilson', '1998-02-12', 'alaawilson', 'alaa1wilson@email.com') ,
	   (19, '456 Maple St.', 'captin9', 'Canada', 'Male', 'emad', 'Brown', '1991-05-20', 'emadbrown', 'emadbrown@email.com') ,
	   (20, '123 Cedar St.', 'captin10', 'USA', 'Female', 'basmala', 'Taylor', '1994-08-05', 'basmalataylor', 'basmalataylor@email.com');

	   

INSERT INTO employee (Employee_id , [User_id] ,  Salary , Days_off )
 VALUES (111, 11, 10000 , 12 ) , 
        (222, 12, 20000 , 13) , 
		(333, 13, 12000 , 10) , 
		(444, 14, 25000 , 5) , 
		(555, 15, 65000 , 5) , 
		(666, 16, 5800 , 8) , 
		(777, 17, 1500 , 9) , 
		(999, 19, 25000 , 8 ) ,
		(1010, 20, 11000 , 8 ) ;



INSERT INTO employee (Employee_id , [User_id] ,  Salary , Days_off )
 VALUES (888, 18, 9900 , 8 ) ; 


INSERT INTO captin ([User_id] , Captin_id) 
VALUES         (11,111) ,
		       (12,222) ,
			   (13,333) ,
			   (14,444) ,
			   (15,555) ,
			   (16,666) ,
			   (17,777) ,
			   (18,888) ,
			   (19,999) ,
			   (20,1010);
select * from captin ;




























