class Game:
    def __init__(self, game_name):
        self.game_name = game_name
    
    def add_game_to_json(self):
        # Add game to dictionary
        game_list["game"] = game_name
        # import do .json game_name ??
        # zatim mi to akorat prepisuje value v key "game", coz by se melo vyresit tim, ze to hned po "Add game" naimportuju do .json ?? Snad ??

    def add_game_time_to_json(self):
        # Add time for game (for example of using of try/excuse function)
        try:
            game_list["game_time"] = int(game_time)
            # .pop to json?? Aby se to odstranilo z dict po exportu
        except Exception as exc:
            print("Not a number! Error:", exc)
            del game_list["game"]
        # potom bude brat cas primo ze Steamu, ted pouze na procviceni a ukol
        # brani ve vstupu stringu do inputu game_time (se kterym se pocita, ze ma byt int)

    def view_stats():
        # Show data from game_list dictionary
        # pozdeji by to melo importovat .json file primo do funkce ?? Asi? Viz. "add_game(self)" pozn.
        print(game_list)


# ________________________________________________________________________

game_list = {}


# Makes menu for better work with app
while True:
    print("1. Add game")
    print("2. View stats")
    print("3. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        game_name = input("Add game:")
        game_time = input("Add time:")
        game = Game("game_name")
        time = Game("game_time")
        game.add_game_to_json()
        time.add_game_time_to_json()
    
    elif choice == "2":
        Game.view_stats()
    
    elif choice == "3":
        print("Exiting")
        break

    else:
        print("Your choice is not executable. Try again.")
