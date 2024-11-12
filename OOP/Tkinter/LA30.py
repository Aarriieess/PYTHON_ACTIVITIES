import tkinter as tk

anime_title = "One Piece"

root = tk.Tk()
root.title(f"LA30")
root.geometry("500x500")

def display_text():
    print(f"My favorite anime is {anime_title}")

button = tk.Button(
    root,
    text="Click me",
    command=display_text
)

button.pack(
    padx=100,
    pady=225
)


root.mainloop()

