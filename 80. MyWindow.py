from tkinter import *

wndRoot = Tk()

def btn1_Click():
    text = tbx1.get()
    lbl1.configure(text = text)

tbx1 = Entry(wndRoot)
tbx1.insert(0, "input")
tbx1.pack()

btn1 = Button(wndRoot, text="OK", width=15, command=btn1_Click)
btn1.pack()

lbl1 = Label(wndRoot, text="output")
lbl1.pack()

wndRoot.mainloop()