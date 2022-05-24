from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log

window = Tk()
screenSize = "279x442"
window.geometry(screenSize)
window.resizable(0, 0)
window.title("Calcualtor")

def about():
    messagebox.showinfo('About',"\n \n \n   Made by Harshit kumar \n \n INSTAGRAM : @harshit_kumarofficial \n \n Github : harshitkumar9030 \n \n Twitter : @OhHarshit \n \n")

def clickButton(item):
    global expression
    inputText.set(inputText.get()+(str(item)))

def clearButton():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clearAll():
    inputText.set("")

def expand():
    if screenSize=="279x500":
        window.geometry("279x555")
    else:
        window.geometry("279x555")
def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)
