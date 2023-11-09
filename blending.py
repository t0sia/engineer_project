from enum import Enum


class Blending(Enum):
    translucent = 1
    translucent_no_depth = 2
    additive = 3
    minimum = 4
    opaque = 5
