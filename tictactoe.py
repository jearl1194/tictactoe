import functools as ft
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.label = ttk.Label(text="Turn: Player 1", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=3)
        self.player_1 = Player("Player 1", True)
        self.player_2 = Player("Player 2")
        self.buttons = [ttk.Button(
            command=ft.partial(self.move, i)) for i in range(9)]
        for i in range(9):
            self.buttons[i].grid(row=(i)//3+1, column=i % 3,
                                 ipadx=10, ipady=10)

    def check_winner(self, player):
        winning_moves = (448, 56, 7, 292, 146, 73, 273, 84)
        player_moves = player.moves
        for move in winning_moves:
            if (move & player_moves) in winning_moves:
                player.set_winner()
                if self.player_1.winner():
                    self.label.config(text="Winner: Player 1")
                elif self.player_2.winner():
                    self.label.config(text="Winner: Player 2")
        if player.winner():
            for btn in self.buttons:
                btn.config(state=tk.DISABLED)

    def move(self, i):
        if self.player_1.turn:
            self.player_1.move(i)
            self.buttons[i].config(text="X")
            self.label.config(text="Turn: Player 2")
            self.check_winner(self.player_1)
            self.player_2.turn = True
        elif self.player_2.turn:
            self.player_2.move(i)
            self.buttons[i].config(text="O")
            self.label.config(text="Turn: Player 1")
            self.check_winner(self.player_2)
            self.player_1.turn = True
        self.buttons[i].config(state=tk.DISABLED)


class Player():
    def __init__(self, name="Player", turn=False):
        self._name = name
        self.turn = turn
        self.moves = 0
        self._winner = False

    def move(self, i):
        self.moves += 2**(8-i)
        self.turn = False

    def set_winner(self):
        self._winner = True

    def winner(self):
        return self._winner


if __name__ == "__main__":
    app = App()
    app.mainloop()
