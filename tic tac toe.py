import random

# Initialize the board
board = [" " for _ in range(9)]


def print_board():
  print()
  print(f" {board[0]} | {board[1]} | {board[2]} ")
  print("---+---+---")
  print(f" {board[3]} | {board[4]} | {board[5]} ")
  print("---+---+---")
  print(f" {board[6]} | {board[7]} | {board[8]} ")
  print()


def check_winner(b, player):
  win_conditions = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],  # Rows
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],  # Columns
      [0, 4, 8],
      [2, 4, 6],  # Diagonals
  ]
  for condition in win_conditions:
    if b[condition[0]] == b[condition[1]] == b[condition[2]] == player:
      return True
  return False


def is_board_full(b):
  return " " not in b


def get_computer_move(b):
  # 1. Check if computer can win in the next move
  for i in range(9):
    if b[i] == " ":
      b[i] = "O"
      if check_winner(b, "O"):
        return i
      b[i] = " "

  # 2. Check if human can win in the next move, and block them
  for i in range(9):
    if b[i] == " ":
      b[i] = "X"
      if check_winner(b, "X"):
        b[i] = " "
        return i
      b[i] = " "

  # 3. Take the center if available
  if b[4] == " ":
    return 4

  # 4. Take a random available corner or edge
  empty_spots = [i for i, spot in enumerate(b) if spot == " "]
  return random.choice(empty_spots)


def play_game():
  print("Welcome to Tic-Tac-Toe!")
  print("You are 'X' and the computer is 'O'.")
  print("Positions are numbered from 0 to 8 like this:")
  print(" 0 | 1 | 2 ")
  print("---+---+---")
  print(" 3 | 4 | 5 ")
  print("---+---+---")
  print(" 6 | 7 | 8 \n")

  while True:
    print_board()

    # Human turn
    try:
      move = int(input("Enter your move (0-8): "))
      if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move. Try again.")
        continue
    except ValueError:
      print("Please enter a number between 0 and 8.")
      continue

    board[move] = "X"

    if check_winner(board, "X"):
      print_board()
      print("Congratulations! You win!")
      break

    if is_board_full(board):
      print_board()
      print("It's a draw!")
      break

    # Computer turn
    print("Computer is making a move...")
    comp_move = get_computer_move(board)
    board[comp_move] = "O"

    if check_winner(board, "O"):
      print_board()
      print("Computer wins! Better luck next time.")
      break

    if is_board_full(board):
      print_board()
      print("It's a draw!")
      break


if __name__ == "__main__":
  play_game()
