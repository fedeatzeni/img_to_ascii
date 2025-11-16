from PIL import Image # py 3.14 not supported
import os

ascii_chars = "@%#*+=-:. "
# ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def pixel_to_ascii(pixel):
    return ascii_chars[pixel * len(ascii_chars) // 256] # pixel è un valore 0-255 (scala di grigi)

BASE = os.path.dirname(os.path.abspath(__file__))  # script directory
IMG_FOLDER = os.path.join(BASE, "imgs")            # entra in imgs

IMG_FOLDER = os.path.abspath(IMG_FOLDER)           # normalizza il percorso

print("Cartella immagini:", IMG_FOLDER)

name = input("Insert file name (es: Name.jpg): ")

PATH = os.path.join(IMG_FOLDER, name)

img = Image.open(PATH)
img = img.resize((125, 75))  # resize
img = img.convert("L")       # scale of gray

ascii_art = []

for y in range(img.height):
    row = ""
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        row += pixel_to_ascii(pixel)
    ascii_art.append(row)
    
base_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(base_path, "output.txt")

with open(output_path, "w") as f:
    f.write("\n".join(ascii_art))
    
print("Done!")