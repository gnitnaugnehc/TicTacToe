import tkinter as tk
import tkinter.messagebox as messagebox
import random
import sys

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [[" ", " ", " "] for i in range(3)]
        self.current_player = "X"
        self.create_widgets()
        
    def create_widgets(self):
        self.cells = []
        for i in range(3):
            for j in range(3):
                cell = tk.Button(self.master, text=" ", font=("Arial", 32), width=3, height=1,
                                 command=lambda i=i, j=j: self.play(i, j))
                cell.grid(row=i, column=j)
                self.cells.append(cell)
        self.new_game_button = tk.Button(self.master, text="New Game", font=("Arial", 16),
                                         command=self.new_game)
        self.new_game_button.grid(row=3, column=0, columnspan=3, pady=10)
        
    def play(self, row, col):
        if self.board[row][col] != " ":
            return
        self.board[row][col] = self.current_player
        self.cells[row*3+col].config(text=self.current_player)
        if self.check_win():
            messagebox.showinfo("Game Over", f"{self.current_player} wins!")
            self.new_game()
        elif self.check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.new_game()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            if self.current_player == "O":
                self.make_computer_move()

    def make_computer_move(self):
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.board[row][col] == " ":
                self.play(row, col)
                break

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def new_game(self):
        self.board = [[" ", " ", " "] for i in range(3)]
        self.current_player = "X"
        for cell in self.cells:
            cell.config(text=" ")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
