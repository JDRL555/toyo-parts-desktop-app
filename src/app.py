from tkinter import Tk
from dotenv import load_dotenv

load_dotenv()

from windows.index.index import MainWindow

from utils.image import get_image
from utils.database import Base, session, engine
from utils.seed import seed

root = Tk()
root.title("Toyo Parts")

root.geometry("1200x600")
root.resizable(False, False)

logo = get_image("logo", (300, 100))
local = get_image("local", (600, 600))

root.wm_iconphoto(True, logo, logo)

main_window = MainWindow(root=root, logo=logo, local=local)
main_window.render()

if __name__ == "__main__":
  Base.metadata.create_all(engine)
  seed(session)
  root.mainloop()