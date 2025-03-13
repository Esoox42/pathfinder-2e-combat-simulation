import tkinter as tk
from tkinter import messagebox
import os
import json

class SelectCharacterUI:
    def __init__(self, master, open_combat_simulation):
        self.master = master
        self.master.title("Select Character")
        self.open_combat_simulation = open_combat_simulation
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.character_listbox = tk.Listbox(self.frame)
        self.character_listbox.pack(padx=10, pady=10)

        self.load_characters()

        self.go_to_combat_button = tk.Button(self.frame, text="Go to Combat", command=self.go_to_combat)
        self.go_to_combat_button.pack(pady=10)

    def load_characters(self):
        directory = os.path.join("data", "character")
        character_files = os.listdir(directory)
        for character_file in character_files:
            self.character_listbox.insert(tk.END, character_file)

    def go_to_combat(self):
        selected_character = self.character_listbox.get(tk.ACTIVE)
        if not selected_character:
            messagebox.showerror("No Selection", "Please select a character.")
            return

        character_path = os.path.join("data", "character", selected_character)
        with open(character_path, "r") as f:
            character_data = json.load(f)
            print(character_data)  # For now, just print the character data

        self.master.destroy()
        self.open_combat_simulation(character_data)