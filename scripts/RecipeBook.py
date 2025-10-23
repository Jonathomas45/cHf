import pandas as pd
from scripts.Style import Cleanup


# Declares path to location of "recipes.csv"
path = "datasets/recipes.csv"
# Pulls data from path location and makes it into a pandas dataframe
df = pd.read_csv(path)

# Convert entire DataFrame to list of dictionaries
recipes = df.to_dict(orient="records")


# This captures the first line from data in 'df' and makes a list of headers
headers = pd.read_csv(path, nrows=0).columns.tolist()
#(no longer) Removes the unnecessary unnamed list item -- learned that the first empty comma is for indexing
#headers.pop(0)

#length of recipes list
quan = len(recipes) 
i = 0
# Temp initiation of list for the meal names.
meal_names = []
while i < quan:
    meal = recipes[i]['recipe_name']
    meal_names.append(meal)
    i += 1

df = pd.DataFrame(meal_names, columns=["recipe_name"])
df.drop_duplicates(subset="recipe_name", keep="first")
df.to_csv("datasets/meal_names.csv", index=False)

class Structure:
    '''
    I want the structure class to build out to make the headers:
    recipe_name:
    total_time:
    ingredients:
    nutrition: 

    Readable as a presenation 
    '''
    
    def __init__(self, recipe_name):
        '''
            uses string of recipe_name variable to validate it and index it from meal_names. 
        
        '''
    
        self.intro_view = [headers[0],headers[3],headers[6], headers[11]]
        self.recipe_name = recipe_name
        self.validate()
      
    def validate(self):
        if self.recipe_name in meal_names:
            meal_index =meal_names.index(self.recipe_name)
            self.snap(self.recipe_name, meal_index)
            #print("this is validate")
            self.display(meal_index)

           
        else:
            print(self.recipe_name +" is not in our recipe book")
        
        
    def snap(self,name, index):
        self.name = name
        self.index = index
        self.capture = [self.name, self.index]
        #print("Snap")
        
     

    def display(self, index):
        '''
        The display function captures the intro_view list of headers to display
        a readable description of the recipe. 
        '''
      

        self.index = index
        for header in self.intro_view:
            string = str(recipes[index][header])
            if header in "ingredients nutrition":
                
                Cleanup.indent(header, string)
            else:
                print(header.capitalize()+': '+ string.center(50, '='))
                
            


