from tkinter import *
from tkinter import ttk
import random

def createBigSpace():
    bigSpace = Label(mainFrame, text=" ", font=('Comic Sans MS', 110, 'bold'), bg='#9cc2ff')
    bigSpace.pack(expand=TRUE, fill="both")

def createSmallSpace():
    smallSpace = Label(mainFrame, text=" ", font=('Comic Sans MS', 10, 'bold'), bg='#9cc2ff')
    smallSpace.pack(expand=TRUE, fill="both")

def backButtonLogic():
    mainMenu()

def playButtonLogic():
    for x in mainFrame.winfo_children():
        x.destroy()

    createBigSpace()
    mainTittle = Label(mainFrame, text="Rock, Papper, Sissors - DELUXE", font=('Comic Sans MS', 40, 'bold'), fg='black', bg='#639fff', relief=RAISED, bd=10)
    mainTittle.pack(expand=TRUE, fill="both")
    createBigSpace()

    pvpButton = Button(mainFrame, text="PVP", font=('Comic Sans MS', 30, 'bold'), bg='#639fff')#, command=pvpButtonLogic)
    pvpButton.pack(expand=TRUE, fill="both")
    createSmallSpace()
    pviButton = Button(mainFrame, text="PVI", font=('Comic Sans MS', 30, 'bold'), bg='#639fff', command= pviButtonLogic)
    pviButton.pack(expand=TRUE, fill="both")
    createSmallSpace()
    backButton = Button(mainFrame, text="Back", font=('Comic Sans MS', 20, 'bold'), bg='#639fff', command=backButtonLogic)
    backButton.pack(expand=TRUE, fill="both")

#def pvpButtonLogic():
#    for x in mainFrame.winfo_children():
#        x.destroy()

#    choice = IntVar()
#    textMessage = "."


#    createBigSpace()
#    mainTittle = Label(mainFrame, text="Rock, Papper, Sissors - DELUXE", font=('Comic Sans MS', 40, 'bold'), fg='black', bg='#639fff', relief=RAISED, bd=10)
#    mainTittle.pack(expand=TRUE, fill="both")
#    createBigSpace()
#    messageBox = Label(mainFrame, text="You selected " + textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
#    messageBox.pack(expand=TRUE, fill="both")
#    createSmallSpace()
#
#    def gameLogic():
#        if (choice.get() == 0):
#            messageBox.destroy()
#            textMessage = "Rock"
#            messageBox = Label(mainFrame, text="You selected " + textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
#            messageBox.pack(expand=TRUE, fill="both")
 #       elif (choice.get() == 1):
 #           messageBox.destroy()
 #           textMessage = "Papper"
#            createSmallSpace()
#            messageBox = Label(mainFrame, text="You selected " + textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
#            messageBox.pack(expand=TRUE, fill="both")
#        elif (choice.get() == 2):
#            messageBox.destroy()
#            textMessage = "Scissor"
#            createSmallSpace()
#            messageBox = Label(mainFrame, text="You selected " + textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
#            messageBox.pack(expand=TRUE, fill="both")
#
#    for index in range(len(listRPS)):
#        userChoice = Radiobutton(mainFrame, text=listRPS[index], variable=choice, value=index, indicatoron=0, font=('Comic Sans MS', 20, 'bold'), bg='#639fff', command=gameLogic)
#        userChoice.pack(expand=TRUE, fill="both")
#        createSmallSpace()
#    backButton = Button(mainFrame, text="Back", font=('Comic Sans MS', 20, 'bold'), bg='#639fff', command=backButtonLogic)
 #   backButton.pack(expand=TRUE, fill="both")

def pviButtonLogic():
    for x in mainFrame.winfo_children():
        x.destroy()

    choice = IntVar()
    createBigSpace()
    mainTittle = Label(mainFrame, text="Rock, Papper, Sissors - DELUXE", font=('Comic Sans MS', 40, 'bold'), fg='black', bg='#639fff', relief=RAISED, bd=10)
    mainTittle.pack(expand=TRUE, fill="both")
    createBigSpace()

    def gameLogic():
        textMessage = " "
        createSmallSpace()
        messageBox = Label(mainFrame, text= textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
        messageBox.pack(expand=TRUE, fill="both")
        messageBox.destroy()
        aiChoice = random.choice(listRPS)

        if choice.get() == aiChoice:
            textMessage = "It's a DRAW"
            messageBox.destroy()
            createSmallSpace()
            messageBox = Label(mainFrame, text= textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
            messageBox.pack(expand=TRUE, fill="both")
            createSmallSpace()
        elif choice.get() == 0:
            if aiChoice == "Papper":
                textMessage ="Papper beats Rock, the AI WINS"
                messageBox.destroy()
                createSmallSpace()
                messageBox = Label(mainFrame, text= textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
                messageBox.pack(expand=TRUE, fill="both")
                createSmallSpace()
            else:
                textMessage = "Rock beats Sissors, Player 1 WINS"
                messageBox.destroy()
                createSmallSpace()
                messageBox = Label(mainFrame, text= textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
                messageBox.pack(expand=TRUE, fill="both")
                createSmallSpace()
        elif choice.get() == 2:
            if aiChoice == "Rock":
                textMessage = "Rock beats Sissors, the AI WINS"
                messageBox.destroy()
                createSmallSpace()
                messageBox = Label(mainFrame, text= textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
                messageBox.pack(expand=TRUE, fill="both")
                createSmallSpace()
            else:
                textMessage = "Sissor beats Papper, Player 1 WINS"
                messageBox.destroy()
                createSmallSpace()
                messageBox = Label(mainFrame, text= textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
                messageBox.pack(expand=TRUE, fill="both")
                createSmallSpace()
        elif choice.get() == 1:
            if aiChoice == "Rock":
                textMessage = "Papper beats Rock, Player 1 WINS"
                messageBox.destroy()
                createSmallSpace()
                messageBox = Label(mainFrame, text= textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
                messageBox.pack(expand=TRUE, fill="both")
                createSmallSpace()
            else:
                textMessage = "Sissor beats Papper, the AI WINS"
                messageBox.destroy()
                createSmallSpace()
                messageBox = Label(mainFrame, text= textMessage, font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
                messageBox.pack(expand=TRUE, fill="both")


    for index in range(len(listRPS)):
        userChoice = Radiobutton(mainFrame, text=listRPS[index], variable=choice, value=index, indicatoron=0, font=('Comic Sans MS', 20, 'bold'), bg='#639fff', command=gameLogic)
        userChoice.pack(expand=TRUE, fill="both")
        createSmallSpace()
    backButton = Button(mainFrame, text="Back", font=('Comic Sans MS', 20, 'bold'), bg='#639fff', command=backButtonLogic)
    backButton.pack(expand=TRUE, fill="both")
    


def mainMenu():

    for x in mainFrame.winfo_children():
        x.destroy()

    createBigSpace()
    mainTittle = Label(mainFrame, text="Rock, Papper, Sissors - DELUXE", font=('Comic Sans MS', 40, 'bold'), fg='black', bg='#639fff', relief=RAISED, bd=10)
    mainTittle.pack(expand=TRUE, fill="both")
    createBigSpace()

    playButton = Button(mainFrame, text="Play", font=('Comic Sans MS', 30, 'bold'), bg='#639fff', command=playButtonLogic)
    playButton.pack(expand=TRUE, fill="both")
    createSmallSpace()
    optionsButton = Button(mainFrame, text="Options", font=('Comic Sans MS', 20, 'bold'), bg='#639fff')
    optionsButton.pack(expand=TRUE, fill="both")
    createSmallSpace()
    exitButton = Button(mainFrame, text="Exit", font=('Comic Sans MS', 20, 'bold'), bg='#639fff', command= window.destroy)
    exitButton.pack(expand=TRUE, fill="both")


listRPS = ["Rock", "Papper", "Scissor"]
player2Choice = " "



window = Tk()

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry(str(width) + "x" + str(height))
window.config(background="#9cc2ff")
window.title("Rock, Paper, Sissors - DELUXE")
window.attributes('-fullscreen', TRUE)


mainFrame = Frame(window)
mainFrame.pack()

mainMenu()

window.mainloop()

