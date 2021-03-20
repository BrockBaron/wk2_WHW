import unittest

from src.song import Song 


class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song('Wicked Games', 'Chris Isaak')
        self.song_2 = Song('Fire Starter', 'The Prodigy')
        
#1    
    def test_song_has_name(self):
        self.assertEqual("Wicked Games", self.song_1.song_name)
#2    
    def test_song_has_artist(self):
        self.assertEqual("The Prodigy", self.song_2.song_artist)
        