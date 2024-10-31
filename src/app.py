from tkinter import Tk

from windows.index.index import MainWindow

from utils.image import get_image


root = Tk()
root.title("Toyo Parts")

root.geometry("1200x600")
root.resizable(False, False)

logo = get_image("logo", (300, 100))
local = get_image("local", (600, 600))

root.wm_iconphoto(True, logo, logo)

main_window = MainWindow(root=root, logo=logo, local=local)
main_window.render()


root.mainloop()