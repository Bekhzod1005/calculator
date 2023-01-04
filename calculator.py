from __future__ import annotations
import tkinter as tk
from tkinter import END

class ButtonCreator:
    # Buttons
    r: int
    c: int

    def __init__(self):
        self.r = 0
        self.c = 0

    def make_button(self, text, onclick=None):
        b = tk.Button(button_frame, text=text, font=('Arial', 16), command=onclick)
        b.grid(row=self.r, column=self.c, sticky=tk.W + tk.E)
        self.c += 1
        if self.c == 3:
            self.r += 1
            self.c = 0

root = tk.Tk()

root.geometry("500x500")
root.title("Calculator")

label = tk.Label(root, text="Calculator", font=('Arial', 18))
label.pack()

# Input placeholder
textbox = tk.Text(root, height=5, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

# NUMBER PAD
button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

button_creator = ButtonCreator()

for i in range(9):
    AAAA = str(i + 1)
    button_creator.make_button(AAAA, lambda AAAA=AAAA: textbox.insert(END, AAAA))

button_creator.make_button("+", lambda: textbox.insert(END, "+"))
button_creator.make_button("0", lambda: textbox.insert(END, "0"))
button_creator.make_button("-", lambda: textbox.insert(END, "-"))
button_creator.make_button("*", lambda: textbox.insert(END, "*"))
button_creator.make_button("/", lambda: textbox.insert(END, "/"))
button_creator.make_button("=", lambda: textbox.insert(END, "="))

button_frame.pack(fill='x')
root.mainloop()