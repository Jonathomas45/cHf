#Mysql_servercommunication
import mysql.connector
import pandas as pd
import numpy as np

# I need this to make DB() an instant instead so the password won't popping up every use. Is this reinventing the wheel?

class DB():
  # starts the connection from python-->SQL_DB
    def __init__(self, database):
        self.database = database
        pwrd = input(f'What is your password for {self.database}: ')
        self.conn = mysql.connector.connect(
            user='root',
            password=pwrd,
            host='localhost',
            database=database
        )
        self.cursor = self.conn.cursor()
        self.commit = self.conn.commit()
        print(f"Connected to database: {self.database}")
    
    def Table(self, name, cols: dict = None):
        return Table(self, name, cols)
#def 
class Table():

    # collects the table_name database, and column names in a dictionary 
    def __init__(self, DataBase: str, table_name: str, cols: dict = None):
        self.DB = DB("test") # this is a quick fix will make this so the default is test and optional if the use need a different database 
        self.name = table_name 
        self.cols = cols or {}
        self.cursor = self.DB.cursor
    # creates a table 
    def Create(self):
        col_def = ", ".join(f"{k} {v}" for k, v in self.cols.items())
        print(col_def)
        sql = f"CREATE TABLE IF NOT EXISTS {self.name} ({col_def})"
        print(sql)
        self.cursor.execute(sql)
        self.DB.conn.commit()
        print(f"Table '{self.name}' created successfully in database '{self.DB.database}'!")
        return self
    
    def categorize(self, col: str = None):
        self.col = col or '*'
        self.cursor.execute(f"SELECT {self.col} FROM {self.DB.database}.{self.name}")
        print(self.cursor.column_names)
        #print(self.cursor.fetchall()) # data pulled from mysql db
        
    def feed(self, file: str):
        # Declares path to location of "recipes.csv"
        path = f"datasets/{file}.csv"
        # Pulls data from path location and makes it into a pandas dataframe
        df = pd.read_csv(path)
        # Convert entire DataFrame to list of tuples for mysql script & changes the numpy/python nan to mysql friendly None
        df = df.replace({np.nan: None})
        recipes = list(df.itertuples(index=False, name=None))
        #print(recipes[:3])
        # This captures the first line from data in 'df' and makes a list of headers
        headers = pd.read_csv(path, nrows=0).columns.tolist()
        #(no longer) Removes the unnecessary unnamed list item -- learned that the first empty comma is for indexing
        #headers.pop(0)
        placeholders = ', '.join(['%s'] * len(headers))
        sql = f"INSERT INTO {self.name} VALUES ({placeholders})"
        print(sql)
        print(placeholders)
        self.cursor.executemany(sql, recipes)
        self.DB.conn.commit()
        print(self.cursor.rowcount, "was inserted.")


    


    
