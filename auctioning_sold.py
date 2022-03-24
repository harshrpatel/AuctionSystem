# Import module
from tkinter import *
import json
import sys

final_list = []
final_dict = {
                'player': '',
                'type': '',
                'team': '',
                'base_price': ''
            }

with open('db', 'r') as fdb:
    lines = fdb.readlines()

    for line in lines:
        temp_final_dict = {}
        l1 = line.split('\t', 3)
        temp_final_dict['player'] = l1[0]
        temp_final_dict['type'] = l1[1]
        temp_final_dict['team'] = l1[2]
        temp_final_dict['price'] = l1[3]
        final_list.append(temp_final_dict)

# Create object
root = Tk()

# Adjust size
root.geometry("800x500")
root['bg'] = '#FFC0CB'
TEAMS = {'Aayushi': [], 'Harsh': [], 'Adi': [],
         'Nakul': [], 'Chirag': [], 'Umang': [],
         'Meet': [], 'Harshil': [], 'Kenul': []}


def auction(team_name, player_name, sold_price):

    teamname = str(team_name)
    playername = str(player_name)
    soldprice = str(sold_price)
    if teamname not in list(TEAMS.keys()):
        print("INVALID TEAM")
        sys.exit(0)
    for i in range(len(final_list)):
        if final_list[i]['player'] == playername:
            final_list[i]['sold_price'] = soldprice
            TEAMS[teamname].append(final_list[i])
    print(TEAMS)
    with open('final_teams', 'w') as ftd:
        ftd.write(json.dumps(TEAMS))

# Change the label text
def show():
    var1 = clicked.get()
    print(var1)
    label.config( text = clicked.get() )


def show1():
    sellPrice = player_name.get()
    playerName = clicked.get()
    teamName = clicked1.get()
    print("!!!!!", playerName, teamName, sellPrice)
    auction(teamName, playerName, sellPrice)
    label.config( text = playerName )


# Dropdown menu options
options = [i['player'] for i in final_list]
options1 = list(TEAMS.keys())
# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("M S Dhoni")

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
print("!!!", clicked.get())
# button = Button( root , text = "click Me" , command=show).pack()

# Create Label
label = Label( root , text = " " )
label.pack()


clicked1 = StringVar()

# initial menu text
clicked1.set("Harsh")

# Create Dropdown menu
drop = OptionMenu( root , clicked1 , *options1 )
drop.pack()

# Create button, it will change label text
button1 = Button( root , text = "PLAYER SOLD" , command=show1).pack()

# Create Label
label = Label( root , text = " " )
label.pack()



player_name = Entry(root)
Label(root, text="Sell Price Player").pack()
player_name.pack(pady=30)

root.mainloop()
