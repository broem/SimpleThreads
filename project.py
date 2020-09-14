import cityInfo as cityInfo 

class Project:
    def __init__(self, name, cityType, dateStart, dateEnd):
        self.name = name
        self.cityType = cityType
        self.dateStart = dateStart
        self.dateEnd = dateEnd
    
    def getReimbursement(self, projectSet):
        reimbursement = 0
        if len(projectSet) <= 0:
            return reimbursement

        projectSet = sorted(projectSet, key=lambda project: project.dateStart)
        
        for project in projectSet:
            # check if the prev start date are in the same range

            # if they are then we dont have "travel" days, use full
            
            pass

        return reimbursement