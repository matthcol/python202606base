"""module with 2D shapes

- Point : a 2D point
- WeightedPoint : a 2D point with a weight
- Circle
- Polygon
"""
from dataclasses import dataclass
import math
from typing import override


@dataclass(order=True)
class Point:
    """ represents a 2D point
    with its cartesian coordinates and an optional name
    """

    x: float = 0.0
    y: float = 0.0
    name: str | None = None

    @override
    def __str__(self) -> str:
        return f"{
            '' if self.name is None else self.name
        }({
            self.x
        }, {
            self.y
        })"
    
    # NB: custom order
    ## __lt__ (<)
    ## __gt__ (>)
    ## __le__ (<=)
    ## __ge__ (>=)

    # surcharge de l'operator +, +=
    def __add__(self, other) -> Point:
        match other:
            case Point():
                return Point(
                    x=self.x + other.x,
                    y=self.y + other.y
                )
            case int() | float():
                return Point(
                    x=self.x + other,
                    y=self.y + other 
                )
            case (int() | float() as x, int() | float() as y):
                return Point(
                    x=self.x + x,
                    y=self.y + y
                )
            case _:
                return NotImplemented
            
    def __radd__(self, other) -> Point:
        return self.__add__(other)
    
    def __iadd__(self, other) -> Point:
        delta_x = 0.0
        delta_y = 0.0
        match other:
            case Point():
                delta_x = other.x
                delta_y = other.y
            case int() | float():
                delta_x = other
                delta_y = other
            case (int() | float() as x, int() | float() as y):
                delta_x = x
                delta_y = y
            case _:
                return NotImplemented
        self.translate(delta_x, delta_y)
        return self
    
    # def distance(self, other: 'Point') -> float:  # before Python 3.14
    def distance(self, other: Point) -> float:  # Python 3.14+
        """compute distance between this point and another

        parameters:
        - other : the 2nd point

        return: the distance
        """
        return math.hypot(
            self.x - other.x,
            self.y - other.y
        )
    
    def translate(self, delta_x: float, delta_y: float) -> None:
        """translate inplace this point with relative offsets

        parameters:
        - delta_x: horizontal offset  
        - delta_y: vertical offset
        """
        self.x += delta_x
        self.y += delta_y

        