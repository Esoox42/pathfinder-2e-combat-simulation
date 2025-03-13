import tkinter as tk
#import sv_ttk

class CombatSimulationUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Combat Simulation")
        self.board_size = 11  # 11x11 grid
        self.square_size = 50
        self.turn = "Player"
        self.selected_piece = None
        self.highlighted_moves = []
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.left_frame = tk.Frame(self.frame)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.canvas_frame = tk.Frame(self.frame)
        self.canvas_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.canvas = tk.Canvas(self.canvas_frame, width=self.board_size * self.square_size + 1, height=self.board_size * self.square_size + 1)
        self.canvas.pack()
        self.draw_grid()

        self.right_frame = tk.Frame(self.frame)
        self.right_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Position players in the middle of their respective columns
        player_start_x = (self.board_size // 2) * self.square_size + self.square_size // 2
        player_start_y = self.square_size // 2
        enemy_start_y = (self.board_size - 1) * self.square_size + self.square_size // 2

        # Size pawns
        pawn_radius = 10

        self.player_piece = self.canvas.create_oval(player_start_x - pawn_radius, player_start_y - pawn_radius, player_start_x + pawn_radius, player_start_y + pawn_radius, fill="blue", tags="player")
        self.enemy_piece = self.canvas.create_oval(player_start_x - pawn_radius, enemy_start_y - pawn_radius, player_start_x + pawn_radius, enemy_start_y + pawn_radius, fill="red", tags="enemy")
        self.canvas.tag_bind("player", "<Button-1>", self.select_piece)
        self.canvas.tag_bind("enemy", "<Button-1>", self.select_piece)

        self.player1_label = tk.Label(self.left_frame, text="Player 1", font=("Helvetica", 16))
        self.player1_label.pack(pady=10)
        self.player2_label = tk.Label(self.right_frame, text="Player 2", font=("Helvetica", 16))
        self.player2_label.pack(pady=10)

        self.update_turn_label()

    def draw_grid(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.canvas.create_rectangle(i * self.square_size, j * self.square_size, (i + 1) * self.square_size, (j + 1) * self.square_size, outline="black")

    def select_piece(self, event):
        piece = self.canvas.find_withtag(tk.CURRENT)
        if (self.turn == "Player" and "player" in self.canvas.gettags(piece)) or (self.turn == "Enemy" and "enemy" in self.canvas.gettags(piece)):
            self.selected_piece = piece
            self.highlight_moves(piece)

    def highlight_moves(self, piece):
        self.clear_highlights()
        x, y, _, _ = self.canvas.coords(piece)
        col = int(x // self.square_size)
        row = int(y // self.square_size)
        possible_moves = [
            (col - 1, row), (col + 1, row),
            (col, row - 1), (col, row + 1),
            (col - 1, row - 1), (col + 1, row - 1),
            (col - 1, row + 1), (col + 1, row + 1)
        ]
        for move in possible_moves:
            if 0 <= move[0] < self.board_size and 0 <= move[1] < self.board_size:
                center_x = move[0] * self.square_size + self.square_size // 2
                center_y = move[1] * self.square_size + self.square_size // 2
                highlight = self.canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="green", tags="highlight")
                self.highlighted_moves.append(highlight)
                self.canvas.tag_bind(highlight, "<Button-1>", self.move_piece)

    def clear_highlights(self):
        for highlight in self.highlighted_moves:
            self.canvas.delete(highlight)
        self.highlighted_moves = []

    def move_piece(self, event):
        if self.selected_piece:
            col = event.x // self.square_size
            row = event.y // self.square_size
            center_x = col * self.square_size + self.square_size // 2
            center_y = row * self.square_size + self.square_size // 2
            pawn_radius = 10  # Ensure the pawns remain the same size when moved
            self.canvas.coords(self.selected_piece, center_x - pawn_radius, center_y - pawn_radius, center_x + pawn_radius, center_y + pawn_radius)
            self.turn = "Enemy" if self.turn == "Player" else "Player"
            self.selected_piece = None
            self.clear_highlights()
            self.update_turn_label()

    def update_turn_label(self):
        if self.turn == "Player":
            self.player1_label.config(fg="blue")
            self.player2_label.config(fg="black")
        else:
            self.player1_label.config(fg="black")
            self.player2_label.config(fg="red")