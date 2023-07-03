
class GameEntry:
    def __init__(self, name, score) -> None:
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self) -> str:
        return f'{self.name}, {self._score}'


class Scoreboard:
    def __init__(self, capacity = 10):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]
    
    def __str__(self) -> str:
        return f'{"|".join([ i for i in self._boards])}'
    
    def add(self, entry):
        score = entry.get_score()

        #check if there is space on the board for new entries
        #check if the last entry is lesser than the current entry score
    
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry


