import pypokedex as pkd
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a GUI using library tkinter
window = tk.Tk()
window.title("Pokedex")
window.config(padx=10, pady=10, bg='lightblue')

# Centralise the logo on the grid
logo_label = tk.Label(window)
logo_label.grid(row=0, column=0,columnspan=5, padx=10, pady=10, sticky="ew")

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

    label.grid(padx=padx, pady=pady)

    return label

# Create a frame for all of the pokemon information
info_frame = tk.Frame(window, bg='lightblue')
info_frame.grid(row=1, column=0, padx=10, pady=10)

# Use create label function to initialise displays for the pokedex GUI

pokemon_image = create_label(info_frame, text=None, padx=10, pady=5, font=False, bg='lightblue')

pokemon_information = create_label(info_frame, text=None,padx=10, pady=5, font=True, fontsize=20, bg='lightblue')

pokemon_types = create_label(info_frame, text=None, padx=10, pady=10, font=True, fontsize=18, bg='lightblue')

pokemon_height_weight = create_label(info_frame, text=None, padx=10, pady=10,font=True, fontsize=18, bg='lightblue')

#Create a base stats frame
stats_frame = tk.Frame(window, bg='lightblue')
stats_frame.grid(row=1, column=1, padx=10, pady=10)


def plot_stats():
    # Extract users input from the text input area
    pokemon = pkd.get(name=text_id_name.get(1.0,"end-1c")) 

    #Plot base stats
    base_stats = {
        "hp": pokemon.base_stats.hp,
        "attack": pokemon.base_stats.attack,
        "defence": pokemon.base_stats.defense,
        "Special Attack": pokemon.base_stats.sp_atk,
        "Special Defense": pokemon.base_stats.sp_def,
        "Speed": pokemon.base_stats.speed,
    }

    fig, axes = plt.subplots(figsize=(4, 5))
    axes.bar(base_stats.keys(), base_stats.values(), color='blue')
    axes.set_xticklabels(base_stats.keys(), rotation=90)
    axes.set_xlabel('Base Stats')
    axes.set_ylabel('Value')
    axes.set_title('Pokémon Base Stats')
    axes.set_facecolor('lightblue')
    fig.set_facecolor('lightblue')

    # Clear previous plots
    for widget in stats_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=stats_frame)  # Create a canvas
    canvas.draw()  # Draw the figure on the canvas

    # Place the canvas in the GUI window
    canvas.get_tk_widget().pack(padx=10, pady=10)


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

    plot_stats()

# Create a prompt for the user
label_id_name = create_label(window,text="Enter Pokémon ID or Name:", padx=10, pady=5, font=True, fontsize=16, bg='lightblue')
label_id_name.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew") 

# Create a text input area for the user
text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.grid(row=3, column=0, columnspan=2,padx=10, pady=10)

# Create a button that triggers load pokemon function when pressed
btn_load = tk.Button(window, text="Load Pokémon", command=load_pokemon)
btn_load.config(font=("Comfortaa", 18))
btn_load.grid(row=4, column=0, columnspan=2,padx=10, pady=10)

#Button aesthetics
btn_load.config(bg='white', fg='black', activebackground='blue')

window.mainloop()
