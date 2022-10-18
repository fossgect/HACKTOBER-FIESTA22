from gameit.example import exampleGame
from gameit.aqeelshamz import treasureHunt
from gameit.MohdShibin import snakeGame


def main():
    games = {"example": exampleGame, "aqeelshamz": treasureHunt, "MohdShibin": snakeGame}
    while True:
        username = input("Enter github username:\n")
        try:
            games[username]()
            print("Happy Gaming")
        except:
            print("Username not found!!.")


if __name__ == "__main__":
    main()
