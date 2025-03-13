from tkinter import Tk, Frame, Button, Label, StringVar, messagebox

class MainUI:
    def __init__(self, master):
        self.master = master
        master.title("Pathfinder 2e Battle Simulator")

        self.main_frame = Frame(master)
        self.main_frame.pack()

        self.title_label = Label(self.main_frame, text="Welcome to Pathfinder 2e Battle Simulator", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.start_button = Button(self.main_frame, text="Start Battle", command=self.start_battle)
        self.start_button.pack(pady=5)

        self.character_button = Button(self.main_frame, text="Create Character", command=self.create_character)
        self.character_button.pack(pady=5)

        self.quit_button = Button(self.main_frame, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

    def start_battle(self):
        messagebox.showinfo("Start Battle", "Battle simulation will start here.")

    def create_character(self):
        messagebox.showinfo("Create Character", "Character creation interface will open here.")

if __name__ == "__main__":
    root = Tk()
    main_ui = MainUI(root)
    root.mainloop()