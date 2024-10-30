from PIL import Image, ImageTk
import os

def get_logo():
  print(os.path.join(os.path.curdir, "src/public/img/logo.jpg"))
  img = Image.open(os.path.join(os.path.curdir, "src/public/img/logo.jpg"))
  
  img = img.resize((300, 100))
  
  logo = ImageTk.PhotoImage(img)
  
  return logo