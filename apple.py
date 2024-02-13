"""
This module represents the apple that appears at random places on the screen.
"""
import random
from typing import List

from gui import Gui
from position import Position

def collides(p, positions):
    """Return true if p is any of the positions in the list."""
    for position in positions:
        if p.get_x() == position.get_x() and p.get_y() == position.get_y():
            return True
    return False

def get_random(gui, snake):
    while True:
        apple_position = Position(random.randrange(1, gui.get_width()-1,1), random.randrange(1, gui.get_height()-1,1))
        if not collides(apple_position,snake): # if the snake is not collliding it is not in the apple position
            return apple_position

class Apple:
    """The apple's location is randomly generated."""
    def __init__(self,snake,gui):
        self.apple = get_random(gui,snake)

    def draw(self, gui):
        gui.draw_text('*', self.apple.get_x(), self.apple.get_y(), "GREEN", "RED")

    def get_apple(self):
        return self.apple
