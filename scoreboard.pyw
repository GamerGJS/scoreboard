from tkinter import *

root = Tk()
root.geometry("800x500")
root.title("SCOREBOARD")
team1 = 0
team2 = 0

def UP1():
    global team1

    team1 = team1 + 1

    TEAM_1.config(text = team1)

def UP2():
    global team2

    team2 = team2 + 1

    TEAM_2.config(text = team2)

def score_reset():
    global team1
    global team2

    team1 = team1 - team1
    
    team2 = team2 - team2

    TEAM_1.config(text = team1)
    
    TEAM_2.config(text = team2)
    
#TEAM 1
Label(root, text="TEAM 1", font=("FRESHMAN", 25), bg="light sea green").place(rely = 0.2, relx = 0.3, anchor=CENTER)
TEAM_1 = Label(root, text=team1, font=("FRESHMAN", 125), bg="light sea green")
TEAM_1.place(rely = 0.5, relx = 0.3, anchor=CENTER)
BUTTONU1 = Button(root, text="+1", font=("Arial", 25), command=UP1).place(rely = 0.8, relx = 0.3, anchor=CENTER)

Label(root, text="-", font=("FRESHMAN", 125), bg="light sea green").place(rely = 0.5, relx = 0.5, anchor=CENTER)

#TEAM 2
Label(root, text="TEAM 2", font=("FRESHMAN", 25), bg="light sea green").place(rely = 0.2, relx = 0.7, anchor=CENTER)
TEAM_2 = Label(root, text=team2, font=("FRESHMAN", 125), bg="light sea green")
TEAM_2.place(rely = 0.5, relx = 0.7, anchor=CENTER)
BUTTONU2 = Button(root, text="+1", font=("Arial", 25), command=UP2).place(rely = 0.8, relx = 0.7, anchor=CENTER)


#RESET
RESET = Button(root, text=" RESET ", font=("Arial", 15), command=score_reset)
RESET.place(rely = 0.8, relx = 0.5, anchor=CENTER)



root.config(bg="light sea green")
root.mainloop()