from flask import Flask,render_template,request
import  Database

CompanyName = "AM AIRLINE"
app = Flask(__name__)

@app.route('/')
def MainHome():
    return render_template("Home Page.html" , title = "Home Page" , ComName = CompanyName)

@app.route('/Login')
def Login():
    return render_template("Fixed Side/Login.html" , title = "Login Page" , ComName = CompanyName)

@app.route('/SearchAccount'  , methods= ["POST" ,"GET"])
def SearchAccount():
    if request.method == "POST":
        Username = request.form.get("Username")
        Password = request.form.get("Password")
        db = Database.DB("flight")
        Fromdata = db.SelectOneWithOutDeplic("Source")
        Todata = db.SelectOneWithOutDeplic("Destination")
        db = Database.DB("[User]")
        Id = int(db.SelectOneTWhere("User_id","User_name" , Username , False ,"Password" , Password , False))
        xdb = Database.DB("admin")
        data = xdb.SelectOne("User_id")
        for i in data:
            if int(i[0]) == Id:
                return render_template("Admin Side/Dashborad.html" , title = "Admin Dashboard Page" , ComName = CompanyName)
        xdb = Database.DB("passenger")
        wdata = xdb.SelectOne("Passenger_id")
        for i in wdata:
            if int(i[0]) == Id:
                return render_template("Passenger Side/Dashborad.html" , title = "Passenger Dashboard Page" , ComName = CompanyName , UserId = Id , Fromdata = Fromdata ,Todata = Todata)

@app.route('/Register')
def Register():
    return render_template("Passenger Side/Register.html" , title = "Register Page" , ComName = CompanyName)

@app.route('/AddNewAccount' , methods= ["POST" ,"GET"])
def AddNewAccount():
    if request.method == "POST":
        Username  = request.form.get("Username")
        FName  = request.form.get("FName")
        LName  = request.form.get("LName")
        Password  = request.form.get("Password")
        Email  = request.form.get("Email")
        Mobile  = request.form.get("Mobile")
        Address  = request.form.get("Address")
        Birthday  = request.form.get("Birthday")
        Gender  = request.form.get("Gender")
        Nationalty  = request.form.get("Nationalty")
        Passport  = request.form.get("Passport")
        db = Database.DB("[User]")
        Id = len(db.SelectAll())
        db.InsertAll([Id+1,False],[Address,True],[Password,True],[Nationalty,True],[Gender,True],[FName,True],[LName,True],[Birthday,True],[Username,True],[Email,True])
        tdb = Database.DB("user_phone")
        tdb.InsertAll([Mobile,True],[Id,False])
        pdb = Database.DB("passenger")
        pdb.InsertAll([Id+1,False],[Passport,True],['',False])
    return render_template("Fixed Side/Login.html" , title = "Login Page" , ComName = CompanyName , )

@app.route('/ChangePassword' , methods= ["POST" ,"GET"])
def ChangePassword():
    if request.method == "POST":
        Username = request.form.get("Username")
        OldPassword = request.form.get("OldPassword")
        NewPassword = request.form.get("NewPassword")
        RenewPassword = request.form.get("RenewPassword")
        if NewPassword == RenewPassword:
            db = Database.DB("[User]")
            Pass = db.SelectOneWhere("Password","User_name",Username,False)
            if Pass == OldPassword:
                db.UpdateOne("Password",NewPassword,False,"User_name",Username,False)
            else:
                return render_template("Error.html" , title = "Error Page" , ComName = CompanyName)
        else:
                return render_template("Error.html" , title = "Error Page" , ComName = CompanyName)
    return render_template("Fixed Side/Change Password.html" , title = "Change Password Page" , ComName = CompanyName , User  = "Admin")

@app.route('/ADashboard')
def ADashboard():
    return render_template("Admin Side/Dashborad.html" , title = "Admin Dashboard Page" , ComName = CompanyName)

@app.route('/AddCaptin' , methods= ["POST" ,"GET"])
def AddCaptin():
    if request.method == "POST":
        Username  = request.form.get("Username")
        FName  = request.form.get("FName")
        LName  = request.form.get("LName")
        Password  = request.form.get("Password")
        Email  = request.form.get("Email")
        Mobile  = request.form.get("Mobile")
        Address  = request.form.get("Address")
        Birthday  = request.form.get("Birthday")
        Gender  = request.form.get("Gender")
        Nationalty  = request.form.get("Nationalty")
        Salary  = request.form.get("Salary")
        db = Database.DB("[User]")
        Id = len(db.SelectAll())+1
        db.InsertAll([Id,False],[Address,True],[Password,True],[Nationalty,True],[Gender,True],[FName,True],[LName,True],[Birthday,True],[Username,True],[Email,True])
        tdb = Database.DB("user_phone")
        tdb.InsertAll([Mobile,True],[Id,False])
        edb = Database.DB("employee")
        eId = len(edb.SelectAll())+1
        edb.InsertAll([eId,False],[Id,False],[Salary,False],[5,False])
        cdb = Database.DB("captin")
        cdb.InsertAll([Id,False],[eId,False],[0,False])

    return render_template("Admin Side/Add Captin.html" , title = "Add Captin Page" , ComName = CompanyName)

@app.route('/ModifyCaptin' , methods= ["POST" ,"GET"])
def ModifyCaptin():
    if request.method == "POST":
        Username  = request.form.get("Username")
        FName  = request.form.get("FName")
        LName  = request.form.get("LName")
        Password  = request.form.get("Password")
        Email  = request.form.get("Email")
        Mobile  = request.form.get("Mobile")
        Address  = request.form.get("Address")
        Birthday  = request.form.get("Birthday")
        Gender  = request.form.get("Gender")
        Nationalty  = request.form.get("Nationalty")
        Salary  = request.form.get("Salary")
        db = Database.DB("[User]")
        Id = int(db.SelectOneWhere("User_id","User_name" , Username , False))
        if FName:
            db.UpdateOne("First_name",FName,False,"User_name",Username,False)
        if LName:
            db.UpdateOne("Last_name",FName,False,"User_name",Username,False)
        if Password:
            db.UpdateOne("Password",Password,False,"User_name",Username,False)
        if Email:
            db.UpdateOne("Email",Email,False,"User_name",Username,False)
        if Address:
            db.UpdateOne("Address",Address,False,"User_name",Username,False)
        if Birthday:
            db.UpdateOne("Date_of_birth",Birthday,False,"User_name",Username,False)
        if Nationalty:
            db.UpdateOne("Nationality",Nationalty,False,"User_name",Username,False)
        if Gender:
            db.UpdateOne("Gender",Gender,False,"User_name",Username,False)
        if Salary:
            edb = Database.DB("employee")
            edb.UpdateOne("Salary",Salary,True,"User_id",Id,True)
        if Mobile:
            mdb = Database.DB("user_phone")
            mdb.UpdateOne("User_phone",Mobile,True,"User_id",Id,True)

    return render_template("Admin Side/Modify Captin.html" , title = "Modify Captin Page" , ComName = CompanyName)

@app.route('/AddAircraft' , methods= ["POST" ,"GET"])
def AddAircraft():
    if request.method == "POST":
        Name  = request.form.get("Name")
        Brand  = request.form.get("Brand")
        Type  = request.form.get("Type")
        Capacity  = request.form.get("Capacity")
        ClassA  = request.form.get("ClassA")
        ClassB  = request.form.get("ClassB")
        ClassC  = request.form.get("ClassC")
        ProDate  = request.form.get("ProDate")
        Status = 'InServise'
        db = Database.DB("air_craft")
        Id = len(db.SelectAll())+1
        if int(ClassA)+int(ClassB)+int(ClassC) == int(Capacity):
            db.InsertAll([Id,False],[Type,True],[Status,True],[Capacity,False],[ProDate,False],[131,False],[21,False],[Brand,True],[Name,True],[ClassA,False],[ClassB,False],[ClassC,False])
        else:
            return render_template("Error.html" , title = "Error Page" , ComName = CompanyName)
    return render_template("Admin Side/Add Aircraft.html" , title = "Add Aircraft Page" , ComName = CompanyName)

@app.route('/ModifyAircraft' , methods= ["POST" ,"GET"])
def ModifyAircraft():
    if request.method == "POST":
        Name  = request.form.get("Name")
        Brand  = request.form.get("Brand")
        Type  = request.form.get("Type")
        Capacity  = request.form.get("Capacity")
        ProDate  = request.form.get("ProDate")
        Status = request.form.get("Status")
        ClassA  = request.form.get("ClassA")
        ClassB  = request.form.get("ClassB")
        ClassC  = request.form.get("ClassC")
        db = Database.DB("air_craft")
        if Type:
            db.UpdateOne("Brand",Brand,False,"Neck_name",Name,False)
        if Brand:
            db.UpdateOne("type",Type,False,"Neck_name",Name,False)
        if Capacity:
            db.UpdateOne("capacity",Capacity,True,"Neck_name",Name,False)
        if ProDate:
            db.UpdateOne("production_year",ProDate,False,"Neck_name",Name,False)
        if Status:
            db.UpdateOne("current_status",Status,False,"Neck_name",Name,False)
        if ClassA:
            db.UpdateOne("class_a",ClassA,True,"Neck_name",Name,False)
        if ClassB:
            db.UpdateOne("class_b",ClassB,True,"Neck_name",Name,False)
        if ClassC:
            db.UpdateOne("class_c",ClassC,True,"Neck_name",Name,False)
    return render_template("Admin Side/Modify Aircraft.html" , title = "Modify Aircraft Page" , ComName = CompanyName)

@app.route('/AddFlight' , methods= ["POST" ,"GET"])
def AddFlight():
    users = Database.DB("[User]")
    craft = Database.DB("air_craft")
    aircrafts = craft.SelectAll()
    emp = Database.DB("employee")
    caps = Database.DB("captin")
    staffs = Database.DB("staff")
    staffsdata = staffs.SelectOneWithOutDeplic("staff_type") 
    capts  =caps.SelectOne("User_id")
    captins = []
    for Row in capts:
        captins.append([emp.SelectOneWhere("Employee_id","User_id",Row[0],True),[list(tup) for tup in users.SelectManyWhere(["First_name","last_name"],"User_id",Row[0],True)]])
    if request.method == "POST":
        Airline = request.form.get("Airline")
        Travelingdate = request.form.get("Travelingdate")
        Arriveingdate = request.form.get("Arriveingdate")
        From = request.form.get("From")
        To = request.form.get("To")
        Aircraft = request.form.get("Aircraft")
        Captin = request.form.get("Captin")
        Staff = request.form.get("Staff")
        Type = request.form.get("Type")
        ClassA  = request.form.get("ClassA")
        ClassB  = request.form.get("ClassB")
        ClassC  = request.form.get("ClassC")
        PersonsNumber = request.form.get("PersonsNumber")
        db = Database.DB("flight")
        Id = len(db.SelectAll())+1
        caps.UpdateOne("number_of_trips", 'number_of_trips+1',True,"Captin_id",Captin,True)
        if Type == 'OneWay':
            Triptype = Database.DB("one_way_flight")
            Triptype.InsertOne("One_way_id",Id,True)
        elif Type == 'RoundWay':
            ReturnDate = request.form.get("ReturnDate")
            Triptype = Database.DB("round_flight")
            Triptype.InsertAll([Id,False],[ReturnDate,True])
        elif Type == 'StopOverTrip':
            Trinsit1 = request.form.get("Trinsit1")
            Trinsit2 = request.form.get("Trinsit2")
            Triptype = Database.DB("stop_over_flight")
            Triptype.InsertAll([Id,False],[Trinsit1,True],[Trinsit2,True])
        elif Type == 'CharterTrip':
            CompanyLabel = request.form.get("CompanyLabel")
            Triptype = Database.DB("charter_flight")
            Triptype.InsertAll([Id,False],[CompanyLabel,True],[PersonsNumber,False])
        else:
            pass
        if PersonsNumber:
            db.InsertAll([Id,False],[Travelingdate,True],[Airline,True],[Arriveingdate,True],[From,True],[To,True],[PersonsNumber,False],[131,False],[21,False],[Aircraft,False],[Captin,False],[Staff,True],[Type,True],[0,False],[0,False],[0,False],[ClassA,False],[ClassB,False],[ClassC,False])    
        else:
            db.InsertAll([Id,False],[Travelingdate,True],[Airline,True],[Arriveingdate,True],[From,True],[To,True],[0,False],[131,False],[21,False],[Aircraft,False],[Captin,False],[Staff,True],[Type,True]) 
    return render_template("Admin Side/Add Flight.html" , title = "Add Flight Page" , ComName = CompanyName , aircrafts = aircrafts , captins = captins , staffsdata = staffsdata )

@app.route('/ModifyFlight' , methods= ["POST" ,"GET"])
def ModifyFlight():
    users = Database.DB("[User]")
    craft = Database.DB("air_craft")
    aircrafts = craft.SelectAll()
    staffs = Database.DB("staff")
    staffsdata = staffs.SelectOneWithOutDeplic("staff_type") 
    emp = Database.DB("employee")
    caps = Database.DB("captin")
    capts  =caps.SelectOne("User_id")
    captins = []
    for Row in capts:
        captins.append([emp.SelectOneWhere("Employee_id","User_id",Row[0],True),[list(tup) for tup in users.SelectManyWhere(["First_name","last_name"],"User_id",Row[0],True)]])
    if request.method == "POST":
        Id = request.form.get("Id")
        Airline = request.form.get("Airline")
        Travelingdate = request.form.get("Travelingdate")
        Arriveingdate = request.form.get("Arriveingdate")
        From = request.form.get("From")
        To = request.form.get("To")
        Aircraft = request.form.get("Aircraft")
        Captin = request.form.get("Captin")
        Staff = request.form.get("Staff")
        Type = request.form.get("Type")
        ClassA  = request.form.get("ClassA")
        ClassB  = request.form.get("ClassB")
        ClassC  = request.form.get("ClassC")
        db = Database.DB("flight")
        if Airline:
            db.UpdateOne("Airline",Airline,False,"Flight_id",Id,True)
        if Travelingdate:
            db.UpdateOne("Arrival_date",Travelingdate,False,"Flight_id",Id,True)
        if Arriveingdate:
            db.UpdateOne("Departual_date",Arriveingdate,False,"Flight_id",Id,True)
        if From:
            db.UpdateOne("Source",From,False,"Flight_id",Id,True)
        if To:
            db.UpdateOne("Destination",To,False,"Flight_id",Id,True)
        if Aircraft:
            db.UpdateOne("Air_craft_id",Aircraft,True,"Flight_id",Id,True)
        if Captin:
            db.UpdateOne("Captin_id",Captin,True,"Flight_id",Id,True)
        if Staff:
            db.UpdateOne("staff_type",Staff,False,"Flight_id",Id,True)
        if ClassA:
            db.UpdateOne("pric_class_a",ClassA,True,"Flight_id",Id,True)
        if ClassB:
            db.UpdateOne("pric_class_a",ClassB,True,"Flight_id",Id,True)
        if ClassC:
            db.UpdateOne("pric_class_a",ClassC,True,"Flight_id",Id,True)
        if Type:
            oldtype = db.SelectOneWhere("flight_type","Flight_id",Id,True)
            db.UpdateOne("flight_type",Type,False,"Flight_id",Id,True)
            if Type != oldtype:
                if oldtype == 'OneWay':
                    Triptype = Database.DB("one_way_flight")
                    Triptype.DeleteAllWhere("One_way_id",Id,True)
                elif oldtype == 'RoundWay':
                    Triptype = Database.DB("round_flight")
                    Triptype.DeleteAllWhere("Round_flight_id",Id,True)
                elif oldtype == 'StopOverTrip':
                    Triptype = Database.DB("stop_over_flight")
                    Triptype.DeleteAllWhere("stop_over_id",Id,True)
                elif oldtype == 'CharterTrip':
                    Triptype = Database.DB("charter_flight")
                    Triptype.DeleteAllWhere("Charter_flight_id",Id,True)
                else:
                    pass
                if Type == 'OneWay':
                    Triptype = Database.DB("one_way_flight")
                    Triptype.InsertOne("One_way_id",Id,True)
                elif Type == 'RoundWay':
                    ReturnDate = request.form.get("ReturnDate")
                    Triptype = Database.DB("round_flight")
                    Triptype.InsertAll([Id,False],[ReturnDate,True])
                elif Type == 'StopOverTrip':
                    Trinsit1 = request.form.get("Trinsit1")
                    Trinsit2 = request.form.get("Trinsit2")
                    Triptype = Database.DB("stop_over_flight")
                    Triptype.InsertAll([Id,False],[Trinsit1,True],[Trinsit2,True])
                elif Type == 'CharterTrip':
                    CompanyLabel = request.form.get("CompanyLabel")
                    PersonsNumber = request.form.get("PersonsNumber")
                    Triptype = Database.DB("charter_flight")
                    Triptype.InsertAll([Id,False],[CompanyLabel,True],[PersonsNumber,False])
                else:
                    pass
            else:
                pass
    return render_template("Admin Side/Modify Flight.html" , title = "Modify Flight Page" , ComName = CompanyName, aircrafts = aircrafts , captins = captins , staffsdata = staffsdata )

@app.route('/ShowFlight' , methods= ["POST" ,"GET"])
def ShowFlight():
    if request.method == "POST":
        FId = request.form.get("Id")
        
    return render_template("Admin Side/Show Flight.html" , title = "Show Flight Page" , ComName = CompanyName)

@app.route('/ShowFlights')
def ShowFlights():
    db = Database.DB("flight")
    data = db.SelectAll()
    return render_template("Admin Side/Show Flights.html" , title = "Show Flights Page" , ComName = CompanyName , data = data)

@app.route('/ShowAircrafts')
def ShowAircrafts():
    db = Database.DB("air_craft")
    data = db.SelectAll()
    return render_template("Admin Side/Show Aircrafts.html" , title = "Show Aircrafts Page" , ComName = CompanyName , data = data)


@app.route('/PDashboard')
def PDashboard():
    db = Database.DB("flight")
    Fromdata = db.SelectOneWithOutDeplic("Source")
    Todata = db.SelectOneWithOutDeplic("Destination")
    return render_template("Passenger Side/Dashborad.html" , title = "Passenger Dashboard Page" , ComName = CompanyName ,Fromdata = Fromdata , Todata = Todata)

@app.route('/PProfile')
def PProfile():
    return render_template("Passenger Side/Profile.html" , title = "Profile Dashboard Page" , ComName = CompanyName)

@app.route('/SearchTicket' , methods= ["POST" ,"GET"])
def SearchTicket():
    if request.method == "POST":
        UserId = request.form.get("UserId")
        From = request.form.get("From")
        To = request.form.get("To")
        Type = request.form.get("Type")
        Date = request.form.get("Date")
        Adult = request.form.get("Adult")
        Child = request.form.get("Child")
        Baby = request.form.get("Baby")
        Class = request.form.get("Class")
        db = Database.DB("flight")
        Result = db.SelectFromFlight(From,To,Date,Type)
    return render_template("Passenger Side/Book Ticket.html" , title = "Book Ticket Page" , ComName = CompanyName , Message = Result[2] , Result = Result[0] , UserId = UserId , Tickets = [Adult,Child,Baby])

@app.route('/Getdata' , methods= ["POST" ,"GET"])
def Getdata():
    if request.method == "POST":
        UserId = request.form.get("UserId")
        FlightId = request.form.get("FlightId")
        Class = request.form.get("Class")
        Price = request.form.get("Price")
        Adult = request.form.get("Adult")
        Child = request.form.get("Child")
        Baby = request.form.get("Baby")
        Ad = []
        Ch = []
        Ba = []
        for i in range(int(Adult)):
            Ad.append(i)
        for i in range(int(Child)):
            Ch.append(i)
        for i in range(int(Baby)):
            Ba.append(i)
    return render_template("Passenger Side/Get data.html" , title = "Get data Page" , ComName = CompanyName , data = [UserId , FlightId , Class , Price] , Tickets = [Ad , Ch , Ba] , T = [Adult , Child , Baby] )

@app.route('/Insertdata' , methods= ["POST" ,"GET"])
def Insertdata():
    if request.method == "POST":
        UserId = request.form.get("UserId")
        FlightId = request.form.get("FlightId")
        Class = request.form.get("Class")
        Price = request.form.get("Price")
        Adult = request.form.get("Adult")
        Child = request.form.get("Child")
        Baby = request.form.get("Baby")
        Payment = request.form.get("Payment")
        xdb = Database.DB("flight")
        db = Database.DB("booking")
        pdb = Database.DB("passenger_booking")
        ddb = Database.DB("dependant")
        tdb = Database.DB("ticket")
        for i in range(int(Adult)):
            Name = request.form.get(f"AName{i}")
            Age = request.form.get(f"AAge{i}")
            Passport = request.form.get(f"APassportNumber{i}")
            Disease = request.form.get(f"ADiseace{i}")
            BookingId =int(xdb.SelectOneWhere("Number_of_passenger","Flight_id",FlightId,True))
            db.InsertAll([BookingId,False],[FlightId,False],['Self',True],[Age,False],[Name,True],[Payment,True],[Disease,True],[Passport,False],[Class,True],[Price,False])
            pdb.InsertAll([UserId,False],[BookingId,False])
            tdb.InsertAll([FlightId,False],[BookingId,False],['Booking',True])
            if Class == "A":
                xdb.UpdateOne("number_class_a",'number_class_a+1',True,"Flight_id",FlightId,True)
            elif Class == "B":
                xdb.UpdateOne("number_class_b",'number_class_b+1',True,"Flight_id",FlightId,True)
            else:
                xdb.UpdateOne("number_class_c",'number_class_c+1',True,"Flight_id",FlightId,True)
            xdb.UpdateOne("Number_of_passenger",'Number_of_passenger+1',True,"Flight_id",FlightId,True)
        for i in range(int(Child)):
            Name = request.form.get(f"CName{i}")
            Age = request.form.get(f"CAge{i}")
            Passport = request.form.get(f"CPassportNumber{i}")
            BookingId =int( xdb.SelectOneWhere("Number_of_passenger","Flight_id",FlightId,True))
            Disease = request.form.get(f"CDiseace{i}")
            db.InsertAll([BookingId,False],[FlightId,False],['Dependent',True],[Age,False],[Name,True],[Payment,True],[Disease,True],[Passport,False],[Class,True],[Price,False])
            pdb.InsertAll([UserId,False],[BookingId,False])
            ddb.InsertAll([Name,True],[UserId,False])
            tdb.InsertAll([FlightId,False],[BookingId,False],['Booking',True])
            if Class == "A":
                xdb.UpdateOne("number_class_a",'number_class_a+1',True,"Flight_id",FlightId,True)
            elif Class == "B":
                xdb.UpdateOne("number_class_b",'number_class_b+1',True,"Flight_id",FlightId,True)
            else:
                xdb.UpdateOne("number_class_c",'number_class_c+1',True,"Flight_id",FlightId,True)
            xdb.UpdateOne("Number_of_passenger",'Number_of_passenger+1',True,"Flight_id",FlightId,True)

        for i in range(int(Baby)):
            pass

    return render_template("Passenger Side/Cancel Book.html" , title = "Cancel Book Page" , ComName = CompanyName)


@app.route('/CancelBook'  , methods= ["POST" ,"GET"])
def CancelBook():
    if request.method == "POST":
        Id = request.form.get("Id")
        db = Database.DB("booking")
        pdb = Database.DB("passenger_booking")
        ddb = Database.DB("dependant")
        tdb = Database.DB("ticket")
        tdb.UpdateOne("Status",'Canceled',False,"booking_id",Id,True)
        var = db.SelectOneWhere("booking_owner","Booking_id",Id,True)
        print(var)
        if var == 'Dependent':
            name = db.SelectOneWhere("name","Booking_id",Id,True)
            ddb.DeleteAllWhere("Dept_name",name,False)
            pdb.DeleteAllWhere("Booking_id",int(Id),True)
            db.DeleteAllWhere("Booking_id",Id,True)
        elif var == 'Self':
            pdb.DeleteAllWhere("Booking_id",int(Id),True)
            db.DeleteAllWhere("Booking_id",Id,True)
    return render_template("Passenger Side/Cancel Book.html" , title = "Cancel Book Page" , ComName = CompanyName)

@app.route('/ModifyBook'  , methods= ["POST" ,"GET"])
def ModifyBook():
    return render_template("Passenger Side/Modify Book.html" , title = "Modify Book Page" , ComName = CompanyName)

@app.route('/SearchTicketClass'  , methods= ["POST" ,"GET"])
def SearchTicketClass():
    if request.method == "POST":
        Id = request.form.get("Id")
        db = Database.DB("booking")
        fdb = Database.DB("flight")
        FlightId = db.SelectOneWhere("Flight_id","Booking_id",Id,True)
        Class = db.SelectOneWhere("class","Booking_id",Id,True)
        Price = db.SelectOneWhere("price","Booking_id",Id,True)
        data = fdb.SelectAllWhere("Flight_id",int(FlightId),True)
    return render_template("Passenger Side/Modify Class.html" , title = "Modify Class Page", ComName = CompanyName , data = data , Class = Class , Price = Price , FlightId = FlightId , Id = Id)

@app.route('/UpdateClass'  , methods= ["POST" ,"GET"])
def UpdateClass():
    if request.method == "POST":
        NewClass = request.form.get("NewClass")
        Class = request.form.get("Class")
        FlightId = int(request.form.get("FlightId"))
        BookingId = int(request.form.get("BookingId"))
        db = Database.DB("flight")
        bdb = Database.DB("booking")

        if Class == 'A':
            db.UpdateOne("number_class_a","number_class_a-1",True,"Flight_id",FlightId,True)
        elif Class == 'B':
            db.UpdateOne("number_class_b","number_class_b-1",True,"Flight_id",FlightId,True)
        elif Class == 'C':
            db.UpdateOne("number_class_c","number_class_c-1",True,"Flight_id",FlightId,True)
        
        if NewClass == 'A':
            db.UpdateOne("number_class_a","number_class_a+1",True,"Flight_id",FlightId,True)
            NewPrice = int(db.SelectOneWhere("pric_class_a","Flight_id",FlightId,True))
        elif NewClass == 'B':
            db.UpdateOne("number_class_b","number_class_b+1",True,"Flight_id",FlightId,True)
            NewPrice = int(db.SelectOneWhere("pric_class_b","Flight_id",FlightId,True))
        elif NewClass == 'C':
            db.UpdateOne("number_class_c","number_class_c+1",True,"Flight_id",FlightId,True)
            NewPrice = int(db.SelectOneWhere("pric_class_c","Flight_id",FlightId,True))
        bdb.UpdateOne("price",NewPrice,True,"Booking_id",BookingId,True)
        bdb.UpdateOne("class",NewClass,False,"Booking_id",BookingId,True)
    return render_template("Passenger Side/Show Avi Flights.html" , title = "Show Avi Flights Page" , ComName = CompanyName)

@app.route('/ShowAviFlights')
def ShowAviFlights():
    return render_template("Passenger Side/Show Avi Flights.html" , title = "Show Avi Flights Page" , ComName = CompanyName)

@app.route('/TripsHistory')
def TripsHistory():
    return render_template("Passenger Side/Trips History.html" , title = "Trips History Page" , ComName = CompanyName)

if __name__ ==  "__main__":
    app.run()