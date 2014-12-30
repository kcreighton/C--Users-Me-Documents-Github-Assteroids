from random import randint
from rigidBody import *
from assUtil import *
import assConstants

class Actor(RigidBody): # intelegent bodies # need AI owners
    def __init__(self, Sprite, spawn = assConstants.CENTER, velocity = [0, 0]):
        self.sprite = Sprite
        self.size = Sprite.get_size()
        self.center = [spawn[0], spawn[1]]
        self.lastCenter = self.center
        self.position = [spawn[0] - (self.size[0]/2), spawn[1] - (self.size[1]/2)]
        self.velocity = [velocity[0], velocity[1]]
        self.Items= []
        self.health = 100
        self.thrust = 0.25
        self.aim = [0, 0] # relative to screen (updated costantly)
        self.Gun = None
        self.trail = False
# called constantly # updates targeting for actor and their gun # called in main loop
    def adjustAim(self, target):
        self.aim = target
        if self.Gun != None:
            self.Gun.updateAim(target)

    def accelerate(self, direction, thrust = None):
        thrust = self.thrust
        self.velocity[0] += thrust * math.cos(direction)
        self.velocity[1] += thrust * math.sin(direction)

    def respawn(self, spawn = assConstants.CENTER, preserveVelocity = False):
        self.position = [spawn[0], spawn[1]]
        self.center = [spawn[0] + 16, spawn[1] + 16]
        if preserveVelocity == False:
            self.velocity = [0, 0]
            self.Gun.velocity = [0, 0]
            
    def hit(self):
        pass
