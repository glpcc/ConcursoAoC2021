def check_if_completed(board):
	#check rows 
	for i in range(len(board)):
		if sum([j for j in board[i] if j < 0]) == -5:
			return True
	#check colums
	for i in range(len(board[0])):
		if sum([board[j][i] for j in range(len(board)) if board[j][i] < 0 ]) == -5:
			return True

	return False

def check_number(number,boards):
	new_boards = boards
	for i in range(len(boards)):
		for j in range(len(boards[i])):
			if boards[i][j] == int(number):
				new_boards[i][j] = -1
				print('hey')
	
	return new_boards

def calculate_value(board,number):
	sum_board = sum([ sum([j for j in i if j>0]) for i in board])
	print(sum_board*number)



file = open('4/input.txt')
lines = file.readlines()
bingo_numbers = [int(i) for i in lines[0].strip().split(',')]
bingo_boards = []
for i in range(2,len(lines),6):
	board = [[k.strip() for k in lines[i+j].split(' ')] for j in range(5)]
	board = [[int(w) for w in k if w != ''] for k in board]
	bingo_boards.append(board)

finished = False
print(bingo_numbers)
for i in bingo_numbers:
	bingo_boards = [check_number(i,n) for n in bingo_boards]
	print(bingo_boards)
	for j in range(len(bingo_boards)):
		try:
			if check_if_completed(bingo_boards[j]):
				last_winner = bingo_boards[j]
				last_winner_num = i
				bingo_boards.pop(j)
		except:
			...

calculate_value(last_winner,last_winner_num)


	

