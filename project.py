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
        return (d2 - d1) > timedelta(days=2)
    @classmethod
    def getDateRange(self, d1, d2):
        return ((d2 + timedelta(days=1)) - d1).days
    
    @classmethod
    def getReimbursement(cls, projectSet):
        reimbursement = 0
        firstPass = True
        if len(projectSet) <= 0:
            return reimbursement

        projectSet = sorted(projectSet, key=lambda project: project.dateStart)
        
        for i, project in enumerate(projectSet):
            lowcost = project.cityType == cityInfo.CityType.low
            if firstPass:
                firstPass = False
                if lowcost:
                    reimbursement += cityInfo.TravelCost.LowCityTravel
                else:
                    reimbursement += cityInfo.TravelCost.HighCityTravel
            else:
                # check if the prev start date are in the same range
                if Project.datesOverlap(projectSet[i-1].dateEnd, project.dateStart):
                    if lowcost:
                        reimbursement += (Project.getDateRange(projectSet[i-1].dateEnd, projectSet[i-1].dateStart) - 1)  * cityInfo.TravelCost.LowCityFull
                    else:
                        reimbursement += (Project.getDateRange(projectSet[i-1].dateEnd, projectSet[i-1].dateStart) - 1)  * cityInfo.TravelCost.HighCityFull
                elif (Project.getDateRange(projectSet[i-1].dateEnd, projectSet[i-1].dateStart)) > 2:
                    if lowcost:
                        reimbursement += (Project.getDateRange(projectSet[i-1].dateEnd, projectSet[i-1].dateStart) - 2)  * cityInfo.TravelCost.LowCityFull
                        reimbursement += cityInfo.TravelCost.LowCityTravel
                    else:
                        reimbursement += (Project.getDateRange(projectSet[i-1].dateEnd, projectSet[i-1].dateStart) - 2)  * cityInfo.TravelCost.HighCityFull
                        reimbursement += cityInfo.TravelCost.HighCityTravel
                else:
                    # the days are short
                    if lowcost:
                        reimbursement += cityInfo.TravelCost.LowCityFull
                        reimbursement += cityInfo.TravelCost.LowCityTravel
                    else:
                        reimbursement += cityInfo.TravelCost.HighCityFull
                        reimbursement += cityInfo.TravelCost.HighCityTravel

            # if they are then we dont have "travel" days, use full
        
        return reimbursement

