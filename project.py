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
    def getReimbursement(cls, projectSet):
        reimbursement = 0
        if len(projectSet) <= 0:
            return reimbursement

        projectSet = sorted(projectSet, key=lambda project: project.dateStart)
        
        for i, project in enumerate(projectSet):
            
            lowcost = project.cityType == cityInfo.CityType.low
            # check if the prev start date are in the same range
            if i != 0 and Project.datesOverlap(projectSet[i-1].dateEnd, project.dateStart):
                if lowcost:
                    # we need to remove prev project travel and add 1 prev day
                    ok = (Project.getDateRange(projectSet[i-1].dateEnd, projectSet[i].dateEnd) - 2)
                    if ok >= 0:
                        reimbursement +=  ok * cityInfo.TravelCost.LowCityFull
                        reimbursement += cityInfo.TravelCost.LowCityTravel
                        if ok > 0:
                            reimbursement += Project.travelModifier(projectSet[i-1])
                else:
                    ok = (Project.getDateRange(projectSet[i-1].dateEnd, projectSet[i].dateEnd) - 2)
                    if ok >= 0:
                        reimbursement +=  ok * cityInfo.TravelCost.HighCityFull
                        reimbursement += cityInfo.TravelCost.HighCityTravel
                        if ok > 0:
                            reimbursement += Project.travelModifier(projectSet[i-1])
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

