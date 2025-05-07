import game_tracker.SteamAPI
import game_tracker.Game

game_list = []
# Makes menu for better work with app
while True:
    print("1. Add game")
    print("2. View stats")
    print("3. Exit")

    choice = input("Enter your choice:")

    if choice == "1":

        game_tracker.SteamAPI.get_gname()
        game = game_tracker.Game.Game()
        game.get_game_title()
        res = game.get_playtime()
        game_list.append(res)
    
    elif choice == "2":
        print(game_list)
    
    elif choice == "3":
        print("Exiting")
        break

    else:
        print("Your choice is not executable. Try again.")
