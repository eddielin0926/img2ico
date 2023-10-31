from os import path
from PIL import Image, ImageOps

def func(img_path: str):
    pre, ext = path.splitext(img_path)
    ico_path = pre + ".ico"
    print(f"Saving to {ico_path}...")

    image = Image.open(img_path)
    size = image.size
    ico = Image.new(mode="RGBA", size=(max(size), max(size)), color=(0, 0, 0, 0))
    ico.paste(image, (int((max(size)-size[0])/2), int((max(size)-size[1])/2)))
    ico.save(ico_path, format='ICO', quality=100)
