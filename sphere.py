

class Sphere:
    def __init__(self,center,rayon,material):
        self.center = center
        self.rayon = rayon
        self.material = material

    def __str__(self):
        return 'Sphere at {} with color {}'.format(self.center,self.material.color)