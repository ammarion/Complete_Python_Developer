from PIL import Image, ImageFilter

img = Image.open("./pokedex/astro.jpg")

img.thumbnail((400, 200))
img.convert("R")
img.save("./pokedex/thumbnail.jpg")
