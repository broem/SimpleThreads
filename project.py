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
                distanceOverlapped = Project.getDateRange(project.dateStart, projectSet[i-1].dateEnd)
                # distance overlapped >= 2 means they are not sitting next to each other
                if distanceOverlapped >= 2:
                    # check to see if they are different city types, highs take precident
                    if projectSet[i-1].cityType != cityInfo.CityType.low:
                        if lowcost:
                            reimbSet[len(reimbSet)-1] = Project.mergeOverlappedRight(curList, reimbSet[len(reimbSet)-1], distanceOverlapped)
                        else:
                            reimbSet[i-1] = Project.mergeOverlappedRight(reimbSet[len(reimbSet)-1], curList, distanceOverlapped)
                    else:
                        reimbSet[len(reimbSet)-1] = Project.mergeOverlappedRight(reimbSet[len(reimbSet)-1], curList, distanceOverlapped)
                else:
                    reimbSet[len(reimbSet)-1] = Project.mergeOverlappedRight(curList, reimbSet[len(reimbSet)-1], distanceOverlapped)
            else:
                reimbSet.append(curList)
        
        # calculate the real reimbursement
        for i, projSet in enumerate(reimbSet):
            for j, proj in enumerate(projSet):
                # these are 
                if j == 0 or j == len(projSet) - 1:
                    if proj == cityInfo.CityType.low:
                        reimbursement += cityInfo.TravelCost.LowCityTravel
                    else:
                        reimbursement += cityInfo.TravelCost.HighCityTravel
                else:
                    if proj == cityInfo.CityType.low:
                        reimbursement += cityInfo.TravelCost.LowCityFull
                    else:
                        reimbursement += cityInfo.TravelCost.HighCityFull

        
        return reimbursement

