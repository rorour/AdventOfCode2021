class Bingo:
    draw = []
    boards = []
    ROWS_PER_BOARD = 5
    num_boards_won = 0

    class Board:
        class Square:
            def __init__(self, value):
                self.value = value
                self.marked = False

            def __str__(self):
                return self.value + ('* ' if self.marked else ' ')

            def mark(self):
                self.marked = True

        def __init__(self, rows):
            self.rows = []
            self.won = False
            for row in rows:
                self.rows.append([Bingo.Board.Square(value) for value in row.split(' ') if value != ''])

        def __str__(self):
            board_str = ''
            for row in self.rows:
                board_str += ''.join([str(sq) for sq in row]) + '\n'
            return board_str

        def all_squares(self):
            all_squares = []
            for row in self.rows:
                all_squares += [sq for sq in row]
            return all_squares

    class Win(Exception):
        def __init__(self, board, last, score):
            self.message = f'Winner with last called {last} and score {score}! Board is \n{board}'

    def __init__(self, input):
        self._process_input(input)

    def play(self, play_to_lose=False):
        try:
            for n in self.draw:
                self._mark_boards(n, play_to_lose=play_to_lose)
        except Bingo.Win as win:
            print(win.message)

    def _calculate_score(self, board, last):
        return int(last) * sum([int(sq.value) for sq in board.all_squares() if not sq.marked])

    def _check_board_for_winner(self, board, last, play_to_lose=False):
        # check rows
        for row in board.rows:
            win = True
            for sq in row:
                if not sq.marked:
                    win = False
                    break
            if win:
                self._handle_win(board, play_to_lose, last)

        # check columns
        for col in range(len(board.rows[0])):
            win = True
            for sq in [row[col] for row in board.rows]:
                if not sq.marked:
                    win = False
                    break
            if win:
                self._handle_win(board, play_to_lose, last)

    def _mark_boards(self, called, play_to_lose=False):
        for board in self.boards:
            for row in board.rows:
                for sq in row:
                    if sq.value == called:
                        sq.mark()
                        self._check_board_for_winner(board, called, play_to_lose=play_to_lose)

    def _process_input(self, input):
        with open(input, 'r') as infile:
            data = [line for line in infile]
        self.draw = [x.strip('\n') for x in data[0].split(',')]

        for i in range(2, len(data), self.ROWS_PER_BOARD + 1):
            self.boards.append(Bingo.Board([row.strip('\n') for row in data[i:i + self.ROWS_PER_BOARD]]))

    def _handle_win(self, board, play_to_lose, last):
        if play_to_lose and not board.won:  # see if this is the last board to win
            self.num_boards_won += 1
            board.won = True
            if self.num_boards_won == len(self.boards):
                print(f'Found last board to win:')
                raise Bingo.Win(board, last, self._calculate_score(board, last))
        elif not play_to_lose:  # normal case, we win and end the game
            raise Bingo.Win(board, last, self._calculate_score(board, last))


Bingo('../inputs/4.txt').play()
Bingo('../inputs/4.txt').play(play_to_lose=True)
