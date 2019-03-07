from intersection import intersect
import numpy as np
from numpy import linalg as la
from light import phong_illuminate, ambiant_illuminate
from math import inf

class Ray :
    def __init__(self, starting_point, direction):
        self.starting_point = starting_point
        self.direction = direction


def trace_ray(ray, scene):
    intersections = []
    for obj in scene.objects:
        intersection = intersect(obj,ray)
        if intersection != None:
            intersections.append(intersect(obj,ray))
    if len(intersections) > 0:
        min_dist = inf
        for inter in intersections:
            dist_from_inter = la.norm(ray.starting_point - inter.position)
            if dist_from_inter < min_dist:
                closest_instersection = inter
                min_dist = dist_from_inter
    else:
        return np.array([0,0,0])

    result_color = ambiant_illuminate(closest_instersection.obj) if len(scene.lights) > 0 else np.array([0,0,0])
    for light in scene.lights:
        result_color += phong_illuminate(light, closest_instersection.position, closest_instersection.normal, closest_instersection.obj, ray.starting_point)
    result_color = np.array([min(rgb,1) for rgb in list(result_color)])
    return result_color

def raytracer_render(camera, scene):
    image = np.zeros((camera.image_nrows,camera.image_ncols,3))
    for row in range(camera.image_nrows):
        for col in range(camera.image_ncols):
            image[row,col,:] = trace_ray(camera.ray_at(row,col), scene)
    return image