from gameit.example import exampleGame
from gameit.sreni import Tic_Tac_Toe


def main():
    games = {"example": exampleGame, "sreni":Tic_Tac_Toe }
    while True:
        username = input("Enter github username:\n")
        try:
            games[username]()
            print("Happy Gaming")
        except:
            print("Username not found!!.")


if __name__ == "__main__":
    main()