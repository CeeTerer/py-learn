import tkinter

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(pady=40, padx=40)


def miles_to_km():
    # print("I got clicked")
    miles = int(miles_input.get())
    km = str(miles * 1.609)
    result.config(text=km)


# Entry
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

result = tkinter.Label()
result.grid(column=1, row=1)

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# label
is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km = tkinter.Label(text="km")
km.grid(column=2, row=1)

miles = tkinter.Label(text="miles")
miles.grid(column=2, row=0)

window.mainloop()
