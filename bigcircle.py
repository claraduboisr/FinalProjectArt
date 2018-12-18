import tkinter as tk
import turtle
from tkinter import *
from tkinter import messagebox
import random
import time

def center_window(w=300, h=200):
    # get screen width and height
    ws = root4.winfo_screenwidth()
    hs = root4.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root4.geometry('%dx%d+%d+%d' % (w, h, x, y))

def information():
    tk.messagebox.showinfo("Clara Dubois", "CIRCLE")
    return locals()

def startingwindow(x):
    button1.pack_forget()

    button2 = tk.Button(frame, text="Information", bg="yellow", fg="red", command=information)
    button2.pack(side=tk.LEFT)

    button3 = tk.Button(frame, text="Circle", fg="green", command=bigcircle)
    button3.pack(side=tk.LEFT)

    button4 = tk.Button(frame, text="Close", fg="red", command=quit)
    button4.pack(side=tk.LEFT)

    return locals(), x.pack_forget()

def bigcircle():

    bigcircle = turtle.Turtle()

    def random_color1():
        color1 = "#" + "%06x" % random.randint(0, 0xFFFFFF)
        return color1

    def random_color2():
        color2 = "#" + "%06x" % random.randint(0, 0xFFFFFF)
        return color2

    def random_color3():
        color3 = "#" + "%06x" % random.randint(0, 0xFFFFFF)
        return color3

    def random_color4():
        color4 = "#" + "%06x" % random.randint(0, 0xFFFFFF)
        return color4

    turtle.speed(11)
    turtle.colormode(random.randint(0,255)/255.0)
    colors = [random_color1(), random_color2(), random_color3(), random_color4()]

    index = 0

    time.sleep(2)

    for j in range(30):

        first = 40
        second = 70
        third = 3
        turtle.pencolor(colors[index])

        for i in range(14):
            turtle.circle(first)
            turtle.left(90)
            turtle.penup()
            turtle.forward(second)
            turtle.right(90)
            turtle.forward(third)
            turtle.pendown()
            first = first * 0.7
            second = second * 0.7
            third = third * 1.1
            turtle.circle(first)

        turtle.penup()
        turtle.goto(0, 0)
        turtle.forward(5)
        turtle.right(12)
        turtle.pendown()

        if index < 3:
            index = index + 1

        else:
            index = 0

    turtle.exitonclick()
    turtle.done()

    return locals()

root4 = tk.Tk()
root4.title("Final Project")

center_window(500, 300)
frame = tk.Frame(root4)
frame.pack()

label = tk.Label(frame, text="Art + Maths + Programming")
label.pack()

canvas = Canvas(width=620, height=620, bg="blue")
canvas.pack(expand=YES, fill=BOTH)

button0 = tk.Button(frame, text="Click To see an artsy CIRCLE of CIRCLES", command=lambda: startingwindow(button0), bg="yellow",fg="green")
button0.pack(side=tk.LEFT)

button1 = tk.Button(frame, text="Not ready for this YET", fg="red", command=quit)
button1.pack(side=tk.LEFT)

root4.mainloop()