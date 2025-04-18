from Game import Game

game_list = {}

# Makes menu for better work with app
while True:
    print("1. Add game")
    print("2. View stats")
    print("3. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        game_name = input("Add game:")
        # game_time = input("Add time:")
        game = Game("game_name")
        # time = Game("game_time")
        game.add_game_to_json()
        # time.add_game_time_to_json()
    
    elif choice == "2":
        Game.view_stats()
    
    elif choice == "3":
        print("Exiting")
        break

    else:
        print("Your choice is not executable. Try again.")
