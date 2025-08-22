from polygon import Polygon

class Polygons():
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 2')

        self._m = m
        self._R = R

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'

    def __iter__(self):
        return PolygonIterator(self._m, self._R)

    def __getitem__(self, idx):
        return self._polygons[idx]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(PolygonIterator(self._m, self._R), 
                                key=lambda p: p.area/p.perimeter,
                                reverse=True)

        return sorted_polygons[0]


class PolygonIterator:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 2')

        self._m = m
        self._R = R 
        self._side_idx = 3
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._side_idx > self._m:
            raise StopIteration
        else:
            result = Polygons(self._side_idx, self._R)
            self._side_idx += 1
            return result