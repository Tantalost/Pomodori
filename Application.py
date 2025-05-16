from tkinter import *

window = Tk()
window.title("Pomodori")

label = Label(window, text="This will make the application")
label.pack()

window.geometry("1920x1080")
background = PhotoImage(file = "bg.gif")

label1 = Label( window, image = background)
label1.place(x = 0, y = 0)

label2 = Label( window, text = "Welcome")
label2.pack(pady = 50)

frame1 = Frame(window)
frame1.pack(pady = 20 )

button1 = Button(frame1,text="Exit")
button1.pack(pady=20)

button2 = Button( frame1, text = "Start")
button2.pack(pady = 20)

button3 = Button( frame1, text = "Reset")
button3.pack(pady = 20)

window.mainloop()