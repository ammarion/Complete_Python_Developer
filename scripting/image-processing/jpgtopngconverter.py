from PIL import Image, ImageFilter
import os
import sys

# Grab first and second argument
# check is new/ exists, if not create it
# loop through pokedex
# convert images t png
# save to new folder

old = sys.argv[1]
new = sys.argv[2]


def img_dir(new_dir, old_dir):
    if new is not None and not os.path.exists(new_dir):
        try:
            os.mkdir(new)
        except OSError as e:
            print(e)


def convert_img(old_dir, new_dir):
    if old is not None:
        try:
            os.chdir(old_dir)
            with os.scandir("./") as it:
                for entry in it:
                    if entry.is_file():
                        print(entry.name)
                        img = Image.open(entry.name)
                        clean_name = os.path.splitext(entry.name)[0]
                        print(img)
                        img.save(f"../{new_dir}/{clean_name}.png", "png")
                        print(img)

        except OSError as e:
            print(e)


if __name__ == "__main__":
    img_dir(new, old)
    convert_img(old, new)
