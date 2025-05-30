import json


def remove_json_content():
    with open("games.json", "w") as f:
        json.dump([], f)


class SaveManager:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def load(self) -> list:
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return self.normalize_data(data)

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def normalize_data(self, data: list) -> list:
        # "Flatten" - převést seznam vnořených seznamů na jednoduchý seznam slovníků
        flattened = []
        for item in data:
            if isinstance(item, list):
                flattened.extend(self.normalize_data(item))  # Rekurzivně rozbal vnořené seznamy
            elif isinstance(item, dict):
                flattened.append(item)
        return flattened

    def save(self, new_games: list[dict]) -> None:
        new_games = self.normalize_data(new_games)
        saved_games = self.normalize_data(self.load())

        for new_game in new_games:
            found = False
            for saved_game in saved_games:
                if saved_game["Game"] == new_game["Game"]:
                    saved_game["Playtime"] = new_game["Playtime"]
                    found = True
                    break
            if not found:
                saved_games.append(new_game)

        with open(self.filename, "w") as f:
            json.dump(saved_games, f, indent=4)
