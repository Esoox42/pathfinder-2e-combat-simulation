import tkinter as tk
from tkinter import messagebox
import json
import os

class CharacterCreationUI:
    def __init__(self, master, on_submit):
        self.master = master
        self.master.title("Character Creation")
        self.on_submit = on_submit
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Add input for character name
        tk.Label(self.frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.labels = ["Strength", "Dexterity", "Constitution", "Charisma", "Intelligence", "Wisdom"]
        self.entries = {}

        for i, label in enumerate(self.labels):
            tk.Label(self.frame, text=label).grid(row=i+1, column=0, padx=5, pady=5)
            entry = tk.Entry(self.frame)
            entry.grid(row=i+1, column=1, padx=5, pady=5)
            self.entries[label] = entry

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit)
        self.submit_button.grid(row=len(self.labels)+1, column=0, columnspan=2, pady=10)

    def submit(self):
        character_name = self.name_entry.get().strip()
        if not character_name:
            messagebox.showerror("Invalid Input", "Name cannot be empty.")
            return

        character = {}
        for label in self.labels:
            value = self.entries[label].get()
            if not value.isdigit():
                messagebox.showerror("Invalid Input", f"{label} must be a number.")
                return
            character[label] = int(value)

        # Ensure the directory exists
        directory = os.path.join("data", "character")
        os.makedirs(directory, exist_ok=True)

        # Save the character data to a JSON file named after the character
        file_path = os.path.join(directory, f"{character_name}.json")
        with open(file_path, "w") as f:
            json.dump(character, f, indent=4)

        messagebox.showinfo("Success", "Character saved successfully!")
        self.master.destroy()  # Close the character creation window

        # Call the callback function to open the combat simulation window
        self.on_submit()