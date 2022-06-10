import tkinter as tk


def bmiClick():
    h = (float(hIn.get()))/100
    w = float(wIn.get())
    BMI = w/(h*h)
    lab5.config(text=str(round(BMI, 2)))


mywin = tk.Tk()
mywin.title("My frist pyhon win program")
mywin.geometry("300x150")

lab1 = tk.Label(mywin, text="Input your name")
lab1.grid(row=0, column=0)

nameIn = tk.Entry(mywin, width=15)
nameIn.grid(row=0, column=1)

lab2 = tk.Label(mywin, text="Input your height in cm")
lab2.grid(row=1, column=0)

hIn = tk.Entry(mywin, width=15)
hIn.grid(row=1, column=1)

lab3 = tk.Label(mywin, text="Input your height in kg")
lab3.grid(row=2, column=0)

wIn = tk.Entry(mywin, width=15)
wIn.grid(row=2, column=1)

lab4 = tk.Label(mywin, text="Your BMI is :")
lab4.grid(row=3, column=0)

lab5 = tk.Label(mywin, text="")
lab5.grid(row=3, column=1)

bmiBut = tk.Button(mywin, text="Click", command=bmiClick)
bmiBut.grid(row=3, column=2)


mywin.mainloop()
