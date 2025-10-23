from scripts.RecipeBook import *




def cleanup():
    string = recipes[Structure("Apple Crisp").index][headers[6]]
    string.replace(",", "\n") 

    print(string)


# 
sg = 'hello'
 
print(sg.center(50, " "))
