from gameit.example import exampleGame
from gameit.aqeelshamz import treasureHunt
from gameit.urmila import HuntingBirds


def main():
    games = {"example": exampleGame, "aqeelshamz": treasureHunt, "urmila": HuntingBirds}
    while True:
        username = input("Enter github username:\n")
        try:
            games[username]()
            print("Happy Gaming")
        except:
            print("Username not found!!.")


if __name__ == "__main__":
    main()
