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

this_scene = Scene()
some_material = Material(np.array([106.,102.,163.])/255,0.5,0.7,0.1,0.3,0.4)
red_material = Material(np.array([255.,151.,112.])/255,0.8,0.4,0.2,0.4,0.7)

light1 = Spotlight(np.array([1.,1.,0.]),np.array([252.,236.,201.])/255)
#red_light = Spotlight(np.array([-1,2,1]),np.array([1,1,0]))
#other_light = Spotlight(np.array([0,-1,1.5]),np.array([1,0,1]))
blue_sphere = Sphere(np.array([0.,0.,3.]), 0.8, some_material)
red_sphere = Sphere(np.array([0.4,0.4,1.8]), 0.1, red_material)

this_scene.add_object(blue_sphere)
this_scene.add_object(red_sphere)
this_scene.add_light(light1)
#this_scene.add_light(red_light)
#this_scene.add_light(other_light)

this_camera = Camera(1500,1500,2.2)

plt.imsave('shadow exemple.png', raytracer_render(this_camera, this_scene))
