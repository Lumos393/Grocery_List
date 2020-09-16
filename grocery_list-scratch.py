import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup
from googlesearch import search
import requests

window = tk.Tk()
choice_a = tk.Frame(
    bg="black",
    relief=tk.GROOVE
)
choice_i = tk.Frame(
    bg="black",
    relief=tk.GROOVE
)

button_a = tk.Button(
    text="Alexa",
    width=20,
    height=5,
    bg="darkgray",
    fg="white",
    master=choice_a
)
button_a.pack()

button_i = tk.Button(
    text="Individual",
    width=20,
    height=5,
    bg="darkgray",
    fg="white",
    master=choice_i
)
button_i.pack()

title = tk.Label(
    text="Thank you for using Sam's Grocery Thingy! Please select if you would like to enter items individually or pull from an Alexa list:"
)

choice_a.pack(
    fill=tk.BOTH,
    side=tk.LEFT,
    expand=True
)
choice_i.pack(
    fill=tk.BOTH,
    side=tk.RIGHT,
    expand=True
)

window.mainloop()

r = requests.get('https://www.walmart.com')
#https://www.walmart.com/search/?query=pumpkin%20pie%20filling

