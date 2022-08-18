from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:      #Here the buttons are not a list but a list of buttons
                                                                            #hence lets us take a button b1 so b1['text'] would be 
        if player == players[0]:                                            #the same as b1.config(text="Any Text")
            buttons[row][column]['text'] = player                           #hence putting button b1="Any Text" would be devoid of 
                                                                            #logic as it would be equalling button to a variable                  
            if check_winner() is False:                                     #hence buttons inner text should be equal to "Any Text"
                player = players[1]
                label.config(text=(players[1]+" turn"))
            
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
            
            elif check_winner() == "Tie":
                label.config(text="Tie!")
        
        else:
            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
            
            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))
            
            elif check_winner() == "Tie":
                label.config(text="Tie!")
def check_winner():
    
    for row in range(3):
        
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    
    for column in range(3):
        
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    else:
        return False

def empty_spaces():
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    
    if spaces == 0:
        return False
    
    else:
        return True

def new_game():
    
    global player
    player = random.choice(players)
    label.config(text=player+" turn")
    
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")
HEIGHT=500
WIDTH=500

window = Tk()
window.title("Tic-Tac-Toe")
screen_width=window.winfo_screenwidth()     #gets the distance of screen
screen_height=window.winfo_screenheight()
length_width=int((screen_width/2)-(WIDTH/2))    #essentialy putting it in the centre of the screen
length_height=int(((screen_height)/2)-(HEIGHT/2))
window.geometry("{}x{}+{}+{}".format(WIDTH,HEIGHT,length_width,length_height))

players = ["X","O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn",font=('Bahnschrift SemiLight SemiConde',15),width=90,height=3,bg="Red")
label.pack(side="top")

reset_button = Button(text="restart", font=('Bahnschrift SemiLight SemiConde',15), command=new_game)
reset_button.pack(side="top")

frame = Frame(window,bd=5,relief=RAISED)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('Bahnschrift SemiLight SemiConde',29), width=8, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
#on the left of : are the parameters for the variable row and column (notice the difference in colour if you get confused by the
#two rows and columns)
        buttons[row][column].grid(row=row,column=column)

window.mainloop()