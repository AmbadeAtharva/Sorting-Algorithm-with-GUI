from tkinter import *

def open_window():
    top = Toplevel()
    top.title("top window")
    top.geometry("300x300+120+120")
    button1 = Button(top, text="close", command= top.quit).grid(row=3,column=4,padx=5,pady=5)
    

root = Tk()
button = Button(root, text="open window", command = open_window)
button.pack()

root.geometry("300x300+120+120")
root.mainloop()