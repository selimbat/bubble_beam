
import numpy as np
import numpy.linalg as la
import sys
sys.path.append('..')
from rayon import *

class Camera:
    def __init__(self, image_nrows, image_ncols, focal_length ):    #constructeur de la classe Camera
        self.image_nrows = image_nrows
        self.image_ncols = image_ncols
        self.focal_length = focal_length
    def ray_at(self, row, col):
        starting_point = [0,0,0]
        x = (self.image_ncols - 2*col)/self.image_ncols             #lien entre la coordonnée x et le pixel en question
        y = (self.image_nrows - 2*row)/self.image_nrows        #lien entre la coordonnée y et le pixel en question
        z = self.focal_length                                       #lien entre la coordonnée z et le pixel en question
        direction = np.array([x,y,z])
        direction = direction/la.norm(direction)                    #normalisation
        return Ray(starting_point, direction)
    
