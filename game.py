class TicTacToe:
    def __int__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def availableSpaces(self):
        return [i for (i, spot) in enumerate(self.board) if spot == " "]

    def emptySquares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def num_of_emptySquares(self):
        return self.board.count(' ')


def play(game, x_player, O_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.emptySquares():
        if letter == 'O':
            square = O_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square , letter):
            if print_game:
                print(letter +  f'make a move gto square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    print('It s a tie')


