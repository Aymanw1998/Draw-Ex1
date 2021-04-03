# Exercise - 1
# Students:
#           Name of first student: Ayman AL-Wahbani     ID: 209138155
#           Name of second student: Refael Gawi         ID: 301050365
from tkinter import *
from tkinter import colorchooser

# Classes

'''Shape class - The desired drawing to create on the board'''


class Shape:
    def __init__(self):
        self.name = ""

    def get(self):
        return self.name

    def set(self, name):
        self.name = name


'''Number_Points - How many dots are on the board (in each new piece)'''


class Number_Points:
    def __init__(self):
        self.counter = 0

    def get(self):
        return self.counter

    def set(self, counter):
        self.counter = counter


# Create a variable of the type of classes we have created
number_point = Number_Points()
shape = Shape()

# x and y are arrays for the points
x = [0, 0, 0, 0]
y = [0, 0, 0, 0]

# draw is a variable that saves the color and size font that the user will draw
draw = ["Black", 1]

# Create GUI

# Create a window
root = Tk()
root.title("Exercise - 1")
# width and height will preserve the length and width of your computer screen
width: int = root.winfo_screenwidth()
height: int = root.winfo_screenheight()

# Gives the window the length and width of the screen
root.geometry("%dx%d+0+0" % (width, height))

# Create frame for the top side
frameTop = Frame(root, width=width, height=height / 1.5)
frameTop.pack(side=TOP)

# Create subtitle for canvas and options
mylabelOptions = Label(frameTop, text="Options:")
mylabelOptions.place(x=0, y=0)

mylebalCanvas = Label(frameTop, text="Board:")
mylebalCanvas.place(x=200, y=0)

# Create frame for left-top side (Options)
frameLeft = Frame(frameTop, width=200, height=height / 1.5, bg="Red")
frameLeft.place(x=0, y=20)

# Create canvas for Right-top side (Board for the users)
canvas = Canvas(frameTop, width=width, height=height, bg="White")
canvas.place(x=200, y=20)
img = PhotoImage(width=width,height=height)
canvas.create_image((width/2, height/2), image=img, state="normal")

'''Color'''
# Create label and button for select the color
color_Label = Label(frameLeft, text="Color (Click for Change):", bg="Red", fg="Black", font=("Helavetica", 11))
color_Label.place(x=0, y=30)

color_button_select = Button(frameLeft, width=5, height=2, bg="Black")
color_button_select.place(x=100, y=60)


# function color_Draw- to change the color
def color_Draw():
    mycolor = colorchooser.askcolor()[1]
    if mycolor is not None:
        color_button_select.configure(bg=mycolor)
        draw[0] = mycolor


def size_Draw():
    pass


# Determining what the color button does
color_button_select.configure(command=lambda: color_Draw())
'''Size font'''
# Create label and Entry for size font
size_font_Label = Label(frameLeft, text="Size font:", bg="Red", fg="Black",
                        font=("Helavetica", 11))
size_font_Label.place(x=0, y=130)

size_font_Entry = Entry(frameLeft, bd=4, width=10)
size_font_Entry.insert(END, '1')
size_font_Entry.place(x=80, y=130)

'''Number sections curve'''
# Create label and Entry for select the curve
number_sections_curve_Label = Label(frameLeft, text="Number of sections for curve:", bg="Red", fg="Black",
                                    font=("Helavetica", 11))
number_sections_curve_Label.place(x=0, y=210)

number_sections_curve_Entry = Entry(frameLeft, bd=4, width=10)
number_sections_curve_Entry.insert(END, '10')
number_sections_curve_Entry.configure(state='disabled', bg="Black")
number_sections_curve_Entry.place(x=80, y=250)

# Create frame for bottom side (for the 4 buttons: Line, Circle, Curve, Create)
frameBottom = Frame(root, width=width)
frameBottom.place(x=width / 6, y=height / 1.5)

# Create the buttons
myButton_Line = Button(frameBottom, text="Line", width=20, height=3, bg="White", font=("Helavetica", 15))
myButton_Circle = Button(frameBottom, text="Circle", width=20, height=3, bg="White", font=("Helavetica", 15))
myButton_Curve = Button(frameBottom, text="Curve", width=20, height=3, bg="White", font=("Helavetica", 15))
myButton_Clear = Button(frameBottom, text="Clear", width=20, height=3, bg="White", font=("Helavetica", 15))
myButton_Restart = Button(frameBottom, text="Restart", width=20, height=3, bg="White", font=("Helavetica", 15))
# Arrange the places of the buttons
myButton_Restart.pack(side=RIGHT)
myButton_Clear.pack(side=RIGHT)
myButton_Curve.pack(side=RIGHT)
myButton_Circle.pack(side=RIGHT)
myButton_Line.pack(side=RIGHT)


# function changeButton - Replacing the desired button (shape to draw)
def changeButton(input: str):
    if input != "Clear":
        shape.set(input)
    if input == "Line":
        # Disabled and non-disabled of Entry
        number_sections_curve_Entry.configure(state='disabled', bg="Black")
        myButton_Line.configure(bg="Pink")
        myButton_Circle.configure(bg="White")
        myButton_Curve.configure(bg="White")
    elif input == "Circle":
        # Disabled and non-disabled of Entry
        number_sections_curve_Entry.configure(state='disabled', bg="Black")
        myButton_Line.configure(bg="White")
        myButton_Circle.configure(bg="Pink")
        myButton_Curve.configure(bg="White")
    elif input == "Curve":
        # Disabled and non-disabled of Entry
        number_sections_curve_Entry.configure(state="normal", bg="White")
        myButton_Line.configure(bg="White")
        myButton_Circle.configure(bg="White")
        myButton_Curve.configure(bg="Pink")
    else:

        # Clean the canvas (board)
        global canvas,img
        canvas.delete(img)
        img = PhotoImage(width=width, height=height)
        canvas.create_image((width / 2, height / 2), image=img, state="normal")
        if input == "":
            draw[1] = "Black"
            color_button_select.configure(bg=draw[1])

            # Clean the Entry (textBox)
            number_sections_curve_Entry.delete(0, END)
            # Write on Entry (textBox) the value
            number_sections_curve_Entry.insert(END, '10')
            # Change the Entry (textBox) to disable
            number_sections_curve_Entry.configure(state='disabled', bg="Black")

            size_font_Entry.delete(0, END)
            size_font_Entry.insert(END, '1')

            myButton_Line.configure(bg="White")
            myButton_Circle.configure(bg="White")
            myButton_Curve.configure(bg="White")


# Determining what each of the buttons does
myButton_Line.configure(command=lambda: changeButton("Line"))
myButton_Curve.configure(command=lambda: changeButton("Curve"))
myButton_Circle.configure(command=lambda: changeButton("Circle"))
myButton_Clear.configure(command=lambda: changeButton("Clear"))
myButton_Restart.configure(command=lambda: changeButton(""))

'''Pixel'''


# function myPixel
def myPixel(_x, _y):
    global canvas, img
    if _x < 0 or _y < 0:
        return
    # create_oval(x0, y0, x1, y1, option, ...), with x0 = x1 and y0 = y1 so it is create/ draw pixel
    img.put(draw[0],(int(_x),int(_y)))


'''Line'''


# DDA algorithm
# myLine: is a function responsible for drawing on the canvas line when the user marks two points
def myLine(x1, y1, x2, y2):
    # We will mark coordinates (x1,y1) a start drawing
    _x = x1
    _y = y1

    # Calculate distance difference between two identical coordinates
    x_dif = abs(x2 - x1)
    y_dif = abs(y2 - y1)

    # Maintaining the maximum difference betwween the two differences we calculated in the previous step
    # and keeping the value in a variable named "rang"
    rang = max(x_dif, y_dif)

    if rang == 0:
        return
    # Defining the size of the pivotal steps (slope)
    dx = x_dif / float(rang)
    dy = y_dif / float(rang)

    # Go through a loop (duration of the required steps [maximum])
    # i = 0......rang
    for i in range(rang):
        # A function does not know which one is large or small in coordinates

        # if we started with the small x (in order of the pixels) so we will move forward (+),
        # else we will progress upside down (-)
        if x1 < x2:
            _x += dx
        else:
            _x -= dx

        if y1 < y2:
            _y += dy
        else:
            _y -= dy

        myPixel(_x, _y)


'''Circle'''


# Bresenheim algorithm
# for draw Circle:
# we have 3 function:
#     1. getRadius: for calculate the radius of the circle (by the equation of the circle)
#     2. plot_circle_points: Auxiliary function that divides the circle into 8 pieces and marks points
#         in the 8 parts
#         [see : https://online.shenkar.ac.il/pluginfile.php/570255/mod_resource/content/6/cg20-03-1.pdf, page 32]
#     3. myCircle: the main function that runs the algorithm of Bresenheim
def getRadius(x1, y1, x2, y2):
    r2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    r = r2 ** 0.5
    return r


def plot_circle_points(xc, yc, _x, _y):
    # Price of spot points that are similar (as if) in each part of 8 parts in a circle
    # see:
    # https://online.shenkar.ac.il/pluginfile.php/570255/mod_resource/content/6/cg20-03-1.pdf, page 32
    myPixel(xc + _x, yc + _y)
    myPixel(xc - _x, yc + _y)
    myPixel(xc + _x, yc - _y)
    myPixel(xc - _x, yc - _y)
    myPixel(xc + _y, yc + _x)
    myPixel(xc - _y, yc + _x)
    myPixel(xc + _y, yc - _x)
    myPixel(xc - _y, yc - _x)


def myCircle(xc, yc, r):
    _x = 0
    _y = r

    p = 3 - (2 * r)
    while _x < _y:
        plot_circle_points(xc, yc, _x, _y)
        if p < 0:
            p = p + 4 * _x + 6
        else:
            p = p + 4 * (_x - _y) + 10
            _y -= 1
        _x += 1
    if _x == _y:
        plot_circle_points(xc, yc, _x, _y)


'''Curve'''


def draw_curve_pixle_blod(_x, _y):
    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) == 2 and abs(j) == 2:
                continue
            myPixel(_x + i, _y + j)


def myCurve(x1, y1, x2, y2, x3, y3, x4, y4, n):
    t = 0
    last_x = x1
    last_y = y1

    ax = -x1 + 3 * x2 - 3 * x3 + x4
    ay = -y1 + 3 * y2 - 3 * y3 + y4

    bx = 3 * x1 - 6 * x2 + 3 * x3
    by = 3 * y1 - 6 * y2 + 3 * y3

    cx = -3 * x1 + 3 * x2
    cy = -3 * y1 + 3 * y2

    dx = x1
    dy = y1

    draw_curve_pixle_blod(x1, y1)
    draw_curve_pixle_blod(x2, y2)
    draw_curve_pixle_blod(x3, y3)
    draw_curve_pixle_blod(x4, y4)

    while t <= 1:
        xt = int(ax * (t ** 3) + bx * (t ** 2) + cx * t + dx)
        yt = int(ay * (t ** 3) + by * (t ** 2) + cy * t + dy)
        myLine(last_x, last_y, xt, yt)
        last_x = xt
        last_y = yt
        t += 1 / n
    myLine(last_x, last_y, x4, y4)


# Function myClick: Main function, for control
def myClick(event):
    number = 10
    try:
        number = int(number_sections_curve_Entry.get())
    except ValueError:
        number = 10
        number_sections_curve_Entry.delete(0, END)
        number_sections_curve_Entry.insert(END, '10')
    try:
        draw[1] = int(size_font_Entry.get())
    except ValueError:
        draw[1] = 1
        size_font_Entry.delete(0, END)
        size_font_Entry.insert(END, '1')
    myPixel(event.x, event.y)
    # save first point
    if number_point.get() == 0:
        x[0] = event.x
        y[0] = event.y
        # change the number_point, for now we have 1 point
        number_point.set(1)
    # save second point
    elif number_point.get() == 1:
        x[1] = event.x
        y[1] = event.y
        # change the number_point, for now we have 2 points
        number_point.set(2)
    # save third point
    elif number_point.get() == 2:
        x[2] = event.x
        y[2] = event.y
        # change the number_point, for now we have 3 points
        number_point.set(3)
    # save fourth point
    elif number_point.get() == 3:
        x[3] = event.x
        y[3] = event.y
        # change the number_point, for now we have 4 points
        number_point.set(4)
    # if the shape is Line and we have 2 points so go to the myLine function to draw Line
    if shape.get() == "Line" and number_point.get() == 2:
        myLine(x[0], y[0], x[1], y[1])
        # change number_point to 0 point, mean now user will draw new shape
        number_point.set(0)
    # if the shape is Circle and we have 2 points so go to the myCircle function to draw Circle
    elif shape.get() == "Circle" and number_point.get() == 2:
        myCircle(x[0], y[0], getRadius(x[0], y[0], x[1], y[1]))
        # change number_point to 0 point, mean now user will draw new shape
        number_point.set(0)
    # if the shape is Curve and we have 4 points so go to the myCurve function to draw Circle
    elif shape.get() == "Curve" and number_point.get() == 4:
        myCurve(x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3], number)
        # Change number_point to 0 point, mean now user will draw new shape
        number_point.set(0)
    elif shape.get() == "":
        # Change number_point to 0 point, mean now user will draw new shape
        number_point.set(0)


# The canvas (drawing board) will be controlled by the mouse button
canvas.bind("<Button-1>", myClick)

# Show the window
root.mainloop()
