from gameit.aqeelshamz import treasureHunt
from gameit.urmila import HuntingBirds
from gameit.aayahda import snakesGame
from gameit.MohdShibin import snakeGame
from gameit.AditiAjithkumar import SnakeGame
from gameit.sreni import Tic_Tac_Toe
from gameit.majid_2002 import jumpMan
from gameit.abhijithram import abhiGame
from gameit.msmuhsin import upAndDown
from gameit.kmSidharthM import Space_Invader
from gameit.anuragrajanp import feedTheSnake
from gameit.AkashKMathew import crash
from gameit.AnnMol_2002 import sudoku
from gameit.example import exampleGame
from gameit.ash394 import pongGame
from gameit.vishakh import car_game
from gameit.ebinjose02 import Snake
from gameit.Prometheus2k import Game2048
from gameit.ashitha_18 import SudokoGame
from gameit.azmisal import playAzmi
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
from gameit.ridin2002 import webshooters
from gameit.taslimmuhammed import PlayerPro
from gameit.nived_krish44 import snake
from gameit.Devadathan_KS import GameLoop
from gameit.Rishajahan import shooter
from gameit.sinana import snake
from gameit.muhammed770 import mazeGame
from gameit.AnaghaJn21 import AppleShooting
from gameit.Haze import Tet
from gameit.zAiN import hallo
from gameit.sammyrin import paambu
from gameit.ARJ18 import Squareventures
from gameit.nikhilputhumana import numberGuessingGame
from gameit.BhargavM import bmsnake
#pifrom gameit.AnjanaPR import Spooky_Halloween
from gameit.ritha import game2

def main():
    games = {
      "msmuhsin": upAndDown,
      "aayahda": snakesGame,
      "example": exampleGame, 
      "aqeelshamz": treasureHunt, 
      "MohdShibin": snakeGame,
      "majid-2002":jumpMan,
      "sreni":Tic_Tac_Toe, 
      "abhijithram":abhiGame,
      "kmSidharthM":Space_Invader,
      "anuragrajanp":feedTheSnake,
      "AkashKMathew": crash,
      "AditiAjithkumar":SnakeGame,
      "urmila":HuntingBirds,
      'AnnMol_2002':sudoku,
      "Ash-394": pongGame,
      "vishakh": car_game,
      "ebinjose02":Snake,
      "Prometheus2k":Game2048,
      "ashitha-18":SudokoGame,
      "azmisal":playAzmi,
      "jithinpkumar":ArmyBase,
      "mimithamg":halloween,
      "jithinpkumar":ArmyBase,
      "Prometheus2k":Game2048,
      "ashitha-18":SudokoGame,
      "JP_GECT":sgame,
      "taslimmuhammed":PlayerPro,
      "AadeshPS":game1,
      "ezbonpj":bounce,
      "ridin2002":webshooters,
      "nived_krish44":snake,
      "Haze":Tet,
      "AnaghaJn21":AppleShooting,
      "Rishajahan":shooter,
      "sinana":snake,
      "AnaghaJn21":AppleShooting,
      "zAiN" :hallo,
      "sammyrin":paambu,
      "muhammed":mazeGame,
      "Devadathan-KS":GameLoop,
      "ARJ18":Squareventures,
      "nikhilputhumana": numberGuessingGame,
      "BhargavM":bmsnake,
      #"AnjanaPR":Spooky_Halloween,
      "ritha":game2
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