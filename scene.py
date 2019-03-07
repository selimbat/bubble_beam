
        
class Scene:
    def __init__(self):
        self.objects = []
        self.lights = []

    def add_object(self,o):
        self.objects.append(o)
        
    def add_light(self,l):
        self.lights.append(l)

