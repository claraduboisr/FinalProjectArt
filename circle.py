import tkinter as tk
import turtle
from tkinter import *
from tkinter import messagebox

def center_window(w=300, h=200):
    # get screen width and height
    ws = root1.winfo_screenwidth()
    hs = root1.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root1.geometry('%dx%d+%d+%d' % (w, h, x, y))

def information():
    tk.messagebox.showinfo("Clara Dubois", "CIRCLE")
    return locals()

def startingwindow(x):
    button1.pack_forget()

    button2 = tk.Button(frame, text="Information", bg="yellow", fg="red", command=information)
    button2.pack(side=tk.LEFT)

    button3 = tk.Button(frame, text="Circle", fg="green", command=circle)
    button3.pack(side=tk.LEFT)

    button4 = tk.Button(frame, text="Close", fg="red", command=quit)
    button4.pack(side=tk.LEFT)

    return locals(), x.pack_forget()

def circle():
    exercise3 = turtle.Turtle()
    exercise3.shape("turtle")
    turtle.title("CIRCLE")

    exercise3.speed(11)

# there will be 37 lines in total but it can be changed
    for i in range(37):
        exercise3.forward(100)
        exercise3.right(50)
        exercise3.forward(20)
        exercise3.left(50)
        exercise3.forward(20)
        exercise3.right(50)
        exercise3.forward(20)
        exercise3.left(50)
        exercise3.forward(20)
        exercise3.right(50)
        exercise3.forward(20)
        exercise3.left(50)
        exercise3.forward(20)
        exercise3.right(50)
        exercise3.forward(20)
        exercise3.left(50)
        exercise3.forward(20)
        exercise3.right(50)
        exercise3.forward(20)
        exercise3.left(50)

        exercise3.penup()
        exercise3.setposition(0, 0)
        exercise3.pendown()

        # between one line and the other
        exercise3.right(10)



root1=tk.Tk()
root1.title("Final Project")

center_window(500, 300)
frame = tk.Frame(root1)
frame.pack()

label = tk.Label(frame, text="Art + Maths + Programming")
label.pack()

canvas = Canvas(width=620, height=620, bg="orange")
canvas.pack(expand=YES, fill=BOTH)

button0 = tk.Button(frame, text="Click to see an artsy CIRCLE",command=lambda: startingwindow(button0), fg="green")
button0.pack(side=tk.LEFT)

button1 = tk.Button(frame, text="Not ready for this YET", fg="red", command=quit)
button1.pack(side = tk.LEFT)

root1.mainloop()
turtle.exitonclick()