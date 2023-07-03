
class TicTacToe:

    def __init__(self) -> None:
        self._board =[[' ']*3 for i in range(3)]
        self._player = 'X'

    def __str__(self):
        rows = ["|".join(self._board[r]) for r in range(3)]
        return "\n-----\n".join(rows) 

    def markP(self, i, j):
        if self._board[i][j] != ' ':
            raise ValueError("The postion is not empty")
        if 0 >= i >= 3 or 0 >= j >= 3:
            raise ValueError("Invalid board postion")
        # if self.winner() is not None:
        #     raise ValueError("Game already completed")

        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self, mark):
        board = self._board

        return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
        mark == board[1][0] == board[1][1] == board[1][2] or # row 1
        mark == board[2][0] == board[2][1] == board[2][2] or # row 2
        mark == board[0][0] == board[1][0] == board[2][0] or # column 0
        mark == board[0][1] == board[1][1] == board[2][1] or # column 1
        mark == board[0][2] == board[1][2] == board[2][2] or # column 2
        mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
        mark == board[0][2] == board[1][1] == board[2][0]) #

    def winner(self):
        for mark in "XO":
            print(mark)
            if self._is_win(mark):
                return mark
            
        return None
        


game = TicTacToe()
print("\n \n ")
game.markP(0, 1)
game.markP(1, 1)
game.markP(2, 0)
game.markP(1, 2)
game.markP(0, 2)
game.markP(1, 0)

print(game)

winner = game.winner() 
print(f"The winner is {winner}")