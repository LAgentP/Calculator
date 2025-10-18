import tkinter as tk
import time

#First, let's build the UI for our calculator


#We create a window, give it a name and size, and customize it a little

fen=tk.Tk()
fen.title("Calculator")
fen.geometry("400x600")
fen.configure(bg="#212420",padx=5,pady=5)

#padx and pady create an empty space near the edge of the window


#We add rows and columns to it, for our buttons
#Each row has the same weight so that they can fill up the entirety of the window
#Each row has the same uniform value so that they have the same height, no matter the text inside
#(here it's "1", but it could be anything, not neccesarily a number as long as it's the same)

for i in range (6):
    fen.grid_rowconfigure(i, weight=1,uniform=1)
for i in range(4):
    fen.grid_columnconfigure(i, weight=2,uniform=1)


#We create dictionnaries that we'll use for our button (so we don't have to write the same thing 100x in a row)
#sticky forces the button to use all the available space, not just the center of a cell

button_dict = {"font":"10"}
grid_dict = {"sticky": "nswe", "padx":5, "pady":5}


#We then define the buttons we need for our calculator

var=tk.StringVar()      #We'll need a variable for the screen of our calculator. However, tkinter only allows their own special variable tk.StringVar
var.set(0)              #Intially we want the screen to display "0", so we set its value to "0"

#We need a screen to display the results of our calculator. we define it as a label (a text area)
#The anchor value is either n,s,w,e (cardinal directions), and forces the text to a side of the box

screen=tk.Label(fen,textvariable=var,bg="#bdff91",anchor="e",font=5)
screen.grid(row=0,columnspan=4,**grid_dict)                                 #we call grid_dict to format it

#For each button, we assign a row, a column, but most importantly a function that we'll need for our calculations

#1st row :

#2nd row :
button7=tk.Button(fen,text="7",**button_dict,command=lambda :C(7))
button7.grid(column=0, row=2,**grid_dict)  

button8=tk.Button(fen,text="8",**button_dict,command=lambda :C(8))
button8.grid(column=1, row=2,**grid_dict)

button9=tk.Button(fen,text="9",**button_dict,command=lambda :C(9))
button9.grid(column=2, row=2,**grid_dict)

add=tk.Button(fen,text="+",**button_dict,command=lambda :OPP(0))
add.grid(column=3, row=2,**grid_dict)

#3rd row :
button4=tk.Button(fen,text="4",**button_dict,command=lambda :C(4))
button4.grid(column=0, row=3,**grid_dict)

button5=tk.Button(fen,text="5",**button_dict,command=lambda :C(5))
button5.grid(column=1, row=3,**grid_dict)

button6=tk.Button(fen,text="6",**button_dict,command=lambda :C(6))
button6.grid(column=2, row=3,**grid_dict)

sub=tk.Button(fen,text="-",**button_dict,command=lambda :OPP(1))
sub.grid(column=3, row=3,**grid_dict)

#4rd row :

button1=tk.Button(fen,text="1",**button_dict,command=lambda :C(1))
button1.grid(column=0, row=4,**grid_dict)

button2=tk.Button(fen,text="2",**button_dict,command=lambda :C(2))
button2.grid(column=1, row=4,**grid_dict)

button3=tk.Button(fen,text="3",**button_dict,command=lambda :C(3))
button3.grid(column=2, row=4,**grid_dict)

mul=tk.Button(fen,text="*",**button_dict,command=lambda :OPP(2))
mul.grid(column=3, row=4,**grid_dict)

#5th row :
clear=tk.Button(fen,text="C",**button_dict,command=lambda :clear())
clear.grid(column=0, row=5,**grid_dict)

button0=tk.Button(fen,text="0",**button_dict,command=lambda :C(0))
button0.grid(column=1, row=5,**grid_dict)

equal=tk.Button(fen,text="=",**button_dict,command=lambda :equal(num1,num2))
equal.grid(column=2, row=5,**grid_dict)

div=tk.Button(fen,text="÷",**button_dict,command=lambda :OPP(3))
div.grid(column=3, row=5,**grid_dict)




#From there, we are going to build the actual calculator


#We'll need some variables for our calculations

num1="0"                        #We store the numbers pressed on the calculator in these variables
num2="0"                        #It's more convenient to work with string, but using float instead *shouldn't* break anything
order=1                         #-> To track if the numbers should go into num1 (when order==1) or num2 (when order ==2)
operation="Nothing"             #-> To track which calculations we're doing
end=False                       #-> To track wether we just finished a calculation or not


#As well as our basic operations
def add(x,y):                   #For additions and substraction
    return x+y
def mul(x,y):                   #For multiplications and divisions
    return x*y


#This function is called when we press the number "n" on the calculator
def C(n):
    global num1                 #For each function, we need to make some variables global, to edit them and save
    global num2                 #their values across multiple functions
    global end

    if order==1:                                #When order==1, the buttons we press only affects num1
        if end==True:                           #If we pressed "=" right before that, we don't want num1 to be saved
            num1="0"                              #so we put its value to 0
            end=False                           #We put end to False so that num1 doesn't get resett when we write 2-digits number

        num1 = f"{num1}{n}".removeprefix("0")   #num1 is an fstring to add the number we pressed to the end of our current value. We also remove useless 0
        var.set(num1)                           #we display num1 on screen

    else:                                       #Same thing with num2 when order==2
        num2 = f"{num2}{n}".removeprefix("0")
        var.set(num2)


#This function is called when we press an operation on the calculator (i specifies which one)
def OPP(i):
    global num1
    global num2
    global operation
    global order

    try:
        if num1 in (0,"0"):         #We don't want the buttons to have any impact as long as num1 doesn't have a value
            return                  #That way, pressing "*" then "3" only outputs "3"
        
        elif order==1:              #Order==1 if no operation has been chosen yet
            order=2                 #We inform the code that a variable has been chose
            if i==0:                #And we store it in operation, depending on what button we pressed
                operation="add"
            elif i==1:
                operation="sub"
            elif i==2:
                operation="mul"
            elif i==3:
                operation="div"

        elif order==2:              #Order==2 if an operation has been chosen. That means we want to do another operation after the first one
            equal(num1,num2)        #So we have do calculate the result of the first operation before doing anything

    except (ZeroDivisionError,ValueError):  #In case something goes wrong
        return


#This function is called when we press "=", or by OPP() (see above)
def equal(x,y):
    global num1
    global num2
    global order
    global operation
    global end

    x=float(x)           #We first need to convert our variables to float to make calculations
    y=float(y)

    #We check what operation we need to do
    if operation=="add":                            
        var.set(str(add(x,y)).removesuffix(".0"))           #.removesuffix() only works with string. It removes the ".0" of a float for a cleaner display

    elif operation=="sub":
        var.set(str(add(x,-y)).removesuffix(".0"))          #Same operation than before, but with -y

    elif operation=="mul":
        var.set(str(mul(x,y)).removesuffix(".0"))

    elif operation=="div":
        try:
            var.set(str(mul(x,1/y)).removesuffix(".0"))     #Same operation than before, but with 1/y

        except ZeroDivisionError:                           #In case we divide by 0
            var.set("ZeroDivisionError")                    #We display it on screen

    if var.get()=="ZeroDivisionError":                      #If we divided by 0, we simply reset num1 value
        num1="0"
    else:                                                   #If not, we assign its value to our result
        num1=(var.get())

    num2="0"                                                #Since we finished our operation, we don't need num2 anymore
    order=1                                                 #We reset order to 1, so the next buttons we pressed get assigned to num1
    operation="Nothing"                                     #We finished our current operation
    end=True                                                #We inform C() that we just finished our operation (see C() for more explanation)


#This function is called when we press "C" on our calculator
#It resets everything to its original value
def clear():
    global num1
    global num2
    global operation
    global order
    global end
    
    num1="0"
    num2="0"
    operation="Nothing"
    order=1
    end=False                       #Technically not needed
    var.set(0)


fen.mainloop()