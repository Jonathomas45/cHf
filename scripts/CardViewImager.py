import pandas as pd
from scripts.RecipeBook import Structure
import contextlib



path = "datasets/meal_names.csv"
df = pd.read_csv(path)
meals = df.to_dict(orient="list")
with open("cardview.txt", "w", encoding="utf-8") as f:
    with contextlib.redirect_stdout(f):
        for meal in meals['recipe_name']:
            Structure(meal)
            print("\n")

