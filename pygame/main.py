from gameit.example import exampleGame
from gameit.aqeelshamz import treasureHunt
from gameit.aayahda import snakesGame
from gameit.MohdShibin import snakeGame
from gameit.sreni import Tic_Tac_Toe
from gameit.majid_2002 import jumpMan
from gameit.abhijithram import abhiGame
from gameit.kmSidharthM import Space_Invader
from gameit.Divyasree import Invader

def main():
    games = {
      "aayahda": snakesGame,
      "example": exampleGame, 
      "aqeelshamz": treasureHunt, 
      "MohdShibin": snakeGame,
      "majid-2002":jumpMan,
      "sreni":Tic_Tac_Toe, 
      "abhijithram":abhiGame,
      "kmSidharthM":Space_Invader,
      "Divyasree":Invader
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
