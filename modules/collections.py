"""importing."""
from googletrans import Translator


with open("test.txt", mode="r") as f:
    text = f.read()
    print(text)

    translator = Translator()
    print(translator.translate(text))

