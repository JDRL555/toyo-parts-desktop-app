from tkinter import Tk

from windows.index_window import MainWindow

from utils.logo import get_logo


root = Tk()
root.title("Toyo Parts")

root.geometry("1200x600")
root.resizable(False, False)

logo = get_logo()

root.wm_iconphoto(True, logo, logo)

main_window = MainWindow(root=root, logo=logo)
main_window.render()


root.mainloop()