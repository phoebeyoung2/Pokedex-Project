import pypokedex as pkd
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

pokemon = pkd.get(name='charmander')

print(pokemon.dex)
print(pokemon.name)
print(pokemon.abilities)
print(pokemon.types)
