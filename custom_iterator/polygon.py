import math


class Polygon:
    def __init__(self, vertices_number, circumradius):
        if vertices_number < 3:
            raise ValueError('Polygon must have at least three sides/vertices.')
        
        self._vertices_number = vertices_number
        self._circumradius = circumradius
        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None



    def __repr__(self):
        return f"Polygon(vertices_number={self._vertices_number}, circumradius={self._circumradius})"

    @property
    def count_vertices(self):
        return self._vertices_number

    @property
    def count_edges(self):
        return self._vertices_number

    @property
    def circumradius(self):
        return self._circumradius

    @property
    def interior_angle(self):
        if self._interior_angle == None:
            self._interior_angle = (self._vertices_number - 2) * 180 / self._vertices_number 

        return self._interior_angle

    @property
    def side_length(self):
        if self._side_length == None:
            self._side_length = 2 * self._circumradius * math.sin(math.pi / self._vertices_number)
        return self._side_length

    @property
    def apothem(self):
        if self._apothem == None:
            self._apothem = self._circumradius * math.cos(math.pi / self._vertices_number)
        return self._apothem

    @property
    def area(self):
        if self._area == None:
            self._area = self._vertices_number / 2 * self.side_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter == None:
            self._perimeter = self._vertices_number * self.side_length
        return self._perimeter

    def __eq__(self, other):
        # check whether is the polygon class
        if isinstance(other, self.__clasee__):
            return (self.count_edges == other.count_edges
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented



