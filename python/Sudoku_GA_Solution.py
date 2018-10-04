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

	def get_horizontal(self, position):
		row_start = (position // 9)* 9
		return self.board[row_start:row_start+9]

	def get_vertical(self, position):
		column_start = position % 9
		return self.board[column_start: len(self.board): 9]

	def get_box(self, position):
		box_col = ((position % 9) // 3) * 3
		box_row = (position // 27) * 3
		box_nums = []

		for i in range(box_row, box_row+3):
			for j in range(box_col, box_col + 3):
				box_nums.append(self.board[i * 9 + j])

		return box_nums

	def check_solved(self):
		if '0' in self.board:
			return False
		return True

	def solve(self):
		has_changed = True

		while has_changed:
			has_changed = False

			for position in range(len(self.board)):
				if self.board[position] == '0':
					# Get the numbers
					# Find the numbers that missing
					# If there is only one num missing, fill it in




test_board1 = '619030040270061008000047621486302079000014580031009060005720806320106057160400030'

board1 = SudokuBoard(test_board1)
board1.print_board()
print('horizontal of 23 is: ')
print(board1.get_horizontal(23))

print('vertical of 25 is: ')
print(board1.get_vertical(25))

print('box of position 34 is: ')
print(board1.get_box(34))