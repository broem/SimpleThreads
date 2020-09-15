from enum import Enum

class CityType(Enum):
    low = 1
    high = 2

class TravelCost:
    LowCityTravel = 45
    HighCityTravel = 66
    LowCityFull = 55
    HighCityFull = 103