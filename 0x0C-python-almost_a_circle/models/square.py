#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        self.__id = super(Rectangle).__init__(Rectangle.__id)
