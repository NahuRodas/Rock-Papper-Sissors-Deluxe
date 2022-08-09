from tkinter import *
import pyautogui
import random

width, height= pyautogui.size()

def backButton(window):
    window.destroy 
    if window ==subMenu:
        createMainMenu()     

def createSubMenu():
    subMenu = Tk()

    frame = Frame(subMenu)
    frame.pack(side=TOP)
    framePvp = Frame(subMenu)
    framePvp.pack(side=BOTTOM)
   
    icon2 = PhotoImage(file = 'Resourses\\icon.png')

    subMenu.geometry(str(width)+"x"+str(height))
    subMenu.title("Rock, Paper, Sissors - DELUXE")
    subMenu.iconphoto(True,icon2)
    subMenu.config(background="#9cc2ff")


    mainTittle = Label(frame, text="Rock, Papper, Sissors - DELUXE", font=('Comic Sans MS', 40, 'bold'), fg='black', bg='#639fff', relief=RAISED, bd=10)
    mainTittle.pack(expand=TRUE, fill="both", padx=50, pady=50)

    pvpButton = Button(framePvp, text="PVP", font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
    pvpButton.pack(expand=TRUE, fill="both", side=LEFT)

    pviButton = Button(framePvp, text="PVI", font=('Comic Sans MS', 30, 'bold'), bg='#639fff')
    pviButton.pack(expand=TRUE, fill="both", side=RIGHT)

    backButton = Button(framePvp, text="Back", font=('Comic Sans MS', 30, 'bold'), bg='#639fff', command=backButton(subMenu))
    backButton.pack(expand=TRUE, fill="both", side=RIGHT)


    subMenu.mainloop()


def createMainMenu():
    mainMenu = Tk()

    frame1 = Frame(mainMenu)
    frame1.pack(side=TOP)
    frame2 = Frame(mainMenu)
    frame2.pack(side=BOTTOM)

    icon1 = PhotoImage(file = 'Resourses\\icon.png')

    mainMenu.geometry(str(width)+"x"+str(height))
    mainMenu.title("Rock, Paper, Sissors - DELUXE")
    mainMenu.iconphoto(True,icon1)
    mainMenu.config(background="#9cc2ff")


    mainTittle = Label(frame1, text="Rock, Papper, Sissors - DELUXE", font=('Comic Sans MS', 40, 'bold'), fg='black', bg='#639fff', relief=RAISED, bd=10)
    mainTittle.pack(expand=TRUE, fill="both")

    playButton = Button(frame2, text="Play", font=('Comic Sans MS', 30, 'bold'), bg='#639fff', command=createSubMenu)
    playButton.pack(expand=TRUE, fill="both")

    exitButton = Button(frame2, text="Exit", font=('Comic Sans MS', 20, 'bold'), bg='#639fff', command=mainMenu.destroy)
    exitButton.pack(expand=TRUE, fill="both")

    mainMenu.mainloop()


createMainMenu()