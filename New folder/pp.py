import pyodbc

server = '(local)'  # Replace with your server name or IP address
database = 'System' # Replace with your database name
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
conn = pyodbc.connect(connection_string)
cur = conn.execute("SELECT User_id FROM [User]")
for row in cur.fetchall():
    print(row[0])






