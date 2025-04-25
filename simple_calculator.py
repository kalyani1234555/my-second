import tkinter as tk
from calculator_widgets import CalculatorGrid

main_window_padding = 8

main_window = tk.Tk()
main_window.title("CalculatorButton test")
main_window.geometry('640x480')
main_window['padx'] = main_window_padding

 
btn = CalculatorGrid(main_window)
btn.grid(row=1, column=0, sticky="nsew")

main_window.mainloop()
