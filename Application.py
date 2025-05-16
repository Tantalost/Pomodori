import tkinter as tk

window = tk.Tk()
window.title("Pomodori")

label = tk.Label(window, text="This will make the application")
label.pack()

window.geometry("1920x1080")
background = PhotoImage(file = "bg.gif")

window.mainloop()