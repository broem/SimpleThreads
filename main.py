from datetime import datetime, date, timedelta
import project as project
import cityInfo as cityInfo

if __name__ == "__main__":
    # build a project
    ok = project.Project(name='project1', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/1/15', '%m/%d/%y'))
    ok1 = project.Project(name='project2', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/3/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/5/15', '%m/%d/%y'))
    ok2 = project.Project(name='project3', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/4/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/8/15', '%m/%d/%y'))
    mySet = [ok1, ok, ok2]

    yo = project.Project.getReimbursement(projectSet=mySet)

    print(yo)
