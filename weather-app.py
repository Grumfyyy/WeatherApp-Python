#tkinter documentation - https://docs.python.org/3/library/tkinter.html
#tkinter entry documentation - https://python-course.eu/tkinter/entry-widgets-in-tkinter.php
from tkinter import *
from tkinter import ttk

def get_coordinates(city_name):
    print(city_name)

def main():
    root = Tk()
    root.title("Weather Application by Josef Swadi Johansson")
    root.geometry("400x400")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="City : ").grid(column=0, row = 0)

    city_input = ttk.Entry(root)
    city_input.grid(column=1, row = 0)
    
    ttk.Button(frm, text="Search", command=(lambda:get_coordinates(city_input.get()))).grid(column = 2, row=0)

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column = 0, row=2)
    root.mainloop()

main()
