import numpy as np

class Sphere:
    def __init__(self,center,rayon,material):                                       #constructeur de la classe Sphere
        self.center = center
        self.rayon = rayon
        self.material = material

class Material:
    def __init__(self,color,ambiant,diffuse,specular,shininess,reflection):         #constructeur de la classe Material
        self.color = color
        self.ambiant = ambiant
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
        self.reflection = reflection
        
class Scene:
    def __init__(self):
        self.objects = []
        self.lights = []
    def add_object(o):
        self.objects.append(o)
    def add_light(l):
        self.lights.append(l)

