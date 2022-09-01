from tkinter import *
#from PIL import ImageTk, Image  #for importing images on tkinter window
from random import randint
from tkinter import messagebox 

window = Tk()
window.title("RPS Guessor")

'''window.geometry("500x375")
c = Canvas(window, bg= "black", height = 500, width= 600)
filename = PhotoImage(file="C:\\Users\\SHRI\\OneDrive\\Pictures\\Screenshots\\rock-paper-scissors-neon-icons.png", height= 500, width= 600)
background_label = Label(window,image=filename)
background_label.place(x = 0, y = 0)
'''

window.configure(background = "Black")

image_rock1 = PhotoImage(file="C:\\Users\\SHRI\\OneDrive\\Pictures\\Screenshots\\rock-paper-scissors-icon-16(1).png")
image_paper1 = PhotoImage(file="C:\\Users\\SHRI\\OneDrive\\Pictures\\Screenshots\\rock-paper-scissors-icon-17(1).png")
image_scissor1 = PhotoImage(file="C:\\Users\\SHRI\\OneDrive\\Pictures\\Screenshots\\rock-paper-scissors-icon-15(1).png")

image_rock2 = PhotoImage(file="C:\\Users\\SHRI\\OneDrive\\Pictures\\Screenshots\\rock-paper-scissors-icon-16(1).png")
image_paper2 = PhotoImage(file="C:\\Users\\SHRI\\OneDrive\\Pictures\\Screenshots\\rock-paper-scissors-icon-17(1).png")
image_scissor2 = PhotoImage(file="C:\\Users\\SHRI\\OneDrive\\Pictures\\Screenshots\\rock-paper-scissors-icon-15(1).png")

label_player = Label(window, image= image_scissor1, height = 350, width = 350)
label_computer = Label(window, image = image_scissor2, height = 350, width = 350)
label_player.grid(row =1, column = 4) #right hand side  and horizontal line (for icons)
label_computer.grid(row = 1, column = 0) #left hand side and horizontal line (for icons)

score_computer = Label(window, text = 0, font =("Monaco", 60, "bold",), bg = "black", fg = "green")
score_player = Label(window, text = 0, font =("Monaco", 60, "bold"), bg = "black", fg = "green")
score_computer.grid(row= 1, column = 1)#for scores
score_player.grid(row=1, column=3)


player_indicator = Label(window, font= ("Monaco", 40, "bold"), 
                         text = "Player", bg = "black", fg = "pink")
computer_indicator = Label(window, font= ("Monaco", 40, "bold"), 
                         text = "Computer", bg = "black", fg = "pink")
player_indicator.grid(row = 0, column = 4)#this is so that we can identify which is player and which is computer
computer_indicator.grid(row = 0, column = 0)


#main program

def updateMessage(a):
    final_message["text"] = a #message about winning and losing

def computer_updation():
    final = int(score_computer['text'])
    final += 1
    score_computer['text'] = str(final)

def player_updation():
    final = int(score_player['text'])
    final += 1
    score_player['text'] = str(final)

def winner_check(p,c): #p means player and c means computer
    if p == c:
        updateMessage("It's a Tie")
    elif p == "Rock":
        if c == "Paper":
            updateMessage("Computer Wins!")
            computer_updation()
        else:
            updateMessage("🤩🥳You Win!!🥳🤩")
            player_updation()
    elif p == "Paper":
        if c == "Scissor":
            updateMessage("Computer Wins!")
            computer_updation()
        else:
            updateMessage("🤩🥳You Win!!🥳🤩")
            player_updation()
    elif p == "Scissor":
        if c == "Rock":
            updateMessage("Computer Wins!")
            computer_updation()
        else:
            updateMessage("🤩🥳You Win!!🥳🤩")
            player_updation()
    else:
        pass


#update choices wrt images only so that we have to make list

to_select = ["Rock", "Paper", "Scissor"]

def choice_update(a): #a for user or player
    choice_computer = to_select[randint(0,2)] #here rock will having index 0, paper having index 1 and scissor having index 2
    if choice_computer == "Rock":
        label_computer.configure(image = image_rock2)  #changing image when computer randomly select that particular choice
    elif choice_computer == "Paper":   
        label_computer.configure(image = image_paper2)
    else:
        label_computer.configure(image = image_scissor2)
    
    if a == "Rock":
        label_player.configure(image = image_rock1)
    elif a == "Paper":
        label_player.configure(image = image_paper1)
    else:
        label_player.configure(image = image_scissor1)

    winner_check(a,choice_computer)



final_message = Label(window, font= ("Monaco",20,"bold"), bg = "Black", fg= "Orange")
final_message.grid(row = 3, column = 2)

button_rock = Button(window, width = 16, height = 3, text = "Rock ✊",
                font = ("Monaco",20,"bold"),bg = "Black", fg= 'purple',command= lambda:choice_update("Rock")).grid(row= 2, column = 1)
button_paper = Button(window, width = 16, height = 3, text = "Scissor ✌️",
                font = ("Monaco", 20, "bold"),bg = "Black",fg = 'blue', command= lambda:choice_update("Scissor")).grid(row = 2, column = 2)
button_scissor = Button(window, width = 16, height = 3, text = "Paper 🖐",
                font = ("Monaco", 20, "bold"),bg = "Black",fg = 'yellow', command= lambda:choice_update("Paper")).grid(row = 2, column = 3)



name = Label(window, font= ("Monaco", 18, "italic bold"), text = "By Himanshu", bg = "black", fg = "violet") 
name.grid(row = 3, column = 4)

window.mainloop()