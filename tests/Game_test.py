import game_tracker.SteamAPI
from game_tracker.Game import Game
import pytest
from unittest.mock import patch

@patch.object(Game, "get_game_title", return_value="Mafia 1")
def test_get_game_title(self):
    game = Game()
    game.get_game_title()
    self.assertEqual(game.game_dict["Game"], "Mafia 1")



