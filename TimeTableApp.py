from tkinter import *

root = Tk()

i = 0


def reset():
    print("RESET")
    list = root.grid_slaves()
    for l in list:
        l.destroy()

def addItem(string1, string2, colour):
    global i
    string1 = Label(root, text=string1, bg=colour, highlightthickness=10, relief="solid")
    string2 = Label(root, text=string2, bg=colour, highlightthickness=10, relief="solid")
    string1.grid(row=i, column=0, sticky=N)
    string2.grid(row=i, column=1, sticky=N)
    i += 1


def mainFunc():
    colour = ""
    lesson = input("What lesson do want to add? ")
    time = input("What time is it at? ")
    if lesson == "English":
        colour = "cyan"
    elif lesson == "Maths":
        colour = "magenta"
    elif lesson == "Biology":
        colour = "green"
    elif lesson == "Chemistry":
        colour = "blue"
    elif lesson == "Physics":
        colour = "red"
    elif lesson == "History":
        colour = "yellow"
    else:
        colour = "white"
    addItem(lesson, time, colour)









#****** MAIN MENU ******

dropDownMenu = Menu(root)
root.config(menu=dropDownMenu) #configuring the dropDownMenu object as a menu

subMenu = Menu(dropDownMenu)
dropDownMenu.add_cascade(label="Menu", menu=subMenu)#adds drop down functionality and says which menu is activated onclick
subMenu.add_command(label="Reset", command=reset)
subMenu.add_command(label="Add Item", command=mainFunc)




#******CODE RUN******

mainFunc()


root.mainloop()




