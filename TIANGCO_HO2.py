# my own profile app

import tkinter as rus

window = rus.Tk()
window.title("Glenn Russel's Profile")
window.geometry("600x600")
window.resizable(False,True)
window.configure(bg = "pink", cursor = "cross")

label1 = rus.Label(window, text = "Student Profile",
                   font = ("Arial", 20, "bold"),
                   fg = "black",
                   bg = "pink",
                   anchor = "center"
                   )
label1.pack(padx = 10, pady = 20)

label2 = rus.Label(window, text = "Name : Glenn Russel M. Tiangco",
                   font = ("Arial", 12, "normal"),
                   fg = "black",
                   bg = "pink"
                   )
label2.pack(anchor = "w", padx = 10, pady = 10)

label3 = rus.Label(window, text = "Age : 18 years old",
                   font = ("Arial", 12, "normal"),
                   fg = "black",
                   bg = "pink"
                   )
label3.pack(anchor = "w", padx = 10, pady = 10)

label4 = rus.Label(window, text = "Course : BSIT",
                   font = ("Arial", 12, "normal"),
                   fg = "black",
                   bg = "pink"
                   )
label4.pack(anchor = "w", padx = 10, pady = 10)

label5 = rus.Label(window, text = "Birthday : July 24, 2007",
                   font = ("Arial", 12, "normal"),
                   fg = "black",
                   bg = "pink"
                   )
label5.pack(anchor = "w", padx = 10, pady = 10)

label6 = rus.Label(window, text = "Motto :",
                   font = ("Arial", 12, "normal"),
                   fg = "black",
                   bg = "pink"
                   )
label6.pack(anchor = "w", padx = 10, pady = 10)

label7 = rus.Label(window, text = "\"Love yourself before you love others\"",
                   font = ("Arial", 12, "italic"),
                   fg = "black",
                   bg = "pink"
                   )
label7.pack(anchor = "w", padx = 25, pady = 10)

window.mainloop()