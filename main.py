from src.ui.combat_simulation_ui import CombatSimulationUI
import tkinter as tk

def main():
    root = tk.Tk()
    app = CombatSimulationUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()