from gameit.example import exampleGame
from gameit.aqeelshamz import treasureHunt
from gameit.MohdShibin import snakeGame
from gameit.sreni import Tic_Tac_Toe
from gameit.majid_2002 import jumpMan

def main():
    games = {
      "example": exampleGame, 
      "aqeelshamz": treasureHunt, 
      "MohdShibin": snakeGame,
      "sreni":Tic_Tac_Toe,
      "majid-2002":jumpMan
    }

    while True:
        username = input("Enter github username:\n")
        try:
            games[username]()
            print("Happy Gaming")
        except:
            print("Username not found!!.")


if __name__ == "__main__":
  main()
