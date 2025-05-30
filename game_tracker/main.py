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
        # Vytvori prehledne menu

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
            # Vypise seznam her ze Steam API
            # Prida nazev hry pomoci input
            # Prida odehrany cas pomoci input. Pokud se hra nachazi v Steam API seznamu, zapise cas automaticky z API
            # Vytvori seznam adresaru s klici "Game" a "Playtime" (podle poctu zvlast zadanych vstupu)

    elif choice == "2":
        print(game_list)
            # Vypise seznam adresaru nami zadanych her

    elif choice == "3":
        save_manager = game_tracker.JsonSave.SaveManager("games.json")
        save_manager.save(game_list)
        game_list.clear()
            # Ulozi seznam do souboru "games.json", pripadne prepise jiz existujici data

    elif choice == "4":
        game_tracker.JsonSave.remove_json_content()
            # Vymaze obsah souboru "games.json", abychom so mohli postup vynulovat

    elif choice == "5":
        print("Exiting")
        break
            # Ukonci program
    else:
        print("Your choice is not executable. Try again.")
            # Po zadani jineho vstupu nez vyse uvedenych, vyhodi program chybu a zazada o novy vstup
