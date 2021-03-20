import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
#rooms
        self.room_1 = Room(1, 4)
        self.room_2 = Room(2, 4)
        self.room_3 = Room(3, 2)
        
#guests        
        self.guest_1 = Guest('Rick Sanchez', 70, 9999)
        self.guest_2 = Guest('Morty Smith', 14, 0)
        self.guest_3 = Guest('Gintoki Sakata', 29, 20)
        self.guest_4 = Guest('Briareos Hecaton', 42, 800)
        self.guest_5 = Guest('Deunan Knute', 33, 500)
        self.guest_6 = Guest('Cheryl Tunt', 27, 20)
        self.guest_7 = Guest('Lana Kane', 32, 300)
        self.guest_8 = Guest('Sterling Archer', 36, 850)
        #unwanted guest
        self.guest_9 = Guest('Jerry Smith', 40, 20)

#songs
        self.song_1 = Song('Wicked Games', 'Chris Isaak')
        self.song_2 = Song('Fire Starter', 'The Prodigy')
        self.song_3 = Song('Big Poppa', 'The Notorious B.I.G')
        self.song_4 = Song('Still D.R.E', 'Dr. Dre ft. Snoop Dogg')

#6
    def test_guest_is_old_enough__returns_true(self):
        self.assertEqual(True, self.room_1.guest_is_old_enough(self.guest_1))
#7
    def test_customer_is_old_enough__returns_false(self):
        self.assertEqual(False, self.room_1.guest_is_old_enough(self.guest_2))   
#8
    def test_add_song_to_room(self):
            self.room_1.add_song(self.song_1)
            self.room_1.add_song(self.song_3)
            self.assertEqual(2, self.room_1.song_count())
#9   
    def test_checks_guests_in(self):
            self.room_1.add_guest(self.guest_1)
            self.room_1.add_guest(self.guest_2)
            self.room_1.add_guest(self.guest_3)
            self.assertEqual(2, self.room_1.guest_count())
#10   
    #@unittest.skip("delete this line to run the test")
    def test_checks_guests_out(self):
            self.room_1.remove_guest(self.guest_1)
            self.assertEqual(0, self.room_1.guest_count())
    
#11
    #unittest.skip("delete this line to run the test")
    def test_remove_song_from_room(self):
            self.room_1.remove_song(self.song_1)
            self.assertEqual(0, self.room_1.song_count())
            
            

#@unittest.skip("delete this line to run the test")
