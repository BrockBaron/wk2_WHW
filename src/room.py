from src import guest


class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capcity = capacity
        self.guests = []
        self.songs = []
    
    def guest_is_old_enough(self, guest):
        return guest.age >= 18
    
    def add_song(self, song):
        self.songs.append(self.songs)
    
    def song_count(self):
        return len(self.songs)
    
    def add_guest(self, guest):
        if not self.guest_is_old_enough(guest):
            return False
        return self.guests.append(self.guests)
    
    def guest_count(self):
        return len(self.guests)
    
    def remove_guest(self, guest):
        while guest in self.guests: self.guests.remove(guest)
    
    def remove_song(self, songs):
        while songs in self.songs: self.songs.remove(songs)