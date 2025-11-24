from tkinter import *

root = Tk()

root.title("Welcome to Python")
root.geometry('350x200')

lbl = Label(root,text="Are you python developer?")
lbl.grid()

txt = Entry(root,width=10)
txt.grid(column=1,row=0)


def clicked():
    res = "You wrote "+ txt.get()
    lbl.configure(text=res)
    txt.destroy()

btn = Button(root, text="Click me",fg='red',command=clicked)
btn2=Button(root,text="Check Out",fg="green",command="Push Me")

btn.grid(column=2,row=0)


root.mainloop()