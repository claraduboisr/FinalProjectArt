import PIL
import tkinter as tk
import turtle
from tkinter import *
from tkinter import messagebox
import time
from matplotlib import colors as mcolors
from PIL import Image, ImageTk
import random

def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# This are the buttons that appear in the window after you agree to continue with the program
def startingwindow(x):
    button1.pack_forget()

    button2 = tk.Button(frame, text="Information", bg="yellow", fg="red", command=information)
    button2.pack(side=tk.LEFT)

    button3 = tk.Button(frame, text="Fibonacci", fg="green", command=continuefibo)
    button3.pack(side=tk.LEFT)

    button4 = tk.Button(frame, text="Star", fg="green", command=star)
    button4.pack(side=tk.LEFT)

    button9 = tk.Button(frame, text="Close", fg="red", command=quit)
    button9.pack(side=tk.LEFT)


    return locals(), x.pack_forget()

def information():
    tk.messagebox.showinfo("Clara Dubois", "Art\n+\nMaths\n+\nProgramming  ")
    return locals()

def continuefibo():

    fiboscreen = tk.Tk()
    fiboscreen.title("Click CONTINUE to see a marvellous colorful fibonacci sequence")

    def center_window(w=300, h=200):
        # get screen width and height
        ws = fiboscreen.winfo_screenwidth()
        hs = fiboscreen.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        fiboscreen.geometry('%dx%d+%d+%d' % (w, h, x, y))
    center_window(620, 620)
    screen = 620
    canvas = Canvas(width=screen, height=screen, bg="white")
    canvas.pack(expand=YES, fill=BOTH)

    # img = ImageTk.PhotoImage(PIL.Image.open("fibo.gif"))
    # panel = tk.Label(fiboscreen, image=img)
    # panel.pack(side=BOTTOM, fill=BOTH, expand=YES)

    button3_5=tk.Button(fiboscreen, text="Continue", background="red", command=fibonacciGraph)
    button3_5.pack( expand=YES)
    fiboscreen.mainloop()

    return locals()

def fibonacciGraph():

    fib = turtle.Turtle()
    turtle.title("Welcome")
    turtle.color('black')
    turtle.pensize(1)
    turtle.tracer(1, 1)
    turtle.speed(50)

    fibo_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    for x in range(0, 100):
        # Sequence have started in 0, then 1
        first = 0
        now = 1
        nextnum = 0
        for y in range(0, 10):

            first = 0
            now = 1
            nextnum = 0

            turtle.fillcolor((random.randint(0, 255) / 255.0, random.randint(0, 255) / 255.0, random.randint(0, 255) / 255.0))
            turtle.begin_fill()

            turtle.bgcolor((random.randint(0, 255) / 255.0, random.randint(0, 255) / 255.0, random.randint(0, 255) / 255.0))

            for z in range(0, len(fibo_list)):
                turtle.circle(now, 90)
                nextnum=now + first  # The sequence is the actual number + the last one
                first = now
                now=nextnum

            turtle.goto(0, 0)
            turtle.end_fill()

            # turtle.rotate(80)
            turtle.right(80)

    button8 = tk.Button(frame, text="I'm done with this", fg="red", command=quit)
    button8.pack(side=tk.LEFT)

    turtle.done()

    return locals()

def star():
    # import exercise1
    # return exercise1
    num = 10
    length = 300
    draw_time = 2

    def random_color(num):
        color = "#" + "%06x" % random.randint(0, 0xFFFFFF)
        if num < 100:
            return color
        else:
            return "#000000"
        return num

    # esta funcion the devuelve un list con todos las rectas a dibujar
    # [ punto_inicio, punto_final] -> [(x0, y0), (x1, y1)]
    def calc_pos(num):
        points = []
        # crear una lista desde el (1, 0) hasta (num, 0)
        for i in range(1, num + 1):
            points.append((i, 0))

        # print(points)
        join = []
        # enumerate devuelve un counter (empieza en start y se le suma 1 cada iteración) y el elemento de la lista
        # entonces al hacer un enumerate de la lista alrevés
        # se obtiene: 1) i=1, element=points[-1] 2) i=2, element=points[-2] 3) i=3, element=num[-3] ...
        # a join se le hace append de una lista con 2 tuples que son las coordenadas de los puntos
        # las coordenadas son (0,i) y un elemento de points que es un tuple (num, 0)
        for i, element in enumerate(points[::-1], start=1):
            join.append([(0, i), element])

        # for i in join:
        #     print(i)
        return join

    # when submit button is clicked
    def submit():
        # read entry's box number
        try:
            num = int(e.get())
        except:
            print("not an integer")
            return
        coord = length / (num)
        # erase everything there where
        canvas.delete("all")
        # create axis
        canvas.create_line(-length + x, y, length + x, y, fill="red", width=0.5)
        canvas.create_line(x, -length + y, x, length + y, fill="red", width=0.5)
        canvas.update()
        # j is the array that gives back the function
        j = calc_pos(num)
        total = len(j) - 1
        # from the extremes to the center
        # calculate the middle of the array
        if len(j) % 2 != 0:
            mid = int((len(j) + 1) / 2)
        else:
            mid = int(len(j) / 2)

        # from 0 to the middle,
        # for the other half, it is made the last element - counter del enumerate

        for c, i in enumerate(j[:mid]):
            canvas.update()
            time.sleep(draw_time / mid)
            canvas.create_line(i[0][0] * coord + x, i[0][1] * coord + y,
                               i[1][0] * coord + x, i[1][1] * coord + y, fill=random_color(num))
            canvas.create_line(j[total - c][0][0] * coord + x, j[total - c][0][1] * coord + y,
                               j[total - c][1][0] * coord + x, j[total - c][1][1] * coord + y, fill=random_color(num))
            # canvas.update()
            # time.sleep(0.1)
            canvas.create_line(i[0][0] * coord + x, i[0][1] * coord + y,
                               -i[1][0] * coord + x, i[1][1] * coord + y, fill=random_color(num))
            canvas.create_line(j[total - c][0][0] * coord + x, j[total - c][0][1] * coord + y,
                               -j[total - c][1][0] * coord + x, j[total - c][1][1] * coord + y, fill=random_color(num))
            # canvas.update()
            # time.sleep(0.2)
            canvas.create_line(-i[0][0] * coord + x, -i[0][1] * coord + y,
                               -i[1][0] * coord + x, i[1][1] * coord + y, fill=random_color(num))
            canvas.create_line(-j[total - c][0][0] * coord + x, -j[total - c][0][1] * coord + y,
                               -j[total - c][1][0] * coord + x, j[total - c][1][1] * coord + y, fill=random_color(num))
            # canvas.update()
            # time.sleep(0.1)
            canvas.create_line(-i[0][0] * coord + x, -i[0][1] * coord + y,
                               i[1][0] * coord + x, i[1][1] * coord + y, fill=random_color(num))
            canvas.create_line(-j[total - c][0][0] * coord + x, -j[total - c][0][1] * coord + y,
                               j[total - c][1][0] * coord + x, j[total - c][1][1] * coord + y, fill=random_color(num))

    tk = Tk()

    def center_window(w=300, h=200):
        # get screen width and height
        ws = tk.winfo_screenwidth()
        hs = tk.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        tk.geometry('%dx%d+%d+%d' % (w, h, x, y))
    center_window(620, 620)
    # screen size
    screen = 620

    # give size to the window
    #tk.geometry(str(screen) + "x" + str(screen))
    bgcolor = "#eff0f7"
    tk.title("Isn't it fascinating?")

    # crea<te a frame to cover all the window
    f = Frame(tk, bg=bgcolor, width=screen, height=screen)
    f.pack(fill=BOTH, expand=1)

    # create a canvas to draw which fills the frame
    canvas = Canvas(f, bg=bgcolor)
    canvas.pack(fill=BOTH, expand=1)

    # x and y are calculated as the center of the screen
    # then I substract the coordinates obtained
    x = screen / 2
    y = screen / 2

    # initial axes
    canvas.create_line(-length + x, y, length + x, y, fill="red", width=0.5)
    canvas.create_line(x, -length + y, x, length + y, fill="red", width=0.5)

    # box where you write
    e = Entry(canvas, bg=bgcolor, highlightthickness=1, relief='flat')
    e.place(x=screen * 0.68, y=30)
    # submit button
    b = Button(canvas, text="submit", command=submit, bg='red', highlightthickness=0)
    b.place(x=screen * 0.76, y=60, anchor=NE)
    l = Label(canvas, text="Insert a number between 1 and 1000", foreground="red", bg=bgcolor)
    l.place(x=screen * 0.59, y=7.5)

    l2 = Label(canvas, text="The higher the number, the slower...", foreground="#8A4B08", bg=bgcolor)
    l2.place(x=screen * 0.01, y=7.5)

    l3 = Label(canvas, text="Try a number with two digits", foreground="green", bg=bgcolor)
    l3.place(x=screen * 0.01, y=30)
    l3.config(font=(15))

    l4 = Label(canvas, text="and another one with three digits", foreground="green", bg=bgcolor)
    l4.place(x=screen * 0.01, y=50)
    l4.config(font=(15))

    # initial image
    coord = length / (num)
    for i in calc_pos(num):
        canvas.create_line(i[0][0] * coord + x, i[0][1] * coord + y, i[1][0] * coord + x, i[1][1] * coord + y)
        canvas.create_line(i[0][0] * coord + x, i[0][1] * coord + y, -i[1][0] * coord + x, i[1][1] * coord + y)

        canvas.create_line(-i[0][0] * coord + x, -i[0][1] * coord + y, i[1][0] * coord + x, i[1][1] * coord + y)
        canvas.create_line(-i[0][0] * coord + x, -i[0][1] * coord + y, -i[1][0] * coord + x, i[1][1] * coord + y)

    tk.mainloop()


root = tk.Tk()
root.title("Final Project")

center_window(500, 300)
frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Art + Maths + Programming")
label.pack()

canvas = Canvas(width=620, height=620, bg="red")
canvas.pack(expand=YES, fill=BOTH)

button0 = tk.Button(frame, text="Click To START",command=lambda: startingwindow(button0),bg="yellow", fg="green")
button0.pack(side=tk.LEFT)

button1 = tk.Button(frame, text="Not ready for this YET", fg="red", command=quit)
button1.pack(side = tk.LEFT)

root.mainloop()