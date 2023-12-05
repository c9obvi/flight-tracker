import tkinter as tk
from tkinter import scrolledtext

def show_popup(json_data):
    # Create a new tkinter window
    window = tk.Tk()
    window.title("Flight Information")

    # Create a scrolled text area widget
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
    text_area.pack(padx=10, pady=10)

    # Insert the JSON data into the text area
    text_area.insert(tk.INSERT, json_data)

    # Disable editing the text area and set the cursor to the beginning
    text_area.configure(state='disabled')
    text_area.yview_moveto(0)

    # Run the tkinter event loop
    window.mainloop()
