from tkinter import *
import sqlite3

# Create the main window
root = Tk()

# Create an IntVar for each checkbox
checkbox1_var = IntVar()
checkbox2_var = IntVar()
checkbox3_var = IntVar()

# Create the checkboxes
Checkbutton(root, text="Option 1", variable=checkbox1_var).pack()
Checkbutton(root, text="Option 2", variable=checkbox2_var).pack()
Checkbutton(root, text="Option 3", variable=checkbox3_var).pack()

# Retrieve the state of the checkboxes
state1 = checkbox1_var.get()
state2 = checkbox2_var.get()
state3 = checkbox3_var.get()

# Use the retrieved states to update the SQL database
conn = sqlite3.connect('recipe.db')
table_create_query = ['''CREATE TABLE IF NOT EXISTS Ingredients
                    (Ing_ID TEXT PRIMARY KEY AUTOINCREMENT, Ing_name TEXT)''',
                    '''CREATE TABLE IF NOT EXISTS Dish
                    (Dish_ID TEXT PRIMARY KEY AUTOINCREMENT, Dish_name TEXT, Steps TEXT)''',
                    '''CREATE TABLE IF NOT EXISTS Type
                    (Type_ID TEXT PRIMARY KEY AUTOINCREMENT, Type_name TEXT)''',
                    '''CREATE TABLE IF NOT EXISTS Ing_Dish
                    (Ing_ID TEXT, Dish_ID TEXT, FOREIGN KEY(Ing_ID) REFERENCES classes(id))''']
cursor = conn.cursor()
for i in table_create_query:
    conn.execute(i)

conn.commit()
conn.close()

# Start the main loop
root.mainloop()
