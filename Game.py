class Game:
    def __init__(self, game_name):
        self.game_name = game_name

    def add_game_to_json(self):
        # Add game to dictionary
        game_list["game"] = game_name
        # import do .json game_name ??
        # zatim mi to akorat prepisuje value v key "game", coz by se melo vyresit tim, ze to hned po "Add game" naimportuju do .json ?? Snad ??

    def view_stats():
        # Show data from game_list dictionary
        # pozdeji by to melo importovat .json file primo do funkce ?? Asi? Viz. "add_game(self)" pozn.
        print(game_list)


# _______________________________________________________________________________________ #
        # def add_game_time_to_json(self):
        #     # Adds time for game (for example of using of try/excuse function)
        #
        #     try:
        #         game_list["game_time"] = int(game_time)
        #         # .pop to json?? Aby se to odstranilo z dict po exportu
        #     except Exception as exc:
        #         print("Not a number! Error:", exc)
        #         del game_list["game"]
        #         del game_list["game_time"]