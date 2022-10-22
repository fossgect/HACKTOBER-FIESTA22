from gameit.example import exampleGame
from gameit.AnnMol_2002 import sudoku

def main():
    games = {
        'example':exampleGame,
        'AnnMol-2002':sudoku
    }
    while True:
        username = input("Enter github username:\n")
        try:
            games[username]()
            print("Happy Gaming")
        except:
            print("Username not found!!.")

if __name__ == '__main__':
    main()