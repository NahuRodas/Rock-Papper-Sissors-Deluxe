from tkinter import *
import pyautogui
import subMenu

width, height= pyautogui.size()

def createSubMenu():
    subMenu = Tk()

    icon = PhotoImage(file = 'Resourses\\icon.png')

    subMenu.geometry(str(width)+"x"+str(height))
    subMenu.title("Rock, Paper, Sissors - DELUXE")
    subMenu.iconphoto(True,icon)
    subMenu.config(background="#9cc2ff")


    mainTittle = Label(subMenu, text="Rock, Papper, Sissors - DELUXE", font=('Comic Sans MS', 40, 'bold'), fg='black', bg='#639fff', relief=RAISED, bd=10, padx=20, pady=20)
    mainTittle.place(x = (width/3.5), y =(height/6))



    subMenu.mainloop()
    
def createWindow():
    newWindow = createSubMenu()
    mainMenu.destroy()


mainMenu = Tk()

icon = PhotoImage(file = 'Resourses\\icon.png')

mainMenu.geometry(str(width)+"x"+str(height))
mainMenu.title("Rock, Paper, Sissors - DELUXE")
mainMenu.iconphoto(True,icon)
mainMenu.config(background="#9cc2ff")


mainTittle = Label(mainMenu, text="Rock, Papper, Sissors - DELUXE", font=('Comic Sans MS', 40, 'bold'), fg='black', bg='#639fff', relief=RAISED, bd=10, padx=20, pady=20)
mainTittle.place(x = (width/3.5), y =(height/6))

playButton = Button(mainMenu, text="Play", font=('Comic Sans MS', 30, 'bold'), bg='#639fff', command=createWindow)
playButton.place(x = (width/2), y =(height/2))

exitButton = Button(mainMenu, text="Exit", font=('Comic Sans MS', 20, 'bold'), bg='#639fff', command=mainMenu.destroy)
exitButton.place(x = (width/2), y =(height/1.6))

mainMenu.mainloop()

