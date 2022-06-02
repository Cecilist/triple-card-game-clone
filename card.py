from asyncio.windows_events import NULL


class Card:
    def __init__(self, name, north, south, east, west, player):
        self.name   = name
        self.north  = north
        self.south  = south
        self.east   = east
        self.west   = west
        self.player = player
        self.pos = -1
        
    
    def __str__(self):
        return self.name + " Controlled by:" + self.player + ".\n Values are N:"+ str(self.north)+ " S:" + str(self.south) +\
             " E:"+ str(self.south)+ " W:"+ str(self.west) + " Position:" + str(self.pos)

    def setPos(self, newPos):
        self.pos = newPos

