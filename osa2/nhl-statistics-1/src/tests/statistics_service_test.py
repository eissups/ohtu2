import unittest
from statistics_service import StatisticsService
from player_reader import PlayerReader
from player_reader_stub import PlayerReaderStub

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        
        
        self.stats = StatisticsService(PlayerReaderStub())
        
    def test_konstruktori_luo_StatisticsService(self):
        
        team_players = self.stats.team("PHI")  
        self.assertIsInstance(team_players, list) 
        print(team_players)

    def test_search_oikea_pelaaja(self):
        player = self.stats.search("Semenko")
        
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_search_tyhja_pelaaja(self):
        player2 = self.stats.search(" ")
        
        self.assertEqual(player2, None)

    def test_top_pelaajat(self):
        
        top_players = self.stats.top(2)
        
        expected_top_players = [
        {"name": "Gretzky", "team": "EDM", "goals": 35, "assists": 89},  
        {"name": "Lemieux", "team": "PIT", "goals": 45, "assists": 54}, 
        {"name": "Yzerman", "team": "DET", "goals": 42, "assists": 56}  
         ]

        for i, player in enumerate(top_players):
            self.assertEqual(player.name, expected_top_players[i]["name"])
            self.assertEqual(player.team, expected_top_players[i]["team"])
            self.assertEqual(player.goals, expected_top_players[i]["goals"])
            self.assertEqual(player.assists, expected_top_players[i]["assists"])
        


        


   
 
        


