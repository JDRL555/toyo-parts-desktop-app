from PIL import Image, ImageTk
import os

def get_image(img_name: str, size: tuple):
  img = Image.open(os.path.join(os.path.curdir, f"src/public/img/{img_name}.jpg"))
  
  img = img.resize(size)
  
  logo = ImageTk.PhotoImage(img)
  
  return logo