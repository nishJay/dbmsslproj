from tkinter import *
import sqlite3

# Create the main window
window = Tk()
window.title("Recipe Suggestor")
frame = Frame(window)
frame.pack()

# Create an IntVar for each checkbox

checkbox1_var = IntVar()


# Create the checkboxes
choices = ["Rava Dosa"]
checkbox = []
state = []
selected = []
for i in range(len(choices)):
    checkbox.append(IntVar())
    Checkbutton(window,text = choices[i], variable = checkbox[i]).pack()
    state.append(checkbox[i].get())
    

def enter_data():
    for i in range(len(choices)):
        if(state[i]):
            selected.append(choices[i])
        print(state)
        print(selected)
           
        

button = Button(frame, text="Submit", command= enter_data())
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

#conn.execute("INSERT INTO Dish VALUES (?, ?,?)", ("D2", "Masala Dosa","Masala Dosa Recipe"))



for i in selected:
    cursor.execute("SELECT * FROM Dish WHERE Dish_name = ?",(i))
results = cursor.fetchall()

for result in results:
    label = Label(text=result)
    label.pack()




conn.commit()
conn.close()

# Start the main loop
window.mainloop()
