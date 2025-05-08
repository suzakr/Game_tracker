# import game_tracker.SteamAPI
import unittest
from game_tracker.Game import Game
from unittest.mock import patch

class TestGame(unittest.TestCase):

    @patch("builtins.input", return_value="Ready or Not")
    def test_get_game_title(self, mock_input):
        game = Game()
        game.get_game_title()
        self.assertEqual(game.game_dict["Game"], "Ready or Not")

    @patch("builtins.input", side_effect=["blabla", 42])
    @patch("builtins.print")
    def test_get_playtime_correct_and_incorrect_input(self, mock_print, mock_input):
        game = Game()
        res = game.get_playtime()
        self.assertEqual(res["Playtime"], 42)
        mock_print.assert_any_call("Please enter a number.")

    @patch("builtins.input", side_effect=["Helldivers 2", 350])
    def test_full_input(self, mock_input):
        game = Game()
        game.get_game_title()
        game.get_playtime()
        self.assertEqual(game.game_dict, {"Game": "Helldivers 2", "Playtime": 350})





