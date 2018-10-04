board = [
	".........",
	"5.367....",
	"9..3421..",
	".....4...",
	"..1...72.",
	"..2.1....",
	".3......9",
	".8.1..2..",
	"...75.8.6"
]

def main():
	global board
	for idx, line in enumerate(board):
		board[idx] = list(line)
	
	#solve()
	print(getPossibilities(2,2))
	
def solve():
	global board
	for i in range(0,9):
		for j in range(0,9):
			possibilities = getPossibilities(i,j)
			if possibilities == False:
				continue
			if len(possibilities) == 1:
				board[i][j] = possibilities[0]

def getPossibilities(i,j):
	global board
	if board[i][j] != '.':
		return False

	possibilities = {str(n) for n in range(1,10)}

	for val in board[i]:
		possibilities -= set(val)

	for idx in range(0,9):
		possibilities -= set(board[idx][j])

	iStart = (i // 3) * 3
	jStart = (j // 3) * 3

	subboard = board[iStart:iStart+3]
	for idx, row in enumerate(subboard):
		subboard[idx] = row[jStart:jStart+3]

	for row in subboard:
		for col in row:
			possibilities -= set(col)

	return list(possibilities)

main()