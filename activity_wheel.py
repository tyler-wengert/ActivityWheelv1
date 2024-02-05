import math
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

category = ['Food', 'Activities', 'Activity + Food']
locations = ['Colorado Springs', 'Denver']

activities_COS = ['The Space Foundation', 'Rail Yard Gaming + Gastropub', 'A1 Fish Arcade', 'Carefree Bingo', 'Bad Axe Throwing', 'Skate City', 'Gold Mine Mini Golf',
                  'Lonees Comedy Corner', 'Dart Wars', 'AirCity360', 'Overdrive Raceway', 'Paint Mines Interpretive Park', 'Poor Richard\'s Book Store']
activities_DEN = ['Chatfield State Park', 'Maroon Bells Guided Tours', 'Ouzel Falls', '88 Drive In Theatre', 'Simply Fashion Boutique', 'Big Soda Lake Beach']
activities_MISC = ['Cherry Springs State Park']

food_COS = ['Cleats Bart and Grill', 'Yellow Mountain Tea House', 'The Old Spaghetti Factory', 'Private Label Distillery', 'Ambli Global Cuisine', 'Cowboy Star',
            '3.14 Pi Bar', 'Bird Dog BBQ', 'Biaggi\'s Ristorante Italiano', 'O\'Furry\'s Sports Bar and Grill', 'Ziggi\'s Coffee', 'Sasquatch Cookies',
            'Cheddar\'s Scratch Kitchen', 'Hungry Howie\'s Pizza', 'Rizuto\'s Ice Cream And Sweet Shop', 'Cy\'s Drive-In Restaurant', 'Paravicini\'s Italian Bistro',
            'Alchemy', 'Dat\'s Italian', 'Westside Cantina', 'Mother Muff\'s Kitchen and Spirits', 'Front Range BBQ', 'Dion\'s', 'Four by Brother Luck', 'Odyssey Gastropub',
            'Carlos\' Bistro', 'The Rabbit Hole', 'Phantom Canyon Brewing Co.', 'Lucky Dumpling', 'Billy\'s Old World Pizza and Italian Cafe', 'The Steakhouse',
            'King\'s Chef Diner', 'Dog Haus', 'Ephemera', 'Streetcar520', 'The Coffee Exchange', 'Frozen Gold', 'The Peppertree Restaurant', 'Shuga\'s', 'HuHot Mongolian Grill',
            'Caffeinated Cow', 'Black Forest Firehouse BBQ', 'Weslet Owens Coffee', 'Judge\'s Char-Grill', 'Gold Tooth Annie\'s']
food_DEN = ['I Heart Mac and Cheese', 'Brothers BBQ', 'Sipp Soda Bar', 'Zero Degrees', 'Punch Bowl Special', 'Postino Broadway', 'Blue Pan Pizza', 'Panaderia el Paisa Bakery', 'Tacos y Salsas', 'Cabrón Carbón Taquería', 'Walter\'s303 - Uptown', 'Giordano\'s']
food_MISC = ['Calivillo\'s Mexican Restaurant']

def pick_item():
    c = cat.get()
    l = loc.get()

    if c == 'Activities' and l == 'Colorado Springs':
        choice = random.choice(activities_COS)
        messagebox.showinfo("Selection", "Youre headed to " + choice )

    if c == 'Food' and l == 'Colorado Springs':
        choice = random.choice(food_COS)
        messagebox.showinfo("Selection", "Youre headed to " + choice)

    if c == 'Activities' and l == 'Denver':
        choice = random.choice(activities_DEN)
        messagebox.showinfo("Selection", "Youre headed to " + choice)

    if c == 'Food' and l == 'Denver':
        choice = random.choice(food_DEN)
        messagebox.showinfo("Selection", "Youre headed to " + choice)

    if c == 'Activity + Food' and l == 'Colorado Springs':
        choice = random.choice(food_COS)
        choice2 = random.choice(activities_COS)
        messagebox.showinfo("Selection", "Youre headed to " + choice2 + " and eating at " + choice)

def callback(eventObject):
    abc = eventObject.widget.get()
    #skill = life.get()
    #index=lifeskills.index(skill)
    #item.config(values=items[index])

#Instantiate the window and name it
win = Tk()
win.title("Activity Selector")

#Add a frame to hold all the widgets
frame = ttk.Frame(win, padding = "5 5 20 20")
frame.grid(column = 0, row = 0, sticky = (N, W, E, S))
win.columnconfigure(0, weight = 1)
win.rowconfigure(0, weight = 1)

#Add dropdown menus
cat = ttk.Combobox(win, width = 30, value=(category))
cat.set('Activities') # default value

loc = ttk.Combobox(win, width = 30, value=(locations))
loc.set("Colorado Springs") # default value

#Entry labels
Label(win, text='Category:').grid(row = 0)
Label(win, text='Location:').grid(row = 1) 

#place entries into the frame
cat.grid(row = 0, column = 1)
loc.grid(row = 1, column = 1)

#bind two menus together
cat.bind('<Button-1>', callback)

#Instantiate a calculate button and place it into the frame
button = Button(win, text='Pick', width=25, bg = 'Green',
                activebackground = 'White', command = lambda: pick_item()) 
button.grid(row = 4)


win.mainloop()
