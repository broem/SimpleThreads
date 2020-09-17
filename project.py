import cityInfo as cityInfo
from datetime import datetime, date, timedelta

class Project:
    def __init__(self, name, cityType, dateStart, dateEnd):
        self.name = name
        self.cityType = cityType
        self.dateStart = dateStart
        self.dateEnd = dateEnd

        
    @classmethod
    def datesOverlap(self, d1, d2):
        return (d2 - d1) <= timedelta(days=1)
    @classmethod
    def getDateRange(self, low, high):
        return ((high + timedelta(days=1)) - low).days
    @classmethod
    def travelModifier(self, proj):
        if proj.cityType == cityInfo.CityType.low:
            return cityInfo.TravelCost.LowCityFull - cityInfo.TravelCost.LowCityTravel
        else:
            return cityInfo.TravelCost.HighCityFull - cityInfo.TravelCost.HighCityTravel
    
    @classmethod
    def mergeOverlappedLeft(self, toBeMergedInto, toBeMergedWith, distance):
        merged = toBeMergedInto[:(len(toBeMergedInto)-distance)] + toBeMergedWith
        return merged
    @classmethod
    def mergeOverlappedRight(self, toBeMergedInto, toBeMergedWith, distance):
        merged = toBeMergedWith + toBeMergedInto[distance:]
        return merged
    
    @classmethod
    def getReimbursement(cls, projectSet):
        reimbursement = 0
        reimbSet = []
        if len(projectSet) <= 0:
            return reimbursement

        projectSet = sorted(projectSet, key=lambda project: project.dateStart)
        
        for i, project in enumerate(projectSet):
            curList = []
            lowcost = project.cityType == cityInfo.CityType.low
            if lowcost:
                curList = [cityInfo.CityType.low]*Project.getDateRange(project.dateStart, project.dateEnd)
            else:
                curList = [cityInfo.CityType.high]*Project.getDateRange(project.dateStart, project.dateEnd)
            # check if the prev start date are in the same range
            if i != 0 and Project.datesOverlap(projectSet[i-1].dateEnd, project.dateStart):
                distanceOverlapped = Project.getDateRange(projectSet[i-1].dateEnd, project.dateStart)
                # distance overlapped > 2 means they are not sitting next to each other
                if distanceOverlapped > 2:
                    # check to see if they are different city types, highs take precident
                    if projectSet[i-1].cityType != lowcost:
                        if lowcost:
                            merged = Project.mergeOverlappedRight(curList, reimbSet[i-1], distanceOverlapped)
                        else:
                            merged = Project.mergeOverlappedRight(reimbSet[i-1], curList, distanceOverlapped)
                else:
                    merged = Project.mergeOverlappedRight(reimbSet[i-1], curList, 0)

            # not a single day
            elif (Project.getDateRange(projectSet[i].dateStart, projectSet[i].dateEnd)) >= 2:
                if lowcost:
                    reimbursement += cityInfo.TravelCost.LowCityTravel
                    reimbursement += (Project.getDateRange(projectSet[i].dateStart, projectSet[i].dateEnd) - 2)  * cityInfo.TravelCost.LowCityFull
                    reimbursement += cityInfo.TravelCost.LowCityTravel
                else:
                    reimbursement += cityInfo.TravelCost.HighCityTravel
                    reimbursement += (Project.getDateRange(projectSet[i].dateStart, projectSet[i].dateEnd) - 2)  * cityInfo.TravelCost.HighCityFull
                    reimbursement += cityInfo.TravelCost.HighCityTravel
            # a single day
            else:
                # the days are short
                if lowcost:
                    reimbursement += cityInfo.TravelCost.LowCityTravel
                else:
                    reimbursement += cityInfo.TravelCost.HighCityTravel
        
        return reimbursement

