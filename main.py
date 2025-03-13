import tkinter as tk
from src.ui.start_menu_ui import StartMenuUI
from src.ui.character_creation_ui import CharacterCreationUI
from src.ui.combat_simulation_ui import CombatSimulationUI
from src.ui.select_character_ui import SelectCharacterUI

def open_character_creation(current_window):
    current_window.destroy()
    root = tk.Tk()
    app = CharacterCreationUI(root, open_combat_simulation)
    root.mainloop()

def open_combat_simulation(character_data=None, current_window=None):
    if current_window:
        current_window.destroy()
    root = tk.Tk()
    app = CombatSimulationUI(root)
    root.mainloop()

def main():
    root = tk.Tk()
    app = StartMenuUI(root, open_character_creation, open_combat_simulation)
    root.mainloop()

if __name__ == "__main__":
    main()