import tkinter as tk
import os
from tkinter import messagebox
from src.ui.select_character_ui import SelectCharacterUI

class StartMenuUI:
    def __init__(self, master, open_character_creation, open_combat_simulation):
        self.master = master
        self.master.title("Start Menu")
        self.open_character_creation = open_character_creation
        self.open_combat_simulation = open_combat_simulation
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.select_character_button = tk.Button(self.frame, text="Select Character", command=self.select_character)
        self.select_character_button.pack(pady=10)

        self.create_character_button = tk.Button(self.frame, text="Create Character", command=lambda: self.open_character_creation(self.master))
        self.create_character_button.pack(pady=10)

        # Disable the "Select Character" button if the folder is empty
        if not os.listdir(os.path.join("data", "character")):
            self.select_character_button.config(state=tk.DISABLED)

    def select_character(self):
        self.master.destroy()
        root = tk.Tk()
        app = SelectCharacterUI(root, self.open_combat_simulation)
        root.mainloop()