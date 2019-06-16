

class Sphere(object):

    def __init__(self, radius = 1.0, x = 0.0, y = 0.0, z = 0.0):
        self.radius = float(radius)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def get_volume(self):
        v = 4 / 3 * 3.1415926535897932384626433 * self.radius ** 3
        return v

    def get_square(self):
        s = 4 * 3.1415926535897932384626433 * (self.radius ** 2)
        return s

    def get_radius(self):
            return self.radius

    def get_center(self):
        return (self.x, self.y, self.z,)

    def set_radius(self, r):
        self.r = float(r)
        self.radius = r

    def set_center(self, x_new, y_new, z_new):
        self.x = float(x_new)
        self.y = float(y_new)
        self.z = float(z_new)

    def is_point_inside(self, x_1, y_1, z_1):
        self.x_1 = x_1
        self.y_1 = y_1
        self.z_1 = z_1
        rn = ((self.x_1 - self.x) ** 2 + (self.y_1 - self.y) ** 2 + (self.z_1 - self.z) ** 2) ** 0.5
        if  rn > self.radius:
            return False
        else:
            return True






s1 = Sphere()
print(s1.radius, s1.x, s1.y, s1.z)
print('V1 =', s1.get_volume())
print('S1 =', s1.get_square())
print('R =', s1.get_radius())
print('coordinates = ', s1.get_center())
s1.set_radius(5)
print('R= %s' % (s1.get_radius()))
s1.set_center(1025, 1026, 1027)
print('coordinates=', s1.get_center())
print(s1.is_point_inside(1000, 1000, 1000), '\n')

s0 = Sphere(0.5) # test sphere creation with radius and default center
print(s0.get_center()) # (0.0, 0.0, 0.0)
print(s0.get_volume()) # 0.523598775598
print(s0.is_point_inside(0, -1.5, 0)) # False
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0)) # True
print(s0.get_radius()) # 1.6