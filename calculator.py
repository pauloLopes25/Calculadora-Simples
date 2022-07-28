from cgitb import text
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('290x425')
root.configure(background="light grey")
root.title("Calculator")

calculatorVisor = Entry(root, width=40, borderwidth=5)
calculatorVisor.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

def buttonClick(number):
    current = calculatorVisor.get()
    calculatorVisor.delete(0, END)
    calculatorVisor.insert(0, str(current) + str(number))

def buttonClear():
    calculatorVisor.delete(0,'end')

def buttonAdd():
    number1 = calculatorVisor.get()
    global f_num
    global math
    math = "adittion"
    f_num = int(number1)
    calculatorVisor.delete(0, END)

def buttonTimes():
    number1 = calculatorVisor.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(number1)
    calculatorVisor.delete(0, END)

def buttonSubtraction():
    number1 = calculatorVisor.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(number1)
    calculatorVisor.delete(0, END)

def buttonDivide():
    number1 = calculatorVisor.get()
    global f_num
    global math
    math = "Divide"
    f_num = int(number1)
    calculatorVisor.delete(0, END)

def buttonEquals():
    number2 = calculatorVisor.get()
    calculatorVisor.delete(0, END)
    if(math == "adittion"):
        calculatorVisor.insert(0, f_num + int(number2))
    if(math == "multiply"):
        calculatorVisor.insert(0, f_num * int(number2))
    if(math == "subtraction"):
        calculatorVisor.insert(0, f_num - int(number2))
    if(math == "Divide"):
        if(int(number2) == 0):
            messagebox.showerror("Error", "Do not divide numbers by zero!")
        calculatorVisor.insert(0,f_num / int(number2))


button7 = Button(root, text="7", padx=40, pady=20, command=lambda:buttonClick(7)).grid(column=0, row=1)
button8 = Button(root, text="8", padx=40, pady=20, command=lambda:buttonClick(8)).grid(column=1, row=1)
button9 = Button(root, text="9", padx=49, pady=20, command=lambda:buttonClick(9)).grid(column=2, row=1)

button6 = Button(root, text="6", padx=40, pady=20, command=lambda:buttonClick(6)).grid(column=0, row=2)
button5 = Button(root, text="5", padx=40, pady=20, command=lambda:buttonClick(5)).grid(column=1, row=2)
button4 = Button(root, text="4", padx=49, pady=20, command=lambda:buttonClick(4)).grid(column=2, row=2)

button3 = Button(root, text="3", padx=40, pady=20, command=lambda:buttonClick(3)).grid(column=0, row=3)
button2 = Button(root, text="2", padx=40, pady=20, command=lambda:buttonClick(2)).grid(column=1, row=3)
button1 = Button(root, text="1", padx=49, pady=20, command=lambda:buttonClick(1)).grid(column=2, row=3)

button0 = Button(root, text="0", padx=40, pady=20, command=lambda:buttonClick(0)).grid(column=0, row=4)
buttonSub = Button(root, text="-", pady=20, padx=40, command=buttonSubtraction).grid(column=1, row=4)
buttonclear = Button(root, text="clear", pady=20, padx=40, command=buttonClear).grid(column=2, row =4)

buttonplus = Button(root, text="+", padx=40, pady=20, command=buttonAdd).grid(column=0,row=5)
buttonTime = Button(root, text="*", padx=40, pady=20, command=buttonTimes).grid(column=1, row=5)
buttonDiv = Button(root, text = "/", padx=48, pady=20, command=buttonDivide).grid(column=2, row=5)

buttonEqual = Button(root, text="=", padx=142, pady=20, command=buttonEquals).grid(column=0, row=6, columnspan=3)

root.mainloop()