from tkinter import *
from tkinter import ttk

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

    pvpButton = Button(mainFrame, text="PVP", font=('Comic Sans MS', 30, 'bold'), bg='#639fff', command=pvpButtonLogic)
    pvpButton.pack(expand=TRUE, fill="both")
    createSmallSpace()
    pviButton = Button(mainFrame, text="PVI", font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
    pviButton.pack(expand=TRUE, fill="both")
    createSmallSpace()
    backButton = Button(mainFrame, text="Back", font=('Comic Sans MS', 20, 'bold'), bg='#639fff', command=backButtonLogic)
    backButton.pack(expand=TRUE, fill="both")


def pvpButtonLogic():
    for x in mainFrame.winfo_children():
        x.destroy()

    

    createBigSpace()
    mainTittle = Label(mainFrame, text="Rock, Papper, Sissors - DELUXE", font=('Comic Sans MS', 40, 'bold'), fg='black', bg='#639fff', relief=RAISED, bd=10)
    mainTittle.pack(expand=TRUE, fill="both")
    createBigSpace()
   
    continueButton = Button(mainFrame, text="Continue", font=('Comic Sans MS', 20, 'bold'), bg='#639fff', command=continueButtonLogic)
    continueButton.pack(expand=TRUE, fill="both")

def continueButtonLogic():

    i = TRUE
    if i:
        entryBox = Entry(mainFrame, font=('Comic Sans MS', 30, 'bold'))
        entryBox.pack(expand=TRUE, fill="both")
        i == FALSE

    players = ["Player 1","Player 2"]

    for x in players:
        x = entryBox.get()
        entryBox.delete(0, END)
        print(x)




    




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

