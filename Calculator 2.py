import tkinter as tk

fen=tk.Tk()
fen.title("Calculatrice")
fen.geometry("400x500")
fen.configure(bg="#212420",padx=5,pady=5)

var=tk.StringVar()
var.set(0)

h=3
w=9

num1=0
num2=0


order=0
operation="Nothing"

def add(x,y):
    global order
    global operation
    order=1
    operation="add"
    print(operation)

def equal(x,y):
    print(operation)
    if operation=="add":
        print(x)
        print(y)
        print(x+y)
        var.set(x+y)
    
def C(n):
    if order==0:
        global num1
        num1 = n
        var.set(num1)
    elif order ==1:
        global num2
        print("Order = 1")
        num2 = n
        var.set(num2)



fen.grid_rowconfigure(0, weight=1)
fen.grid_rowconfigure(1, weight=1)
fen.grid_rowconfigure(2, weight=1)
fen.grid_rowconfigure(3, weight=1)
fen.grid_rowconfigure(4, weight=1)
fen.grid_columnconfigure(0, weight=2)
fen.grid_columnconfigure(1, weight=2)
fen.grid_columnconfigure(2, weight=2)
fen.grid_columnconfigure(3, weight=2)


Ecran=tk.Label(fen,textvariable=var,bg="#bdff91",anchor="e",font=5)
Ecran.grid(row=0,columnspan=4,sticky="nswe",padx=5,pady=5)


h=3
w=9
button0=tk.Button(fen,text="0",command=lambda :C(0))
button0.grid(column=1, row=4,sticky="nswe",padx=5,pady=5)
button1=tk.Button(fen,text="1",command=lambda :C(1))
button1.grid(column=0, row=3,sticky="nswe",padx=5,pady=5)
button2=tk.Button(fen,text="2",command=lambda :C(2))
button2.grid(column=1, row=3,sticky="nswe",padx=5,pady=5)
button3=tk.Button(fen,text="3",command=lambda :C(3))
button3.grid(column=2, row=3,sticky="nswe",padx=5,pady=5)
button4=tk.Button(fen,text="4",command=lambda :C(4))
button4.grid(column=0, row=2,sticky="nswe",padx=5,pady=5)
button5=tk.Button(fen,text="5",command=lambda :C(5))
button5.grid(column=1, row=2,sticky="nswe",padx=5,pady=5)
button6=tk.Button(fen,text="6",command=lambda :C(6))
button6.grid(column=2, row=2,sticky="nswe",padx=5,pady=5)
button7=tk.Button(fen,text="7",command=lambda :C(7))
button7.grid(column=0, row=1,sticky="nswe",padx=5,pady=5)
button8=tk.Button(fen,text="8",command=lambda :C(8))
button8.grid(column=1, row=1,sticky="nswe",padx=5,pady=5)
button9=tk.Button(fen,text="9",command=lambda :C(9))
button9.grid(column=2, row=1,sticky="nswe",padx=5,pady=5)
buttonp=tk.Button(fen,text="+",command=lambda :add(num1,num2))
buttonp.grid(column=3, row=1,sticky="nswe",padx=5,pady=5)
buttone=tk.Button(fen,text="=",command=lambda :equal(num1,num2))
buttone.grid(column=3, row=4,sticky="nswe",padx=5,pady=5)


fen.mainloop()