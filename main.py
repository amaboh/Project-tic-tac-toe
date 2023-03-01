# -----------Global Variables
board = ["-","-", "-",
          "-", "-","-",
         "-","-","-"]

# If game is stil going 
game_still_going = True

#who won? Or tie?
winner = None

#whos turn is it?
current_player = "x"

def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

#play a game of tic tac toe
def play_game():
  
  #display initial board
  display_board()

  #while the game is still going
  while game_still_going:
 
   handle_turn(current_player)
   
   #handle a single turn of an abritary player 
   check_if_game_over()

   #flip to the other player
   flip_player()

# The game has ended
if winner == "x" or winner=="o":
  print(winner + "won.")
elif winner== None:
  print("Tie.")

#handle a single turn of an abritary player
def handle_turn(player):

  print(player + " 's turn. ")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input ("Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
     print("You caant go there. Go again.")

  board[position] = player
 
  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

  #setup gglobal variables 
  global winner

  #check rows
  row_winner = check_rows()
  #check compile
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()

  #get the winnner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return

def check_rows():
  #Set up global variables
  global game_still_going
  #check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #if any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
    #return the winner(X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
  global game_still_going
  #check if any of the rows have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  #if any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
    #return the winner(X or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return


def check_diagonals():
  global game_still_going
  #check if any of the rows have all the same value (and is not empty)
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[6] == board[4] == board[2] != "-"
  #if any row does have a match, flag that there is a win
  if diagonals_1 or diagonals_2:
    game_still_going = False
    #return the winner(X or O)
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[6]
  return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return

def flip_player():
  #global variables we NotImplementedError
  global current_player
  # if the current player was x, then change it to 0
  if current_player == "x":
    current_player= "o"
  elif current_player == "o":
    #if the current player was 0. then change it to x
    current_player = "x"
  return


play_game()


#board
#display board
#play game
#check win
#handle turn  
  #check rows
  #check columns
  #check diagonals
#check Tie
#flip players
