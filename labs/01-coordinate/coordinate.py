class Coordinate:
    '''Coordinate on Earth'''
    
    def __repr__(self):
        return f'Coordinate({self.lat}, {self.long})'
    
    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'EW'[self.long < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.long):.1f}°{we}'