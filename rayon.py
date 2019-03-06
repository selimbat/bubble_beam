
import numpy as np
import numpy.linalg as la

class Ray :
    def __init__(self, starting_point, direction):           #constructeur de la classe Ray
        self.starting_point = starting_point
        self.direction = direction