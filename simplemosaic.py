#Moroccan Mosaic using Python Turtle - www.101computing.net/morroccan-mosaic/
import tkinter as tk
import turtle
from tkinter import *
from tkinter import messagebox
import random


def center_window(w=300, h=200):
    # get screen width and height
    ws = root2.winfo_screenwidth()
    hs = root2.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root2.geometry('%dx%d+%d+%d' % (w, h, x, y))


def information():
    tk.messagebox.showinfo("Clara Dubois", "SIMPLE MOSAIC")
    return locals()


def startingwindow(x):
    button1.pack_forget()

    button2 = tk.Button(frame, text="Information", bg="yellow", fg="red", command=information)
    button2.pack(side=tk.LEFT)

    button3 = tk.Button(frame, text="Mosaic", fg="green", command=secondmosaic)
    button3.pack(side=tk.LEFT)

    button4 = tk.Button(frame, text="Close", fg="red", command=quit)
    button4.pack(side=tk.LEFT)

    return locals(), x.pack_forget()

def secondmosaic():

    exercise4 = turtle.Turtle()
    exercise4.shape("arrow")
    turtle.title("SIMPLE MOSAIC")
    turtle.color('black')
    turtle.pensize(1)
    turtle.tracer(1, 1)
    turtle.speed(11)

    def random_color1():
        color1 = "#" + "%06x" % random.randint(0, 0xFFFFFF)
        return color1


    def simpleMosaic(color,numberOfSides,size,numberOfIterations):
        turtle.color(color)
        for i in range(0,numberOfIterations):
            for j in range (0,numberOfSides):
                turtle.forward(size)
                turtle.left(360 / numberOfSides)
            turtle.left(360 / numberOfIterations)


    simpleMosaic(random_color1(),6,100,20)

    turtle.done()

    return locals()

#drawMosaic("#CB0B3F",5,100,10)
#drawMosaic("#0BCB9D",6,100,6)
#drawMosaic("#FF5733",6,100,15)

    # exercise4.hideturtle()

root2 = tk.Tk()
root2.title("Final Project")

center_window(500, 300)
frame = tk.Frame(root2)
frame.pack()

label = tk.Label(frame, text="Art + Maths + Programming")
label.pack()

canvas = Canvas(width=620, height=620, bg="yellow")
canvas.pack(expand=YES, fill=BOTH)

button0 = tk.Button(frame, text="Click to see a SIMPLE MOSAIC",command=lambda: startingwindow(button0), fg="green")
button0.pack(side=tk.LEFT)

button1 = tk.Button(frame, text="Not ready for this YET", fg="red", command=quit)
button1.pack(side = tk.LEFT)

root2.mainloop()