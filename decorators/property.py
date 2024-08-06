# Decorator @property
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get the radius of the circle"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Set the radius of the circle. Must be positive."""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
        
    def diameter(self):
        """Get the diameter of the circle"""
        return self._radius * 2
    
# Usage
my_circle = Circle(5)
print(my_circle.radius)
print(my_circle.diameter)