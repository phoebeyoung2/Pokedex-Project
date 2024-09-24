import pypokedex as pkd
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

# Create a GUI using library tkinter
window = tk.Tk()
window.geometry("600x500")
window.title("Pokedex")
window.config(padx=10, pady=10)

"""
creates a label for a Tkinter GUI window

Parameters
----------
tk_interface : tkinter.tk
             application window
text         : string
             text to display
padx         : Integer
             horizontal padding on the widget
pady         : Integer
             vertical padding on the widget
font         : Boolean
             True for text labels
fontsize     : Integer
             adjusts the size of the label text

Returns
-------
label       : tkinter.label
            text or image display

"""
def create_label(tk_interface, text, padx, pady, font=True, fontsize=20):

    # Initialise label
    if text != None:
        label = tk.Label(tk_interface, text=text)
    else:
        label = tk.Label(tk_interface)

    if font is True:
        label.config(font=("Comfortaa", fontsize))

    label.pack(padx=padx, pady=pady)

    return label

# Use create label function to initialise displays for the pokedex GUI
title_label = create_label(window, text="Pokedex", padx=10, pady=5, font=True, fontsize=32)

pokemon_image = create_label(window, text=None, padx=10, pady=5, font=False)

pokemon_information = create_label(window, text=None,padx=10, pady=5, font=True, fontsize=20)

pokemon_types = create_label(window, text=None, padx=10, pady=10, font=True, fontsize=18)

pokemon_height_weight = create_label(window, text=None, padx=10, pady=10,font=True, fontsize=18)

"""
Function finds and displays information on a pokemon based on the user input

"""
def load_pokemon():
    pokemon = pkd.get(name=text_id_name.get(1.0,"end-1c")) # Extract users input from the text input area

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    print(response)
    image = PIL.Image.open(BytesIO(response.data))
    image = image.resize((200, 200), PIL.Image.LANCZOS)

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_height_weight.config(text=f"Height: {pokemon.height/10} m    Weight: {pokemon.weight/10} kg ")
    pokemon_types.config(text="Type: " + " - ".join([i for i in pokemon.types]))


label_id_name = create_label(window,text="Pokemon ID or Name", padx=10, pady=10, font=True, fontsize=18)

# Create a text input area for the user
text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

# Create a button that triggers load pokemon function when pressed
btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Comfortaa", 18))
btn_load.pack(padx=10, pady=10)

window.mainloop()
