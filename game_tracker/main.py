

game_list = []
# Makes menu for better work with app
while True:
    print("1. Add game")
    print("2. View stats")
    print("3. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        ...
        # SteamAPI.get_gname()
        # game = Game()
        # game.get_game_title()
        # res = game.get_playtime()
        # game_list.append(res)
    
    elif choice == "2":
        print(game_list)
    
    elif choice == "3":
        print("Exiting")
        break

    else:
        print("Your choice is not executable. Try again.")
