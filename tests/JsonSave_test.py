import unittest
import tempfile
import os
import json

from game_tracker.JsonSave import SaveManager

class TestSaveManager(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.filename = self.temp_file.name
        self.temp_file.close()
        self.manager = SaveManager(self.filename)

    def tearDown(self):
        os.remove(self.filename)

    def test_save_and_update_game_in_json(self):
        initial_data = [{"Game": "Mafia 1", "Playtime": 200}]
        self.manager.save(initial_data)

        updated_data = [{"Game": "Mafia 1", "Playtime": 1000}]
        self.manager.save(updated_data)

        with open(self.filename, "r") as f:
            result = json.load(f)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["Game"], "Mafia 1")
        self.assertEqual(result[0]["Playtime"], 1000)

    def test_add_multiple_and_nested_data_to_json(self):
        nested_data = [
            {"Game": "Fallout 4", "Playtime": 300},
            [{"Game": "Stalker", "Playtime": 500}]
        ]
        self.manager.save(nested_data)

        with open(self.filename, "r") as f:
            result = json.load(f)

        games = {g["Game"]: g["Playtime"] for g in result}

        self.assertEqual(len(games), 2)
        self.assertEqual(games["Fallout 4"], 300)
        self.assertEqual(games["Stalker"], 500)
