import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_hae_loytaa_olemassa_olevan_pelaajan(self):
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_hae_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        player = self.stats.search("Tuntematon Pelaaja")
        self.assertIsNone(player)

    def test_joukkue_palauttaa_oikean_joukkueen_pelaajat(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_parhaat_palauttaa_oikean_maaran_parhaita_pisteilla(self):
        top_players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")

    def test_parhaat_palauttaa_oikean_maaran_parhaita_maaleilla(self):
        top_players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")

    def test_parhaat_palauttaa_oikean_maaran_parhaita_syotoilla(self):
        top_players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Yzerman")

  

