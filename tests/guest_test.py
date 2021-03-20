import unittest

from src.guest import Guest


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        
        self.guest = Guest('Kaneda Shotaro', 21, 100)
#3    
    def test_guest_has_name(self):
        self.assertEqual("Kaneda Shotaro", self.guest.guest_name)
#4        
    def test_guest_has_age(self):
        self.assertEqual(21, self.guest.age)
#5        
    def test_guest_has_money(self):
        self.assertEqual(100, self.guest.money)
    
