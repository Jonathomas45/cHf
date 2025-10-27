#Mysql_servercommunication
import mysql.connector

connection = mysql.connector.connect(user='root', password='Password', host='localhost')

def ShowDBs():
    s = connection.cursor()
    s.execute('SHOW DATABASES')
    for (db_name,) in s.fetchall():

        print(db_name)

class DB():

    def __init__(self, database):
        self.database = database
        pwrd = input(f'What is your password for {self.database}:')
        self.conn = mysql.connector.connect(
            user='root',
            password=pwrd,
            host='localhost',
            database=database
        )
        self.cursor = self.conn.cursor()
        print(f"Connected to database: {self.database}")
    
    def Table(self, name, cols: dict = None):
        return Table(self, name, cols)

    
        
class Table():
    def __init__(self, DB, name, cols: dict = None):
        self.DB = DB
        self.name = name
        self.cols = cols or {}
        self.cursor = self.DB.cursor

    def create(self):
        col_def = ", ".join(f"{k} {v}" for k, v in self.cols.items())
        print(col_def)
        sql = f"CREATE TABLE IF NOT EXISTS {self.name} ({col_def})"
        self.cursor.execute(sql)
        self.DB.conn.commit()
        print(f"Table '{self.name}' created successfully in database '{self.DB.database}'!")
        return self
    
    def categorize(self, col: str = None):
        self.col = col or '*'
        self.cursor.execute(f"SELECT {self.col} FROM {self.DB.database}.{self.name}")
        print(self.cursor.column_names)
        print(self.cursor.fetchall())
        
    
headers = ['id',"col3",'name']


main = DB("test").Table("TESTTABLE")
main.categorize(f"{headers[0]},{headers[1]}")

          
ShowDBs()

    
