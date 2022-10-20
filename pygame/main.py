from gameit.example import exampleGame
from gameit.aqeelshamz import treasureHunt
from gameit.aayahda import snakesGame
from gameit.MohdShibin import snakeGame
from gameit.sreni import Tic_Tac_Toe
from gameit.abhijithram import abhiGame

def main():
    games = {
      "aayahda": snakesGame,
      "example": exampleGame, 
      "aqeelshamz": treasureHunt, 
      "MohdShibin": snakeGame,
      "sreni":Tic_Tac_Toe, 
      "abhijithram":abhiGame,
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
