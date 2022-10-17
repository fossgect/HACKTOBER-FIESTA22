from gameit.example import exampleGame

def main():
    games = {
        'example':exampleGame
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