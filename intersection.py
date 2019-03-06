import numpy as np
from numpy import linalg as la
from scene import *


        
class Intersection:
    def __init__(self,position,normal,objet):              #constructeur de la classe intersection
        self.position = position
        self.normal = normal
        self.objet = objet

def intersect(objet,ray):
    if type(objet) is Sphere:
        r = objet.rayon
        c = objet.center
        o = ray.starting_point
        u = ray.direction / la.norm(ray.direction)
        delta = u.dot(o-c)**2 - ( la.norm(o-c)**2 - r**2 )                #discriminant de l'equation du second degré
        if delta < 0 :
            return None                                                             #cas où il n'y a pas d'intersection
        elif delta == 0 :                                                              #unique point d'intersection
            d = (-1)*u.dot(o-c)          #distance parcourue sur l'axe du rayon pour atteindre le point d'intersection
            if d < 0 :
                return None                                                                 #intersection avant le starting point (non valable)
            else :
                return Intersection(o+d*u,(o+d*u-c)/la.norm(o+d*u-c),objet)                #intersection après le starting point (valable)
        else :
            d = (-1)*u.dot(o-c) - np.sqrt(delta)         #distance parcourue sur l'axe du rayon (première solution)
            if d >= 0 :
                if la.norm(o-c) < r :
                    return Intersection(o+d*u,(c-o-d*u)/la.norm(o+d*u-c),objet)            #normale pointant vers l'intérieur
                else:
                    return Intersection(o+d*u,(o+d*u-c)/la.norm(o+d*u-c),objet)            #normale pointant vers l'extérieur
            else :
                d += 2*np.sqrt(delta)                   #deuxieme solution de l'équation du deuxième degré
                if d >= 0 :
                    if la.norm(o-c) < r:
                        return Intersection(o+d*u,(c-o-d*u)/la.norm(o+d*u-c),objet)        #normale pointant vers l'intérieur
                    else:
                        return Intersection(o+d*u,(o+d*u-c)/la.norm(o+d*u-c),objet)        #normale pointant vers l'extérieur
                else :
                    return None
    