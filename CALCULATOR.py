from tkinter import *

root = Tk()
root.title("CALCULATOR")


numberDisplay = Entry(root, width=35, borderwidth=5)
numberDisplay.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def buttonClick(number):
    # numberDisplay.delete(0, END)
    current = numberDisplay.get()
    numberDisplay.delete(0, END)
    numberDisplay.insert(0, str(current) + str(number))


def buttonAdd():
    firstNumber = numberDisplay.get()
    global fNum, math
    math = 'addition'
    fNum = int(firstNumber)
    numberDisplay.delete(0, END)


def buttonSubtract():
    firstNumber = numberDisplay.get()
    global fNum, math
    math = 'subtraction'
    fNum = int(firstNumber)
    numberDisplay.delete(0, END)


def buttonMultiply():
    firstNumber = numberDisplay.get()
    global fNum, math
    math = 'multiplication'
    fNum = int(firstNumber)
    numberDisplay.delete(0, END)


def buttonDivide():
    firstNumber = numberDisplay.get()
    global fNum, math
    math = 'division'
    fNum = int(firstNumber)
    numberDisplay.delete(0, END)


def buttonEqual():
    secondNUmber = numberDisplay.get()
    numberDisplay.delete(0, END)
    if math == 'addition':
        numberDisplay.insert(0, fNum + int(secondNUmber))
    if math == 'subtraction':
        numberDisplay.insert(0, fNum - int(secondNUmber))
    if math == 'multiplication':
        numberDisplay.insert(0, fNum * int(secondNUmber))
    if math == 'division':
        numberDisplay.insert(0, fNum / int(secondNUmber))


def buttonClear():
    numberDisplay.delete(0, END)


number0 = Button(root, text='0', padx=40, pady=20, fg='red', activebackground='gold',
                 command=lambda: buttonClick(0))
number1 = Button(root, text='1', padx=40, pady=20, fg='red', activebackground='gold',
                 command=lambda: buttonClick(1))
number2 = Button(root, text='2', padx=40, pady=20, fg='red', activebackground='gold',
                 command=lambda: buttonClick(2))
number3 = Button(root, text='3', padx=40, pady=20, fg='red', activebackground='gold',
                 command=lambda: buttonClick(3))
number4 = Button(root, text='4', padx=40, pady=20, fg='red', activebackground='gold',
                 command=lambda: buttonClick(4))
number5 = Button(root, text='5', padx=40, pady=20, fg='red', activebackground='gold',
                 command=lambda: buttonClick(5))
number6 = Button(root, text='6', padx=40, pady=20, fg='red', activebackground='gold',
                 command=lambda: buttonClick(6))
number7 = Button(root, text='7', padx=40, pady=20, fg='red', activebackground='gold',
                 command=lambda: buttonClick(7))
number8 = Button(root, text='8', padx=40, pady=20, fg='red', activebackground='gold',
                 command=lambda: buttonClick(8))
number9 = Button(root, text='9', padx=40, pady=20, fg='red', activebackground='gold',
                 command=lambda: buttonClick(9))
addOp = Button(root, text='+', padx=40, pady=20, fg='red', activebackground='green',
               command=buttonAdd)
subtractOp = Button(root, text='-', padx=40, pady=20, fg='red', activebackground='red',
                    command=buttonSubtract)
multiplyOp = Button(root, text='*', padx=40.4, pady=20, fg='red', activebackground='violet',
                    command=buttonMultiply)
divideOp = Button(root, text='/', padx=40, pady=20, fg='red', activebackground='white',
                  command=buttonDivide)
equalOp = Button(root, text='=', padx=39, pady=20, fg='red', activebackground='orange',
                 command=buttonEqual)
clearButton = Button(root, text='CLEAR', padx=83, pady=20, fg='red', activebackground='black',
                     command=buttonClear)

number0.grid(row=4, column=0)
number1.grid(row=3, column=2)
number2.grid(row=3, column=1)
number3.grid(row=3, column=0)
number4.grid(row=2, column=2)
number5.grid(row=2, column=1)
number6.grid(row=2, column=0)
number7.grid(row=1, column=2)
number8.grid(row=1, column=1)
number9.grid(row=1, column=0)
addOp.grid(row=4, column=1)
subtractOp.grid(row=4, column=2)
multiplyOp.grid(row=5, column=0)
divideOp.grid(row=5, column=1)
equalOp.grid(row=5, column=2)
clearButton.grid(row=6, column=0, columnspan=3)


root.mainloop()
