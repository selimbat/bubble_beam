import sys
sys.path.append('..')
from scene import Scene
from sphere import Sphere
from material import Material
from light import Spotlight
from rayon import raytracer_render
from camera import Camera
import numpy as np
import matplotlib.pyplot as plt
from random import random

this_scene = Scene()
material1 = Material(np.array([random(),random(),random()]),0.8,0.7,0.8,0.85,0.75)
material2 = Material(np.array([random(),random(),random()]),0.8,0.6,1.,0.7,0.5)
material3 = Material(np.array([random(),random(),random()]),0.9,0.9,1.,0.5,0.1)
material4 = Material(np.array([1,1,1]),1.,1.,1.,0.6,1.)

sphere1 = Sphere(np.array([0.,1.,3.]), 0.8, material1)
sphere2 = Sphere(np.array([0.87,-0.5,3.]), 0.8, material2)
sphere3 = Sphere(np.array([-0.87,-0.5,3.]), 0.8, material3)
small_sphere1 = Sphere(np.array([0.,-1.3,3.]), 0.3, material4)
small_sphere2 = Sphere(np.array([1.131,0.65,3.]), 0.3, material4)
small_sphere3 = Sphere(np.array([-1.131,0.65,3.]), 0.3, material4)

white_light = Spotlight(np.array([3.,0.,1.5]),np.array([1.,1.,1.]))
light1 = Spotlight(np.array([-2.,-0.6,1.4]), np.array([random(),random(),random()]))
light2 = Spotlight(np.array([-0.6,2.,1.4]),np.array([random(),random(),random()]))
light3 = Spotlight(np.array([0.6,-2.,1.4]),np.array([random(),random(),random()]))
light4 = Spotlight(np.array([2.,0.6,1.4]), np.array([random(),random(),random()]))
#white_light2 = Spotlight(np.array([0.,1.5,0.3]),np.array([1.,1.,1.]))
#white_light3 = Spotlight(np.array([-1.,0.5,0.]),np.array([1.,1.,1.]))
#red_light = Spotlight(np.array([0.,-1.5,1.]), np.array([1.,0.,0.]))
#green_light = Spotlight(np.array([-1.74,0.75,1.]), np.array([0.,1.,0.]))
#blue_light = Spotlight(np.array([1.74,0.75,1.]), np.array([0.,0.,1.]))


this_scene.add_object(sphere1)
this_scene.add_object(sphere2)
this_scene.add_object(sphere3)
this_scene.add_object(small_sphere1)
this_scene.add_object(small_sphere2)
this_scene.add_object(small_sphere3)

this_scene.add_light(white_light)
this_scene.add_light(light1)
this_scene.add_light(light2)
this_scene.add_light(light3)
this_scene.add_light(light4)
#this_scene.add_light(white_light2)
#this_scene.add_light(white_light3)
#this_scene.add_light(red_light)
#this_scene.add_light(green_light)
#this_scene.add_light(blue_light)

this_camera = Camera(2000,2000,1.35)

plt.imsave('random8.png', raytracer_render(this_camera, this_scene))
print('colors of spheres :\n{}\n{}\n{}'.format(sphere1.material.color,sphere2.material.color,sphere3.material.color))
print('colors of lights :\n{}\n{}\n{}\n{}'.format(light1.color,light2.color,light3.color,light4.color))
