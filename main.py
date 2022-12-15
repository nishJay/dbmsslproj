from tkinter import *
import sys
import sqlite3

# Create the main window
window = Tk()
window.title("Recipe Suggestor")
window.geometry("400x400")
frame = Frame(window)
frame.pack()

# Create an IntVar for each checkbox



# Create the checkboxes
choices = ["Rava Dosa","Masala Dosa"]
checkbox = []
state = []
selected = []
results = []
for i in range(len(choices)):
    checkbox.append(IntVar())
    Checkbutton(window,text = choices[i], variable = checkbox[i]).pack()
    


def enter_data():    
    for i in range(len(choices)):
        state.append(checkbox[i].get())
        if(state[i] == 1):
            selected.append(choices[i])
    print(selected)
    for i in selected:
        print(i)
        cursor.execute("SELECT * FROM Dish WHERE Dish_name = '{i}'")
        results = cursor.fetchall()
        print(results)
    for result in results:
        label = Label(text=result)
        label.pack()
    conn.commit()
    conn.close()
    
        
           
        

button = Button(frame, text="Submit", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)





# Table creation
conn = sqlite3.connect('recipe.db')
table_create_query = ['''CREATE TABLE IF NOT EXISTS Ingredients
                    (Ing_ID TEXT PRIMARY KEY , Ing_name TEXT)''',
                    '''CREATE TABLE IF NOT EXISTS Dish
                    (Dish_ID TEXT PRIMARY KEY , Dish_name TEXT, Steps TEXT)''',
                    '''CREATE TABLE IF NOT EXISTS Type
                    (Type_ID TEXT PRIMARY KEY, Type_name TEXT)''',
                    '''CREATE TABLE IF NOT EXISTS Ing_Dish
                    (Ing_ID TEXT, Dish_ID TEXT, FOREIGN KEY(Ing_ID) REFERENCES Ingredients(Ing_ID)
                    , FOREIGN KEY(Dish_ID) REFERENCES Dish(Dish_ID))''',
                    '''CREATE TABLE IF NOT EXISTS Type_Dish
                    (Type_ID TEXT, Dish_ID TEXT, FOREIGN KEY(Type_ID) REFERENCES Type(Type_ID)
                    , FOREIGN KEY(Dish_ID) REFERENCES Dish(Dish_ID))''',
                    ]
cursor = conn.cursor()
for i in table_create_query:
    conn.execute(i)

#conn.execute("INSERT INTO Dish VALUES (?, ?,?)", ("D1","Masala Dosa","Batter"))










# Start the main loop
window.mainloop()
