import tkinter as tk
from tkinter import END

root = tk.Tk()

root.geometry("500x500")
root.title("Calculator")

label = tk.Label(root, text="Calculator", font=('Arial', 18))
label.pack()

#Input placeholder
textbox = tk.Text(root, height=5, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

#NUMBER PAD
button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

r = 0
c = 0

for i in range(9):
    AAAA = str(i+1)
    btn = tk.Button(button_frame, text=AAAA, font=('Arial', 16), command=lambda AAAA=AAAA: textbox.insert(END, AAAA))
    btn.grid(row=r, column=c, sticky=tk.W + tk.E)
    c += 1
    if c == 3:
        r += 1
        c = 0

button_frame.pack(fill='x')
root.mainloop()