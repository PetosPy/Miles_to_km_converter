from tkinter import *

window = Tk()
#window.minsize(width= 300, height=200)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile_entry = Entry(width=8, font=("Ariel", 15, "bold"))
mile_entry.grid(column=1, row=4)

miles = Label(text="Miles",font=("Ariel", 15, "bold"))
miles.grid(column=3, row=4)

is_equal_to = Label(text="is equal to",font=("Ariel", 15, "bold"))
is_equal_to.grid(column=0, row= 5)

to_kms = Label(text=0,font=("Ariel", 15, "bold"))
to_kms.grid(column=1, row=5)

km = Label(text="Km",font=("Ariel", 15, "bold"))
km.grid(column=3, row=5)


def button_pressed():
	miles = int(mile_entry.get())
	answer = round(miles * 1.609)
	to_kms.config(text=answer)


button =Button(text="Calculate", command=button_pressed)
button.grid(column=1, row=6)



window.mainloop()