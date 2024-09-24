import pypokedex as pkd
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

# Create a GUI using library tkinter
window = tk.Tk()
window.geometry("600x500")
window.title("Pokedex")
window.config(padx=10, pady=10, bg='lightblue')

logo_label = tk.Label(window)
logo_label.pack(padx=10, pady=10)

"""
Takes an image url and uses it as the GUI title display image
"""
def logo_title():
    logo_url = "https://archives.bulbagarden.net/media/upload/4/4b/Pok%C3%A9dex_logo.png"

    http = urllib3.PoolManager()
    response = http.request('GET', logo_url)

    logo_image = PIL.Image.open(BytesIO(response.data))

    image = logo_image.resize((387,140), PIL.Image.LANCZOS)

    img = PIL.ImageTk.PhotoImage(image)
    logo_label.config(image=img, bg='lightblue')
    logo_label.image = img


# Implement the logo title method
logo_title()


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
def create_label(tk_interface, text, padx, pady, font=True, fontsize=20, bg='lightblue'):

    # Initialise label
    if text != None:
        label = tk.Label(tk_interface, text=text)
    else:
        label = tk.Label(tk_interface)

    if font is True:
        label.config(font=("Comfortaa", fontsize), bg='lightblue')

    label.pack(padx=padx, pady=pady)

    return label

# Use create label function to initialise displays for the pokedex GUI

pokemon_image = create_label(window, text=None, padx=10, pady=5, font=False, bg='lightblue')

pokemon_information = create_label(window, text=None,padx=10, pady=5, font=True, fontsize=20, bg='lightblue')

pokemon_types = create_label(window, text=None, padx=10, pady=10, font=True, fontsize=18, bg='lightblue')

pokemon_height_weight = create_label(window, text=None, padx=10, pady=10,font=True, fontsize=18, bg='lightblue')

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
    pokemon_image.config(image=img, bg='lightblue')
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_height_weight.config(text=f"Height: {pokemon.height/10} m    Weight: {pokemon.weight/10} kg ")
    pokemon_types.config(text="Type: " + " - ".join([i for i in pokemon.types]))


label_id_name = create_label(window,text="Enter Pokémon ID or Name:", padx=10, pady=5, font=True, fontsize=16, bg='lightblue')

# Create a text input area for the user
text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

# Create a button that triggers load pokemon function when pressed
btn_load = tk.Button(window, text="Load Pokémon", command=load_pokemon)
btn_load.config(font=("Comfortaa", 18))
btn_load.pack(padx=10, pady=10)

#Button aesthetics
btn_load.config(bg='white', fg='black', activebackground='blue')

window.mainloop()
