from intersection import intersect
import numpy as np
from numpy import linalg as la
from light import phong_illuminate, ambiant_illuminate
from math import inf,log

class Ray :
    def __init__(self, starting_point, direction):
        self.starting_point = starting_point
        self.direction = direction


def trace_ray(ray, scene, on_reflection_object=None, n_reflections=0):
    n_reflections += 1
    if n_reflections == 6:
        return np.array([0.,0.,0.])
    intersections = []
    #Find the object to print on the image
    other_objects = [o for o in scene.objects if o != on_reflection_object]
    for obj in other_objects:
        intersection = intersect(obj,ray)
        if intersection != None:
            intersections.append(intersection)

    if len(intersections) > 0:
        min_dist = inf
        for inter in intersections:
            dist_from_inter = la.norm(ray.starting_point - inter.position)
            if dist_from_inter < min_dist:
                closest_instersection = inter
                min_dist = dist_from_inter

        result_color = ambiant_illuminate(closest_instersection.obj) if len(scene.lights) > 0 else np.array([0.,0.,0.])
        for light in scene.lights:
            result_color += compute_light(light, scene, closest_instersection, ray.starting_point)
        
        R = ray.direction
        N = closest_instersection.normal
        reflection_ray = Ray(closest_instersection.position, R - 2*R.dot(N)*N)
        reflection_factor = closest_instersection.obj.material.reflection
        result_color = result_color*(1 - reflection_factor) + reflection_factor*trace_ray(reflection_ray, scene, on_reflection_object=closest_instersection.obj, n_reflections=n_reflections)
        return result_color
    else:
        return np.array([0.,0.,0.])



def compute_light(light, scene, intersection, viewer):
    to_light = light.position - intersection.position
    occlusion = None
    other_objects = [o for o in scene.objects if o != intersection.obj]
    for obj in other_objects:
        occlusion = intersect(obj, Ray(intersection.position, to_light))
        if occlusion != None:
            dist_to_occl = la.norm(occlusion.position - intersection.position)
            if dist_to_occl < la.norm(to_light) and to_light.dot(occlusion.position - intersection.position) > 0 :
                return np.array([0.,0.,0.])
    return phong_illuminate(light, intersection.position, intersection.normal, intersection.obj, viewer)


def raytracer_render(camera, scene):
    image = np.zeros((camera.image_nrows,camera.image_ncols,3))
    for row in range(camera.image_nrows):
        for col in range(camera.image_ncols):
            image[row,col,:] = trace_ray(camera.ray_at(row,col), scene)
    log_normalizer = np.vectorize(lambda x: log(1+x))
    image_log = log_normalizer(image)
    image_log = image_log / np.amax(image_log)
    return image_log
