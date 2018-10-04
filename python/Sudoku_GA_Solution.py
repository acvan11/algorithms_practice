class SudokuBoard():
	def __init__(self, board):
		self.board = list(board)

	def print_board(self):
		for i in range(0, len(self.board), 9):
			if i%27 == 0:
				print()

			temp = ''
			for j in range(i, i+9):
				temp += self.board[j] + ' '

				if (j + 1) % 3 == 0:
					temp += ' '
			print(temp)




test_board1 = '619030040270061008000047621486302079000014580031009060005720806320106057160400030'

board1 = SudokuBoard(test_board1)
board1.print_board()