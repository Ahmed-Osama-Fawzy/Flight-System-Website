import pyodbc , os
class DB:
    Tablename = ''
    server = '(local)'  # Replace with your server name or IP address
    database = 'System'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    Cols = ''

    def __init__(self , T ):
        self.Tablename = T

    def Create(self ,*Data):
        try:
            with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                M = ''
                for One in Data:
                    M += f"{One[0]} {One[1]} {One[2]},"
                XM = M.rstrip(",")
                cur.execute(f"CREATE TABLE IF NOT EXISTS {self.Tablename}({XM})")
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()
    
    
    def SelectAll(self):
        try:
            with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                cur.execute(f"SELECT * FROM {self.Tablename}")
                data = [list(tup) for tup in cur.fetchall()]
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()
        return data
    
    def SelectOne(self,Col):
        try:
            with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                cur.execute(f"SELECT {Col} FROM {self.Tablename}")
                data = cur.fetchall()
                con.commit()
                return data
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()
    def SelectOneWithOutDeplic(self,Col):
        try:
            with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                cur.execute(f"SELECT DISTINCT {Col} FROM {self.Tablename};")
                data = cur.fetchall()
                con.commit()
                return data
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()
    
    def SelectAllWhere(self , Key , Value, Numrical = True):
        try:
            with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                if Numrical == True:
                    cur.execute(f"SELECT * FROM {self.Tablename} WHERE {Key} = {Value}")
                else:
                    cur.execute(f"SELECT * FROM {self.Tablename} WHERE {Key} = '{Value}'")
                data = [list(tup) for tup in cur.fetchall()]
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()
        return data
    
    def SelectAllTWhere(self , Key , Value, Numrical , XKey , XValue , XNumrical ):
        try:
            with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                if Numrical == True and XNumrical == True:
                    cur.execute(f"SELECT * FROM {self.Tablename} WHERE {Key} = {Value} AND {XKey} = {XValue}")

                elif Numrical == False and XNumrical == False:
                    cur.execute(f"SELECT * FROM {self.Tablename} WHERE {Key} = '{Value}' AND {XKey} = '{XValue}'")

                elif Numrical == False and XNumrical == True:
                    cur.execute(f"SELECT * FROM {self.Tablename} WHERE {Key} = '{Value}' AND {XKey} = {XValue}")

                elif Numrical == True and XNumrical == False:
                    cur.execute(f"SELECT * FROM {self.Tablename} WHERE {Key} = {Value} AND {XKey} = '{XValue}'")

                data = cur.fetchall()
                con.commit()
                return data
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()
        
    
    
    
    def SelectOneWhere(self , One , Key , Value, Numrical = True):
        try:
            with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                if Numrical == True:
                    cur.execute(f"SELECT {One} FROM {self.Tablename} WHERE {Key} = {Value}")
                else:
                    cur.execute(f"SELECT {One} FROM {self.Tablename} WHERE {Key} = '{Value}'")
                data = cur.fetchall()            
                con.commit()
                return data[0][0]
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()
        
    
    def SelectOneTWhere(self , One , Key , Value, Numrical , XKey , XValue , XNumrical ):
        try:
            with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                if Numrical == True and XNumrical == True:
                    cur.execute(f"SELECT {One} FROM {self.Tablename} WHERE {Key} = {Value} AND {XKey} = {XValue}")

                elif Numrical == False and XNumrical == False:
                    cur.execute(f"SELECT {One} FROM {self.Tablename} WHERE {Key} = '{Value}' AND {XKey} = '{XValue}'")

                elif Numrical == False and XNumrical == True:
                    cur.execute(f"SELECT {One} FROM {self.Tablename} WHERE {Key} = '{Value}' AND {XKey} = {XValue}")

                elif Numrical == True and XNumrical == False:
                    cur.execute(f"SELECT {One} FROM {self.Tablename} WHERE {Key} = {Value} AND {XKey} = '{XValue}'")
                data = cur.fetchall()
                con.commit()
                print(f'From Select Where {data[0][0]}')
                if data:
                    return data[0][0]
                else:
                    return False 
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()


    def SelectFromFlight(self , From , To , Date , Type):
        try:
            with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                if From and To and Date and Type:
                    cur.execute(f"SELECT * FROM flight WHERE Source = '{From}' AND Destination = '{To}' AND Arrival_date = '{Date}' AND flight_type = '{Type}'")
                    data = cur.fetchall()
                    if data:
                        return [data,4,"Success Details"]
                    else:
                        cur.execute(f"SELECT * FROM flight WHERE Source = '{From}' AND Destination = '{To}' AND flight_type = '{Type}'")
                        data = cur.fetchall()
                        if data:
                            return [data,3,"Sorry We Have Not Trips at This Time , This Trips With same Details"]
                        else:
                            cur.execute(f"SELECT * FROM flight WHERE Source = '{From}' AND Destination = '{To}' AND Arrival_date = '{Date}'")
                            data = cur.fetchall()
                            if data:
                                return [data,3,"Sorry We Have Not Trips at This Type , This Trips With same Details"]
                            else:
                                cur.execute(f"SELECT * FROM flight WHERE Source = '{From}' AND Destination = '{To}'")
                                data = [cur.fetchall(),2,"Sorry We Have Not Trips at This Time & Type , This Trips With same Details"]
                                return data
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()

    
    def SelectManyWhere(self , Many , Key , Value, Numrical = True):
        try:
            with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                M = ''
                for One in Many:
                    M += f"{One},"
                XM = M.rstrip(",")
                if Numrical == True:
                    cur.execute(f"SELECT {XM} FROM {self.Tablename} WHERE {Key} = {Value}")
                else:
                    cur.execute(f"SELECT {XM} FROM {self.Tablename} WHERE {Key} = '{Value}'")
                data = cur.fetchall()
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()
        return data
    

    def InsertAll(self , *Many):
        try:
           with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                M = ''
                for One in Many:
                    if One[1] == True:
                        M+=f"'{One[0]}',"
                    elif One[1] == False:
                        M+=f"{One[0]},"
                XM = M.rstrip(",")
                cur.execute(f"INSERT INTO {self.Tablename} VALUES({XM})")
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()
    

    def InsertOne(self ,Key , Value , Numrical ):
        try:
           with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                if Numrical == True:
                    cur.execute(f"INSERT INTO {self.Tablename}({Key}) VALUES({Value})")
                else:
                    cur.execute(f"INSERT INTO {self.Tablename}({Key}) VALUES('{Value}')")
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()
        


    def DropTable(self):
        try:
           with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                cur.execute(f"DROP TABLE IF EXISTS {self.Tablename}")
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()



    def ClearTable(self):
        try:
           with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                cur.execute(f"DELETE FROM {self.Tablename}")
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()



    def DeleteAllWhere(self ,Key , Value , Numrical ):
        try:
           with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                if Numrical == True:
                    cur.execute(f"DELETE FROM {self.Tablename} WHERE {Key} = {Value}")
                else:
                    cur.execute(f"DELETE FROM {self.Tablename} WHERE {Key} = '{Value}'")
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()



    def UpdateOne(self , Key , Value , Numrical , XKey , XValue , XNumarical ):
        try:
           with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                if Numrical == True and XNumarical == True:
                    cur.execute(f"UPDATE {self.Tablename} SET {Key} = {Value} WHERE {XKey} = {XValue}")

                elif Numrical == False and XNumarical == False:
                    cur.execute(f"UPDATE {self.Tablename} SET {Key} = '{Value}' WHERE {XKey} = '{XValue}'")
                
                elif Numrical == True and XNumarical == False:
                    cur.execute(f"UPDATE {self.Tablename} SET {Key} = {Value} WHERE {XKey} = '{XValue}'")

                elif Numrical == False and XNumarical == True:
                    cur.execute(f"UPDATE {self.Tablename} SET {Key} = '{Value}' WHERE {XKey} = {XValue}")
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()



    def UpdateMany(self ,*Many , XKey , XValue , XNumarical ):
        try:
           with pyodbc.connect(DB.connection_string) as con :
                cur = con.cursor()
                for One in Many:
                    if One[2] == True and XNumarical == True:
                        cur.execute(f"UPDATE {self.Tablename} SET {One[0]} = {One[1]} WHERE {XKey} = {XValue}")

                    elif One[2] == False and XNumarical == False:
                        cur.execute(f"UPDATE {self.Tablename} SET {One[0]} = '{One[1]}' WHERE {XKey} = '{XValue}'")
                    
                    elif One[2] == True and XNumarical == False:
                        cur.execute(f"UPDATE {self.Tablename} SET {One[0]} = {One[1]} WHERE {XKey} = '{XValue}'")

                    elif One[2] == False and XNumarical == True:
                        cur.execute(f"UPDATE {self.Tablename} SET {One[0]} = '{One[1]}' WHERE {XKey} = {XValue}")
                con.commit()
        except pyodbc.Error as er:
            print(er)
        finally:
            con.close()