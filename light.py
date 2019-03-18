import numpy as np
from numpy import linalg as la

class Spotlight :
    def __init__(self,position,color):
        self.position = position
        self.color = color
        
def phong_illuminate(light, position, normal, object, viewer):
    L = light.position - position       #surface to light vector
    L = (1/la.norm(L))*L
    N = (1/la.norm(normal))*normal
    R = 2*L.dot(N)*N - L                #reflection vector
    R = (1/la.norm(R))*R
    V = viewer - position               #surface to viewer vector
    V = (1/la.norm(V))*V
    if L.dot(N) > 0 and V.dot(N) > 0 :
        ks = object.material.specular
        kd = object.material.diffuse
        shi = object.material.shininess
        I = kd*L.dot(N)                 #calcul de l'intensité à partir du modèle de Phong, ajout de la composante diffuse
        if R.dot(V) > 0:
            I += ks*(R.dot(V))**shi     #ajout de la composante specular
        return I*object.material.color*light.color
    else:                                       #si la lumière ou l'observateur est derrière la surface en question
        return np.array([0.,0.,0.])                #couleur noire
    
def ambiant_illuminate(object):
    return object.material.ambiant*object.material.color
    