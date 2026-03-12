import tkinter as rus

window = rus.Tk()
window.title("Simple Calculator")
window.geometry("350x350")
window.resizable(False,False)
window.configure(bg = "dark violet", cursor = "arrow")

# TITLE BLOCK
label1 = rus.Label(window, text = "Simple Calculator",
                   bg = "white",
                   font = ("times new roman", 14, "italic"),
                   fg = "black",
                   height = 2,
                   width = 35,
                   )
label1.grid(row = 0, column = 0, columnspan = 4)

# Label
number1 = rus.Label(window, text = "Enter First Number: ",
                    font = ("times new roman", 12, "italic"),
                    bg = "white",
                    fg = "black"
                    )
number1.grid(row = 1, column = 0, pady = 20, padx = 5)

number2 = rus.Label(window, text = "Enter Second Number: ",
                    font = ("times new roman", 12, "italic"),
                    bg = "white",
                    fg = "black"
                    )
number2.grid(row = 2, column = 0, pady = 5, padx = 5)

# Entry
entry1 = rus.Entry(window, width = 25)
entry1.grid(row = 1, column = 1, pady = 20, padx = 5)

entry2 = rus.Entry(window,  width = 25)
entry2.grid(row = 2, column = 1, padx = 5)

# Def Functions

def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    label1.config(text = f"The sum of {num1} and {num2} is {result}",
                  font = ("times new roman", 12, "italic"),
                  )

def sub():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 - num2
    label1.config(text = f"The difference of {num1} and {num2} is {result}",
                  font = ("times new roman", 12, "italic"),
                  )

def multi():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 * num2
    label1.config(text = f"The product of {num1} and {num2} is {result}",
                  font = ("times new roman", 12, "italic"),
                  )

def div():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 / num2
    label1.config(text = f"The quotient of {num1} and {num2} is {result}",
                  font = ("times new roman", 12, "italic"),
                  )

# Buttons
button1 = rus.Button(window,
                     text = "Add",
                     font = ("times new roman", 12, "italic"),
                     command = add,
                     relief = "raised",
                     activebackground = "white",
                     activeforeground = "dark gray"
                     )
button1.grid(row = 3, column = 0, pady = 30, padx = 5)

button2 = rus.Button(window,
                     text = "Subtract",
                     font = ("times new roman", 12, "italic"),
                     command = sub,
                     relief = "raised",
                     activebackground = "white",
                     activeforeground = "dark gray"
                     )
button2.grid(row = 3, column = 1, pady = 20, padx = 5)

button3 = rus.Button(window,
                     text = "Multiply",
                     font = ("times new roman", 12, "italic"),
                     command = multi,
                     relief = "raised",
                     activebackground = "white",
                     activeforeground = "dark gray"
                     )
button3.grid(row = 4, column = 0, pady = 20, padx = 5)

button4 = rus.Button(window,
                     text = "Divide",
                     font = ("times new roman", 12, "italic"),
                     command = div,
                     relief = "raised",
                     activebackground = "white",
                     activeforeground = "dark gray"
                     )
button4.grid(row = 4, column = 1, pady = 20, padx = 5)

window.mainloop()