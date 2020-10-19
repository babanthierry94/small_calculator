import tkinter as tk
from tkinter import *
from tkmacosx import Button
import math


class Calculator:

    def pressDigit (self, digit):
        self.disp.configure(state='normal') # This instruction is to enable the the Text widget modification
        if self.equalFlag:
            self.disp.delete("0.0", tk.END)
            self.expression = ""
            self.equalFlag = False

        self.expression = self.expression + str(digit)
        self.disp.insert(END, str(digit), 'tag-right')
        self.disp.configure(state='disabled') # This instruction is to disanable the the Text wtdget modification
        print("Expression : ", self.expression)

    def getAndClean(self):
        # self.expression_clean = self.disp.get("0.0", tk.END)
        self.expression_clean = self.expression
        temp = self.expression_clean.replace('÷', '/')
        temp = temp.replace('x', '*')
        temp = temp.replace('^', '**')
        self.expression_clean = temp
        print("Equation Clean : ", self.expression_clean)

    def pressClear(self):
        self.disp.configure(state='normal')
        self.disp.delete("0.0", tk.END)
        self.disp.configure(state='disabled')
        print("clear button press")

    def pressDelete(self):
        self.equalFlag = False
        self.disp.configure(state='normal')
        self.disp.delete("0.0", tk.END)
        self.expression = self.expression[:-1]
        self.disp.insert("0.0", self.expression, 'tag-right')
        self.disp.configure(state='disabled')
        print("clear button press")

    def pressEqual(self):
        self.getAndClean()
        self.disp.configure(state='normal')
        if self.equalFlag:
            self.disp.delete("0.0", tk.END)
            self.disp.insert("0.0", self.expression, 'tag-right')

        self.disp.insert(END, "\n ANS : \n", 'tag-left')
        try:
            total = str(eval(str(self.expression_clean)))
            self.disp.insert(END, total, 'tag-right')
        except:
            self.disp.insert(END, "ERROR", 'tag-right')

        self.disp.configure(state='disabled')
        self.equalFlag = True
        print("Equal button press")

    def __init__(self):
        window = tk.Tk()
        window.title("Calculator 1.0")
        window.geometry()
        self.expression = ""
        self.expression_clean = ""
        self.equalFlag = False

        self.disp = Text(window, height=3, maxundo=-1, undo=True, state='disabled')
        self.disp.tag_configure('tag-right', justify='right')
        self.disp.tag_configure('tag-left', justify='left')
        self.disp.grid(row=0, column=0, columnspan=7, ipadx=20, ipady=10, sticky="nesw")

        # Create a tag for left and right text align in the Text widget
        self.disp.tag_config("alignRight", justify="right")
        self.disp.tag_config("alignLeft", justify="left")
        self.disp.insert(END, self.expression, 'tag-right')
        # self.disp.focus_set() # set the focus on the input text

        # Create Buttons and place it on the window grid
        Button(window, text="7", width=5, bg="snow", fg="black", borderless=1, command=lambda: self.pressDigit('7')).grid(row=1, column=0, sticky="nesw")
        Button(window, text="8", width=5, bg="snow", fg="black", borderless=1, command=lambda: self.pressDigit('8')).grid(row=1, column=1, sticky="nesw")
        Button(window, text="9", width=5, bg="snow", fg="black", borderless=1, command=lambda: self.pressDigit('9')).grid(row=1, column=2, sticky="nesw")
        Button(window, text="4", width=5, bg="snow", fg="black", borderless=1, command=lambda: self.pressDigit('4')).grid(row=2, column=0, sticky="nesw")
        Button(window, text="5", width=5, bg="snow", fg="black", borderless=1, command=lambda: self.pressDigit('5')).grid(row=2, column=1, sticky="nesw")
        Button(window, text="6", width=5, bg="snow", fg="black", borderless=1, command=lambda: self.pressDigit('6')).grid(row=2, column=2, sticky="nesw")
        Button(window, text="3", width=5, bg="snow", fg="black", borderless=1, command=lambda: self.pressDigit('3')).grid(row=3, column=0, sticky="nesw")
        Button(window, text="2", width=5, bg="snow", fg="black", borderless=1, command=lambda: self.pressDigit('2')).grid(row=3, column=1, sticky="nesw")
        Button(window, text="1", width=5, bg="snow", fg="black", borderless=1, command=lambda: self.pressDigit('1')).grid(row=3, column=2, sticky="nesw")
        Button(window, text="±", width=5, bg="azure3", fg="black", borderless=1, state=DISABLED).grid(row=4, column=0, sticky="nesw")
        Button(window, text="0", width=5, bg="snow", fg="black", borderless=1, command=lambda: self.pressDigit('0')).grid(row=4, column=1, sticky="nesw")
        Button(window, text=".", width=5, bg="azure3", fg="black", borderless=1, command=lambda: self.pressDigit('.')).grid(row=4, column=2, sticky="nesw")
        Button(window, text="√", width=5, bg="azure3", fg="black", borderless=1, state=DISABLED).grid(row=1, column=3, sticky="nesw")
        Button(window, text="OFF", width=5, bg="red", fg="white", borderless=1, command=lambda: window.destroy()).grid(row=1, column=4, sticky="nesw")
        Button(window, text="AC", width=5, bg="DarkOrange1", fg="white", borderless=1, command=lambda: self.pressClear()).grid(row=1, column=5, sticky="nesw")
        Button(window, text="←", width=5, bg="deep sky blue", fg="white", borderless=1, command=lambda: self.pressDelete()).grid(row=1, column=6, sticky="nesw")

        Button(window, text="x\u02B8", width=5, bg="azure3", fg="black", borderless=1, command=lambda: self.pressDigit('^')).grid(row=2, column=3, sticky="nesw")
        Button(window, text="(", width=5, bg="azure3", fg="black", borderless=1, command=lambda: self.pressDigit('(')).grid(row=2, column=4, sticky="nesw")
        Button(window, text="x", width=5, bg="azure3", fg="black", borderless=1, command=lambda: self.pressDigit('x')).grid(row=2, column=5, sticky="nesw")
        Button(window, text="÷", width=5, bg="azure3", fg="black", borderless=1, command=lambda: self.pressDigit('÷')).grid(row=2, column=6, sticky="nesw")

        Button(window, text="%", width=5, bg="azure3", fg="black", borderless=1, command=lambda: self.pressDigit('%')).grid(row=3, column=3, sticky="nesw")
        Button(window, text=")", width=5, bg="azure3", fg="black", borderless=1, command=lambda: self.pressDigit(')')).grid(row=3, column=4, sticky="nesw")
        Button(window, text="+", width=5, bg="azure3", fg="black", borderless=1, command=lambda: self.pressDigit('+')).grid(row=3, column=5, sticky="nesw")
        Button(window, text="-", width=5, bg="azure3", fg="black", borderless=1, command=lambda: self.pressDigit('-')).grid(row=3, column=6, sticky="nesw")

        Button(window, text="=", width=10, bg="lime green", fg="white", borderless=1, command=lambda: self.pressEqual()).grid(row=4, column=3, columnspan=4, sticky="nesw")

        # Enable element in the windows to be be resizable
        n_rows = 5
        n_columns = 7
        for i in range(n_rows):
            window.grid_rowconfigure(i, weight=1)
        for i in range(n_columns):
            window.grid_columnconfigure(i, weight=1)
        window.mainloop()


# launch the calculator
Calculator()
