# Yifeng Ding
# 2014-10-06
#
# Rotates the point clockwise by a specified 
#   number of radians about another optional 
#   point, defaulting to the origin.

import numpy as np

class Point(object):
    """docstring for Point"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, p=None):
        if p is None:
            p = Point(0.0, 0.0)
        
        return np.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )

    def rotate(self,rad,p=None):
        if p is None:
            p = Point(0.0, 0.0)

        rot = np.array([[np.cos(rad),np.sin(rad)],[-np.sin(rad),np.cos(rad)]])
        x,y=np.dot(rot,[self.x-p.x,self.y-p.y])
        self.x=x+p.x
        self.y=y+p.y
        return self

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)
    
    def __repr__(self):
        return 'Point(%f, %f)' % (self.x, self.y)
    