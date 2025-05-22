class Game:

    def __init__(self) -> None:
        self.game_dict = {}

    def add_game_title(self) -> None:
        x = input("You can choose or add new game:")
        self.game_dict["Game"] = x

    def add_playtime(self) -> dict:
        while True:
            y = input("Add time (in hours):")
            try:
                self.game_dict["Playtime"] = int(y)
                break
            except ValueError:
                print("Please enter a number.")

        return self.game_dict
