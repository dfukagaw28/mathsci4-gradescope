import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def volume(self):
        return self.radius ** 2 * math.pi * self.height

if __name__ == '__main__':
    testcases = [
        (3, 3),
        (10, 5),
    ]
    for testcase in testcases:
        a = Cylinder(*testcase)
        print(a.radius, a.height)
        print(a.volume())
