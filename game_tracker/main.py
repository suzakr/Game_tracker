import game_tracker.SteamAPI
import game_tracker.Game
import game_tracker.JsonSave

game_list = []

while True:
    print("1. Add game")
    print("2. View stats")
    print("3. Save list")
    print("4. Remove all games from file")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        game_info = game_tracker.SteamAPI.get_game_info()

        game_tracker.SteamAPI.get_game_name()
        game = game_tracker.Game.Game()
        game.add_game_title()
        entered_game = game.game_dict["Game"]

        match = None
        for i in game_info:
            if i["Game"] == entered_game:
                match = i
                break

        if match:
            print("Playtime added automatically.")
            game.game_dict["Playtime"] = match["Playtime"]

        else:
            game.add_playtime()

        game_list.append(game.game_dict)


    elif choice == "2":
        print(game_list)

    elif choice == "3":
        save_manager = game_tracker.JsonSave.SaveManager("games.json")
        save_manager.save(game_list)
        game_list.clear()

    elif choice == "4":
        game_tracker.JsonSave.remove_json_content()

    elif choice == "5":
        print("Exiting")
        break

    else:
        print("Your choice is not executable. Try again.")
