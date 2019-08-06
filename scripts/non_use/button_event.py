from tkinter import *
 
def my_fun(event):
    print("Function called") 
    

win = Tk()

button = Button(win, text="Click me")
button.bind("<Button-1>", my_fun)
button.pack()

win.mainloop()