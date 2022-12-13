from PIL import Image
from tkinter import Tk, filedialog

invert_color = lambda color: tuple([255-int(x) for x in color])

filename = filedialog.askopenfilename(title="Open a file", initialdir='/')

def autosave(filename):
    length = len(filename)
    last_slash = 0
    for x in range(length-1, 0, -1):
        if filename[x] == "/":
            last_slash = x+1
            break
    return filename[:last_slash]
            

with Image.open(filename) as img:
        width, height = img.size
        for y in range(height):
            for x in range(width):
                cords = x, y
                color = img.getpixel(cords)
                pix_color = invert_color(color)
                img.putpixel((x,y), pix_color)
        img = img.save(autosave(filename) + "inverted.jpg")
