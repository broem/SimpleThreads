from datetime import datetime, date, timedelta
import project as project
import cityInfo as cityInfo

if __name__ == "__main__":
    d1 = datetime.strptime('9/1/15', '%m/%d/%y')
    d2 = datetime.strptime('9/1/15', '%m/%d/%y')
    dd = (d2 + timedelta(days=1)) - d1

    # build a project
    ok = project.Project(name='project1', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/1/15', '%m/%d/%y'))
    ok1 = project.Project(name='project2', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/2/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/5/15', '%m/%d/%y'))
    mySet = [ok1, ok]

    print(dd.days)
