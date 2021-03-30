from tkinter import *

window = Tk()
window.minsize(width=250, height=250)
window.title("Mile to Km Converter")


def convert():
    miles = float(input_miles.get())
    km = round(miles * 1.6)
    label_amount.config(text=km)


input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_equal = Label(text="is equal to")
label_amount = Label(text="0")
label_km = Label(text="Km")
label_miles.grid(row=0, column=2)
label_equal.grid(row=1, column=0)
label_amount.grid(row=1, column=1)
label_km.grid(row=1, column=2)

button_calc = Button(text="Calculate", command=convert)
button_calc.grid(row=2, column=1)

window.mainloop()
