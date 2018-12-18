import tkinter as tk
import turtle
from tkinter import *
from tkinter import messagebox
import random

def center_window(w=300, h=200):
    # get screen width and height
    ws = root3.winfo_screenwidth()
    hs = root3.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root3.geometry('%dx%d+%d+%d' % (w, h, x, y))

def information():
    tk.messagebox.showinfo("Clara Dubois", "COMPLEX MOSAIC")
    return locals()

def startingwindow(x):
    button1.pack_forget()

    button2 = tk.Button(frame, text="Information", bg="yellow", fg="red", command=information)
    button2.pack(side=tk.LEFT)

    button3 = tk.Button(frame, text="Complex Mosaic", fg="green", command=complexmosaic)
    button3.pack(side=tk.LEFT)

    button4 = tk.Button(frame, text="Close", fg="red", command=quit)
    button4.pack(side=tk.LEFT)

    return locals(), x.pack_forget()

def complexmosaic():

    exercisemosaic = turtle.Turtle()
    exercisemosaic.shape("arrow")

    exercisemosaic.speed(5000)  # Set the speed of the turtle

    # generate different colors y sides
    def random_color1():
        color1 = "#" + "%06x" % random.randint(0, 0xFFFFFF)
        return color1

    def random_color2():
        color2 = "#" + "%06x" % random.randint(0, 0xFFFFFF)
        return color2

    def random_sides1():
        for x in range(10):
          return random.randint(3,13)

    def random_sides2():
        for x in range(10):
          return random.randint(3,13)
    # create polygon
    def exercise3(color1, firstsides, size1, color2, secondsides, size2, numberOfIterations):
        for i in range(0, numberOfIterations):
            exercisemosaic.color(color1)
            for j in range(0, firstsides):
                exercisemosaic.forward(size1)
                exercisemosaic.right(360 / firstsides)
            exercisemosaic.color(color2)
            for k in range(0, secondsides):
                exercisemosaic.forward(size2)
                exercisemosaic.right(360 / secondsides)

            exercisemosaic.right(360 / numberOfIterations)


    exercise3(random_color1(),random_sides1(), 80, random_color2(), random_sides2(), 70, 20)
    turtle.done()

    return locals()

    # exercisemosaic.hideturtle()


root3 = tk.Tk()
root3.title("Final Project")

center_window(500, 300)
frame = tk.Frame(root3)
frame.pack()

label = tk.Label(frame, text="Art + Maths + Programming")
label.pack()

canvas = Canvas(width=620, height=620, bg="green")
canvas.pack(expand=YES, fill=BOTH)

button0 = tk.Button(frame, text="Click to see a COMPLEX MOSAIC",command=lambda: startingwindow(button0),bg="yellow", fg="green")
button0.pack(side=tk.LEFT)

button1 = tk.Button(frame, text="Not ready for this YET", fg="red", command=quit)
button1.pack(side = tk.LEFT)

root3.mainloop()