import os
import platform
from classes import *
class Menu():
    def __init__(self, title, options, path=""):
        self.title: str = title
        self.path: str = path
        self.options: list[MenuOption] = options

    def display(self, selected):
        clearscreen()
        size = os.get_terminal_size()
        print("┌" + "─" * (size.columns - 2) + "┐")
        print("│" + self.title.center(size.columns - 2) + "│")
        print("│" + self.path.ljust(size.columns - 2) + "│")
        print("├" + "─" * (size.columns - 2) + "┤")
        for i in range(len(self.options)):
            j = f"{}"
            "│" + i.ljust(size.columns - 2) + "│"
        
class MenuOption():
    def __init__(self, text: str, purpose: function):
        self.text = text
        self.purpose = purpose
