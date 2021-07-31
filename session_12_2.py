from collections import namedtuple
import session_12 as rp
from functools import lru_cache
Poly = namedtuple('PolygonTuples','Polys')



"""Regular Polygon Sequence class"""
class RegularPolySeq:
    """Class to create a sequence of regular polygon"""

    def __init__(self, vert_count, radius):
        """Initialize the RegulaPoly class attributes"""

        self.vert_count = vert_count # Number of vertices of polygon
        self.radius     = radius # Circumradius
        self.length_1   = None 
        self.max_eff_l = 0

    @property
    def vert_count(self):
        """Get count of vertices"""
        return self._vert_count

    @vert_count.setter
    def vert_count(self, vert_count):
        """Set the number of vertices of polygon"""
        if not isinstance(vert_count, int):
            raise TypeError(f'Number of vertices should be of type integer')
        if vert_count < 3:
            raise ValueError(f'Number of vertices should be greater than or equal to 3')

        self._vert_count = vert_count

    @property
    def radius(self):
        """Get circumradius"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Set the circumradius of polygon"""
        if not isinstance(radius, int):
            raise TypeError(f'Radius should be of type integer')
        if radius < 0:
            raise ValueError(f'Radius should be greater than 0')

        self._radius = radius

    def __getitem__(self, seq):
        """get next item in the sequence"""
        if isinstance(seq, int):
            seq = seq + 3
            if seq - 3 < 0:
                seq = self.vert_count + seq - 3
            if seq  < 3 or seq > self.vert_count:
                raise IndexError
            else:
                if seq >=3:
                    return RegularPolySeq._seq(seq, self.radius)
        else:
            raise TypeError ('Please provide valid integer value')

    def __len__(self):
        """get length of sequence"""
        if self.length_1 is not None:
            return self.length_1
        else:
            self.length_1  =    self.vert_count - 2   
            return self.length_1

    def __repr__(self):
        """ Return string for RegularPolySeq"""
        return (f'RegularPolySeq({self.vert_count}, {self.radius})')

    @property
    def max_efficiency_poly(self,n):
        """ find the max efficiency polygon """

        self.max_eff_l = n 
        return self.max_eff_l 




        # max_ratio = -100
        # for i in range(self.vert_count-2):
        #     area_perimeter_ratio = self.__getitem__(i)[1]
        #     if area_perimeter_ratio > max_ratio:
        #         max_ratio = area_perimeter_ratio
        #         max_ratio_polygon = self.__getitem__(i)[0]
        # return max_ratio_polygon

    def __reversed__(self) -> 'object':
        """
        Reverse and iterate
        :return object
        """
        return self.PolygonIterator(self.vert_count, self.radius, reverse=True)
        

    @staticmethod
    @lru_cache(2 ** 10)
    def _seq(seq,radius):
        if seq < 3:
            return None
        else:
            poly = rp.RegularPoly(seq,radius)
            return poly , poly.area/poly.perimeter




class PolygonIterator:
        """
        PolygonIterator class helps in behaviour of iteratable and iterator
        """
        def __init__(self, vc, radius_value, *, reverse=False) -> None:            
            self.vc = vc
            self.radius_value = radius_value
            self.reverse = reverse 
            self.length = vc
            self.i = 0
            self.curr_poly = 3
            self.max_efficient = 0 
        
        def __iter__(self) -> 'object':
            """
            Iterator
            :return self
            """            
            return self 
        

        def __next__(self) -> 'object':
            """
            Helps to iterate
            :return iterables
            """            
            if self.curr_poly > self.vc:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - self.i
                    self.i += 1                    
                else:
                    index = self.curr_poly
                item = rp.RegularPoly(index, self.radius_value)
                curr_efficiency = item.area/item.perimeter
                if curr_efficiency > self.max_efficient:
                    self.max_efficient = curr_efficiency
                    self.max_eff_poly_id = index
                Polygons.eff = self.max_eff_poly_id
                self.curr_poly += 1              
                return Poly(item)
