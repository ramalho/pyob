import geohash

class Coordinate:
    '''Coordinate on Earth'''

    reference_system = 'WGS84'

    def __init__(self, lat=0.0, long=0.0):
        self.lat = lat
        self.long = long
    
    def __repr__(self):
        return f'Coordinate({self.lat}, {self.long})'
    
    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'EW'[self.long < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.long):.1f}°{we}'

    def geohash(self):
        return geohash.encode(self.lat, self.long)