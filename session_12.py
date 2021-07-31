import math

"""Regular Polygon class"""
class RegularPoly:
    """Class to create a regular polygon"""
    def __init__(self, vert_count, radius):
        """Initialize the RegulaPoly class attributes"""

        self.vert_count = vert_count # Number of vertices of polygon
        self.radius     = radius # Circumradius
        self.interior_angle_l = None 
        self.edge_length_l = None
        self.apothem_l = None 
        self.area_l = None 
        self.perimeter_l = None 

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

    @property
    def edge_count(self):
        """Get edge count"""
        return(self.vert_count)

    @property
    def interior_angle(self):
        """Get interior angle value"""
        if self.interior_angle_l is not None:
            return self.interior_angle_l
        else:
            self.interior_angle_l =  ((self.vert_count - 2)*180)/math.pi
            return self.interior_angle_l

    @property
    def edge_length(self):
        """Get edge length value"""
        if self.edge_length_l is not None:
            return self.edge_length_l
        else:
            self.edge_length_l = (2 * self.radius * math.sin(math.pi / self.vert_count))
            return self.edge_length_l

    @property
    def apothem(self):
        """Get apothem value"""
        if self.apothem_l is not None:
            return self.apothem_l
        else:
            self.apothem_l =  (self.radius * math.cos(math.pi / self.vert_count))
            return self.apothem_l

    @property
    def area(self):
        """Get area value"""
        if self.area_l is not None:
            return self.area_l
        else:
            self.area_l =  (1 / 2 * (self.vert_count * self.edge_length * self.apothem))
            return self.area_l

    @property
    def perimeter(self):
        """Get perimeter value"""
        if self.perimeter_l is not None:
            return self.perimeter_l
        else:
            self.perimeter_l =  (self.vert_count * self.edge_length)

            return self.perimeter_l

    def __repr__(self):
        """ Return string for RegularPoly"""
        return (f'RegularPoly({self.vert_count}, {self.radius})')


    def __eq__(self,other):
        """ Check for the equality of RegularPoly"""
        if isinstance(other, RegularPoly):
            return(self.vert_count == other.vert_count and self.radius == other.radius)
        else:
            raise NotImplementedError('Incorrect data type')

    def __gt__(self,other):
        """ Check for the greater than ineqaulity for RegularPoly"""
        if isinstance(other, RegularPoly):
            return(self.vert_count > other.vert_count)
        else:
            raise NotImplementedError('Incorrect data type')