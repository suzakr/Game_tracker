class Game:

    def __init__(self) -> None:
        self.game_dict = {}

    def get_game_title(self) -> None:
        x = input("You can choose or add new game:")
        self.game_dict["Game"] = x

    def get_playtime(self) -> dict:
        while True:
            y = input("Add time (in hours):")
            try:
                self.game_dict["Playtime"] = int(y)
                break
            except ValueError:
                print("Please enter a number.")

        return self.game_dict



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