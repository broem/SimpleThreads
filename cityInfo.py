from enum import Enum

class CityType(Enum):
    low = 1
    high = 2

class TravelCost:
    LowCityTravel = 45
    HighCityTravel = 55
    LowCityFull = 75
    HighCityFull = 85