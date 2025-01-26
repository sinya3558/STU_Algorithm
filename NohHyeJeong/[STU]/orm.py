from dataclasses import dataclass
from typing import TypeVar


# dataclass
@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return (self.width * self.height)

rect = Rectangle(3, 4)
print(rect.area())


# TypeVar
T = TypeVar('T')
U = TypeVar('U')

def area_equal(a:T, b:U) -> bool:
    return a==b

print(area_equal(10, 10.0))
