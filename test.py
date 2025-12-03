import pandas as pd
import numpy as np
from scripts.DataComm import *

db = DB("test")
testtable = db.Table(name="testtable")
conn = db.conn
# this just shows the column names for now but will be more dynamic to show more rows, and will utilize the SELECT from MySQL
testtable.categorize()

def c():
    Table(table_name="testtable2").Create()
    cursor = conn.cursor
    cursor.execute("SHOW Tables;")
    conn.commit 

# example of how to insert data into the database  
def tabletest():
    Table(name="testtable").feed('recipes')
    

def junk():
    # Declares path to location of "recipes.csv"
    path = "datasets/recipes.csv"
            # Pulls data from path location and makes it into a pandas dataframe
    df = pd.read_csv(path)

        # Convert entire DataFrame to list of tuples for mysql script and replacing nan to None to make SQL safe
    df = df.replace({np.nan: None})  
    recipes = list(df.itertuples(index=False, name=None))


            # This captures the first line from data in 'df' and makes a list of headers
            #(no longer) Removes the unnecessary unnamed list item -- learned that the first empty comma is for indexing
            #headers.pop(0)
    for m in recipes[:][0]:
        print(type(m))
        print(m) 

c()