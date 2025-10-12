import tkinter as tk
import time

#first, let's build the UI for our calculator


#we create a window, give it a name and size, and customize it a little

fen=tk.Tk()
fen.title("Calculator")
fen.geometry("400x600")
fen.configure(bg="#212420",padx=5,pady=5)

#padx and pady create an empty space near the edge of the window


#we add rows and columns to it, for our buttons
#each row has the same weight so that they can fill up the entirety of the window
#each row has the same uniform value so that they have the same height, no matter the text inside
#(here it's "1", but it could be anything, not neccesarily a number as long as it's the same)

for i in range (6):
    fen.grid_rowconfigure(i, weight=1,uniform=1)
for i in range(4):
    fen.grid_columnconfigure(i, weight=2,uniform=1)


#we create dictionnaries that we'll use for our button (so we don't have to write the same thing 100x in a row)
#sticky forces the button to use all the available space, not just the center of a cell

button_dict = {"font":"10"}
grid_dict = {"sticky": "nswe", "padx":5, "pady":5}


#we then define the buttons we need for our calculator

var=tk.StringVar()      #we'll need a variable for the screen of our calculator. However, tkinter only allows their own special variable tk.StringVar
var.set(0)              #intially we want the screen to display "0", so we set its value to "0"

#we need a screen to display the results of our calculator. we define it as a label (a text area)
#the anchor value is either n,s,w,e (cardinal directions), and forces the text to a side of the box

screen=tk.Label(fen,textvariable=var,bg="#bdff91",anchor="e",font=5)
screen.grid(row=0,columnspan=4,**grid_dict)         #we call grid_dict for format

#for each button, we assign a row, a column, but most importantly a function that we'll need for our calculations

#1st row

#2nd row :
button7=tk.Button(fen,text="7",**button_dict,command=lambda :C(7))
button7.grid(column=0, row=2,**grid_dict)  

button8=tk.Button(fen,text="8",**button_dict,command=lambda :C(8))
button8.grid(column=1, row=2,**grid_dict)

button9=tk.Button(fen,text="9",**button_dict,command=lambda :C(9))
button9.grid(column=2, row=2,**grid_dict)

add=tk.Button(fen,text="+",**button_dict,command=lambda :OPP(0,num1,num2))
add.grid(column=3, row=2,**grid_dict)

#3rd row :
button4=tk.Button(fen,text="4",**button_dict,command=lambda :C(4))
button4.grid(column=0, row=3,**grid_dict)

button5=tk.Button(fen,text="5",**button_dict,command=lambda :C(5))
button5.grid(column=1, row=3,**grid_dict)

button6=tk.Button(fen,text="6",**button_dict,command=lambda :C(6))
button6.grid(column=2, row=3,**grid_dict)

sub=tk.Button(fen,text="-",**button_dict,command=lambda :OPP(1,num1,num2))
sub.grid(column=3, row=3,**grid_dict)

#4rd row :

button1=tk.Button(fen,text="1",**button_dict,command=lambda :C(1))
button1.grid(column=0, row=4,**grid_dict)

button2=tk.Button(fen,text="2",**button_dict,command=lambda :C(2))
button2.grid(column=1, row=4,**grid_dict)

button3=tk.Button(fen,text="3",**button_dict,command=lambda :C(3))
button3.grid(column=2, row=4,**grid_dict)

mul=tk.Button(fen,text="*",**button_dict,command=lambda :OPP(2,num1,num2))
mul.grid(column=3, row=4,**grid_dict)

#5th row :
clear=tk.Button(fen,text="C",**button_dict,command=lambda :clear())
clear.grid(column=0, row=5,**grid_dict)

button0=tk.Button(fen,text="0",**button_dict,command=lambda :C(0))
button0.grid(column=1, row=5,**grid_dict)

equal=tk.Button(fen,text="=",**button_dict,command=lambda :equal(num1,num2))
equal.grid(column=2, row=5,**grid_dict)

div=tk.Button(fen,text="÷",**button_dict,command=lambda :OPP(3,num1,num2))
div.grid(column=3, row=5,**grid_dict)




#from there, we are going to build the actual calculator


#We'll need some variables for our calculations

num1=0                          #We store the numbers pressed on the calculator in these variables
num2=0
order=1                         #To track
operation="Nothing"             #To track which calculations we're doing

def C(n):
    global num1
    global num2
    global order
    if order==0:
        num1=num2=0
        var.set(num1)
        order=1
    if order==1:
        num1 = num1+n
        if num1=="":
            num1=0
        var.set(num1)
    else:
        num2 = num2+n
        if num2=="":
            num2=0
        var.set(num2)

def add(x,y):
    return float(x)+float(y)
def mul(x,y):
    return float(x)*float(y)

def OPP(i,x,y):
    global num1
    global num2
    global operation
    global order
    print(num1,num2)
    try:
        if order==2:
            if i==0:
                return add(x,y)
            if i==1:
                return add(x,-y)
            if i==2:
                return mul(x,y)
            if i==3:
                return mul(x,1/y)
        else:
            order=2
            if i==0:
                operation="add"
            if i==1:
                operation="sub"
            if i==2:
                operation="mul"
            if i==3:
                operation="div"

    except (ZeroDivisionError,ValueError):
        return


def equal(x,y):
    global num1
    global num2
    global order
    print(x,y)
    if operation=="add":
        var.set(str(OPP(0,x,y)).removesuffix(".0"))
    if operation=="sub":
        var.set(str(OPP(0,x,-y)).removesuffix(".0"))
    if operation=="mul":
        var.set(str(OPP(2,x,y)).removesuffix(".0"))
    if operation=="div":
        try:
            var.set(str(OPP(2,x,1/y)).removesuffix(".0"))
        except ZeroDivisionError:
            var.set("ZeroDivisionError")
    if var.get()=="ZeroDivisionError":
        print("yes")
        num1=0
    else:
        num1=(var.get())
    num2=0
    order=0
    print(num1,num2)

def clear():
    global num1
    global num2
    global operation
    global order
    num1=0
    num2=0
    order=1
    operation="Nothing"
    var.set(0)
    print(num1,num2)


fen.mainloop()