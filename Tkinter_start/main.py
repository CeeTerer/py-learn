import tkinter

window = tkinter.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
my_label = tkinter.Label(text="I am a label", font=("arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label["text"] = "My label"
my_label.config(text="My text")


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="Click me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=3)


window.mainloop()
