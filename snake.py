"""
This module implements the snake class.
"""

from gui import Gui
from position import Position
from typing import List
from apple import Apple

class Snake:
    """This is the Snake.

    It has a list of positions. The head is at index 0.
    The tail occupies the rest of the list.
    """

    def __init__(self,x,y):
        self.body = []
        self.head = Position(x,y)
        self.body.append(self.head)
        self.tail = Position(x-1,y)
        self.body.append(self.tail)
        self.tail2 = Position(x-2, y)
        self.body.append(self.tail2)
        self.direction = "right"


    def draw(self, gui):
        i = 0
        while i < len(self.body):
            if i == 0:
                if self.direction == "left":
                    gui.draw_text('<', self.body[0].get_x(), self.body[0].get_y(), "BLUE", "YELLOW")
                elif self.direction == "right":
                    gui.draw_text('>', self.body[0].get_x(), self.body[0].get_y(), "BLUE", "YELLOW")
                elif self.direction == "up":
                    gui.draw_text('^', self.body[0].get_x(), self.body[0].get_y(), "BLUE", "YELLOW")
                elif self.direction == "down":
                    gui.draw_text('v', self.body[0].get_x(), self.body[0].get_y(), "BLUE", "YELLOW")
            else:
                gui.draw_text('+', self.body[i].get_x(), self.body[i].get_y(), "BLUE", "YELLOW")
            i += 1

    def move(self):
        for i in range((len(self.body) -1), 0, -1):
            cpos = self.body[i]
            npos = self.body[i-1]
            self.body[i] = Position(npos.get_x(), npos.get_y())
        if self.direction == "right":
            self.body[0] = Position(self.body[0].get_x() + 1, self.body[0].get_y())
        elif self.direction == "left":
            self.body[0] = Position(self.body[0].get_x() - 1, self.body[0].get_y())
        elif self.direction == "up":
            self.body[0] = Position(self.body[0].get_x(), self.body[0].get_y() - 1)
        elif self.direction == "down":
            self.body[0] = Position(self.body[0].get_x(), self.body[0].get_y() + 1)
    def change_direction(self,c):
        if c == "KEY_UP":
            if self.direction == "down":
                pass
            else:
                self.direction = "up"
        elif c == "KEY_DOWN":
            if self.direction == "up":
                pass
            else:
                self.direction = "down"
        elif c == "KEY_LEFT":
            if self.direction == "right":
                pass
            else:
                self.direction = "left"
        elif c == "KEY_RIGHT":
            if self.direction == "left":
                pass
            else:
                self.direction = "right"
        else:
            ""


    def grow(self):
        self.body.append(self.tail2)

    def get_body(self):
        return self.body
