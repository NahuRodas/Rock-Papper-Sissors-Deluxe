from tkinter import *
import pyautogui

def createSubMenu():
    width, height= pyautogui.size()
    subMenu = Tk()

    icon = PhotoImage(file = 'Resourses\\icon.png')

    subMenu.geometry(str(width)+"x"+str(height))
    subMenu.title("Rock, Paper, Sissors - DELUXE")
    subMenu.iconphoto(True,icon)
    subMenu.config(background="#9cc2ff")


    mainTittle = Label(subMenu, text="Rock, Papper, Sissors - DELUXE", font=('Comic Sans MS', 40, 'bold'), fg='black', bg='#639fff', relief=RAISED, bd=10, padx=20, pady=20)
    mainTittle.place(x = (width/3.5), y =(height/6))



    subMenu.mainloop()