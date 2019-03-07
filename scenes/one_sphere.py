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
blue_material = Material(np.array([0,0,1]),0.4,0.5,0.7,1.,1.)


white_light = Spotlight(np.array([1,1,2]),np.array([1,1,1]))
blue_sphere = Sphere(np.array([0,0,3]), 1, blue_material)

this_scene.add_object(blue_sphere)
this_scene.add_light(white_light)

this_camera = Camera(1000,1000,1)

plt.imsave('blue sphere.png', raytracer_render(this_camera, this_scene))
