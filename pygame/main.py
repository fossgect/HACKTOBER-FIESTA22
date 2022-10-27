from gameit.aqeelshamz import treasureHunt
from gameit.urmila import HuntingBirds
from gameit.aayahda import snakesGame
from gameit.MohdShibin import snakeGame
from gameit.AditiAjithkumar import SnakeGame
from gameit.sreni import Tic_Tac_Toe
from gameit.majid_2002 import jumpMan
from gameit.abhijithram import abhiGame
from gameit.kmSidharthM import Space_Invader
from gameit.anuragrajanp import feedTheSnake
from gameit.AnnMol_2002 import sudoku
from gameit.example import exampleGame
from gameit.ash394 import pongGame
from gameit.vishakh import car_game
from gameit.ebinjose02 import Snake
from gameit.jithinpkumar import ArmyBase
from gameit.Prometheus2k import Game2048
from gameit.ashitha_18 import SudokoGame
from gameit.mimithamg import halloween
from gameit.jithinpkumar import ArmyBase
from gameit.Prometheus2k import Game2048
from gameit.ashitha_18 import SudokoGame
from gameit.JP_GECT import sgame
from gameit.AadeshPS import game1
from gameit.ezbonpj import bounce
from gameit.taslimmuhammed import PlayerPro
from gameit.nived_krish44 import snake
from gameit.muhammed770 import mazeGame
from gameit.AnaghaJn21 import AppleShooting
from gameit.sammyrin import paambu


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
      "anuragrajanp":feedTheSnake,
      "AditiAjithkumar":SnakeGame,
      "urmila":HuntingBirds,
      'AnnMol_2002':sudoku,
      "Ash-394": pongGame,
      "vishakh": car_game,
      "ebinjose02":Snake,
      "jithinpkumar":ArmyBase,
      "mimithamg":halloween,
      "jithinpkumar":ArmyBase,
      "Prometheus2k":Game2048,
      "ashitha-18":SudokoGame,
      "JP_GECT":sgame,
      "taslimmuhammed":PlayerPro,
      "AadeshPS":game1,
      "ezbonpj":bounce,
      "nived_krish44":snake,
      "AnaghaJn21":AppleShooting,
      "sammyrin":paambu,
      "muhammed":mazeGame,
    }


    while True:
        username = input("Enter github username:\n")
        try:
            games[username]()
            print("Happy Gaming")
        except KeyError:
            print("Username not found!!.")


if __name__ == "__main__":
  main()
