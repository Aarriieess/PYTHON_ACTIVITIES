import tkinter as tk

name = "Jan Aries Sarabia"
section = "BSCS-2A"

root = tk.Tk()
root.title(f"LA29")
root.geometry("500x500")

label = tk.Label(root, text=f"OOP LA29 {name} {section}")
label.grid(row=0, column=0, padx=150, pady=225)


root.mainloop()

