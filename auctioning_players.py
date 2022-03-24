from tkinter import *
import random

ws = Tk()
ws.title("IPL AUCTION 2022")
ws.geometry('400x300')
ws['bg'] = '#ffbf00'

called_out_players = []

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


TEAMS = {'A': [], 'B': []}
total_players = [i['player'] for i in final_list]
print("#################################", total_players, "#################################")
global CUR_PLAYER


def register():
    player_info = None
    l3 = [x for x in total_players if x not in called_out_players]
    player = l3.pop(random.randrange(len(l3)))
    for i in final_list:
       if i['player'] == player:
           player_info = i
    called_out_players.append(player)
    print(len(total_players), len(called_out_players), called_out_players)
    return player_info


def printValue():
    di = register()
    Lbl.config(text=f'{di}', font = "Helvetica 32 bold italic", fg = "light green", bg = "dark green")


Lbl = Label(ws, pady=20, bg='#ffbf00')
Button(
    ws,
    text="Next PLAYER for Auction",
    padx=10,
    pady=5,
    command=printValue
    ).pack()

Lbl.pack()
ws.mainloop()
