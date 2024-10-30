import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Wayne Gretzky", "EDM", 40, 50)

    def test_player_initialization(self):
        self.assertEqual(self.player.name, "Wayne Gretzky")
        self.assertEqual(self.player.team, "EDM")
        self.assertEqual(self.player.goals, 40)
        self.assertEqual(self.player.assists, 50)

    def test_points_property_calculates_correctly(self):
        self.assertEqual(self.player.points, 90)

    def test_str_representation(self):
        expected_str = "Wayne Gretzky EDM 40 + 50 = 90"
        self.assertEqual(str(self.player), expected_str)