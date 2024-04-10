def game_menu():
  print("Welcome to the Game Selection Menu!")
  print("1. Rock, Paper, Scissors")
  print("2. Number Guessing Game")

def main():
  game_menu()
  choice = input("Enter the number of the game you want to play: ")

  if choice == '1':
      print("You selected Rock, Paper, Scissors!")
      # Call function to start Rock, Paper, Scissors game
  elif choice == '2':
      print("You selected the Number Guessing Game!")
      # Call function to start Number Guessing Game?
  #Add hangman game
  # Call function to start Hangman game
  else:
      print("That is an invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
  main()
