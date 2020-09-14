import tkinter as tk

window = tk.Tk()
choice_a = tk.Frame()
choice_i = tk.Frame()

button_a = tk.Button(
    text="Alexa",
    width=10,
    height=5,
    master=choice_a
)
button_a.pack()

button_i = tk.Button(
    text="Individual",
    width=10,
    height=5,
    master=choice_i
)
button_i.pack()

choice_a.pack()
choice_i.pack()

window.mainloop()