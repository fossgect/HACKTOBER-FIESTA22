from gameit.example import exampleGame
from gameit.example import exampleGame
from gameit.example import treasureHunt


def main():
    games = {"example": exampleGame, "aqeelshamz": treasureHunt}
    while True:
        username = input("Enter github username:\n")
        try:
            games[username]()
            print("Happy Gaming")
        except:
            print("Username not found!!.")


if __name__ == "__main__":
    main()
