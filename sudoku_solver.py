deska = [
[0,7,3,0,9,0,0,0,6],
[0,0,0,0,2,0,0,4,0],
[0,0,0,0,0,5,0,7,0],
[0,0,0,6,8,0,0,1,0],
[5,0,0,0,0,0,0,2,0],
[0,0,0,0,0,4,6,0,0],
[2,0,9,0,0,0,7,0,0],
[7,0,0,1,0,0,0,0,8],
[6,0,0,0,0,0,0,0,0]
]


def find_empty(board):
	for row in range(9):
		for column in range(9):
			if(board[row][column]) == 0:
				return [row,column]
	return False




def check_validity(board, coordinates,number):
	#Check current row
	for column in range(9):
		if board[coordinates[0]][column] == number and board[coordinates[0]][column] != board[coordinates[0]][coordinates[1]]:
			# print("found dupicate at [" + str(coordinates[0]) + "," + str(column) + "]")
			return False	
			
	#Check current column
	for row in range(9):
		if board[row][coordinates[1]] == number and board[row][coordinates[1]] != board[coordinates[0]][coordinates[1]]:
			# print("found dupicate at [" + str(row) + "," + str(coordinates[1]) + "]")
			return False

	# Check square
	squareX = coordinates[1] // 3
	squareY = coordinates[0] // 3


	for row in range(squareY*3,squareY*3 +3):
		for column in range(squareX*3,squareX*3 +3):
			if board[row][column] == number and row != coordinates[0] and column != coordinates[1]:
				return False



	return True



def solve(board):
	find = find_empty(board)
	if find == False:
		return True

	for i in range(1,10):
		if check_validity(board,find,i):
			board[find[0]][find[1]] = i

			if solve(board):
				return True

			board[find[0]][find[1]] = 0

	return False




def print_board(board):
	counter = 1
	for row in range(9):
		for column in range(9):
			print(board[row][column],end="  ")
			if((column+1) % 3 == 0):
				print("| ", end = "")

		if((row+1) % 3 == 0):
			print("")
			print("--------------------------------",end="")

		print("")


print_board(deska)
solve(deska)
print("",end="\n\n")
print_board(deska)

terminate = input()




