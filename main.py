import pypokedex as pkd
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

# Create a user interface window
window = tk.Tk()
window.geometry("600x500")
window.title("Pokedex")
window.config(padx=10, pady=10)

# Write a function that creates labels
def create_label(tk_interface, text, padx, pady, font=True, fontsize):

    # Initialise label
    if text != None:
        label = tk.Label(tk_interface, text=text)
    else:
        label = tk.Label(tk_interface)

    if font is True:
        label.config(font=("Arial", fontsize))

    label.pack(padx=padx, pady=pady)

    return label


tite_label = create_label(window, text="Phoebe's Pokedex", padx=10, pady=10, font=True, fontsize=32)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=30, pady=30)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

# Write function that finds and displays information on the pokemon given by the user window input

window.mainloop()
