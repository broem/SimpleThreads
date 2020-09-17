import unittest
from datetime import datetime, date, timedelta
import project as project
import cityInfo as cityInfo


class ProjectsSetTests(unittest.TestCase):
    def test_1(self):
        ok = project.Project(name='project1', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/1/15', '%m/%d/%y'))
        ok1 = project.Project(name='project2', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/3/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/5/15', '%m/%d/%y'))
        ok2 = project.Project(name='project3', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/4/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/8/15', '%m/%d/%y'))
        mySet = [ok1, ok, ok2]
        resp = project.Project.getReimbursement(projectSet=mySet)
        
        self.assertTrue(resp == 435)
    
    def test_single_day(self):
        ok = project.Project(name='project1', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/3/15', '%m/%d/%y'))
        mySet = [ok]
        resp = project.Project.getReimbursement(projectSet=mySet)

        self.assertTrue(resp == 165)

    def test_set_with_consecutive_singles(self):
        ok = project.Project(name='project1', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/1/15', '%m/%d/%y'))
        ok1 = project.Project(name='project2', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/1/15', '%m/%d/%y'))
        ok2 = project.Project(name='project3', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/2/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/2/15', '%m/%d/%y'))
        ok3 = project.Project(name='project3', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/2/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/3/15', '%m/%d/%y'))
        mySet = [ok, ok1, ok2, ok3]
        resp = project.Project.getReimbursement(projectSet=mySet)

        self.assertTrue(resp == 165)
    
    def test_mix_high_next_to_each_other(self):
        ok = project.Project(name='project1', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/1/15', '%m/%d/%y'))
        ok1 = project.Project(name='project2', cityType=cityInfo.CityType.high, dateStart=datetime.strptime('9/2/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/6/15', '%m/%d/%y'))
        ok2 = project.Project(name='project3', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/6/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/8/15', '%m/%d/%y'))
        mySet = [ok1, ok, ok2]
        resp = project.Project.getReimbursement(projectSet=mySet)

        self.assertTrue(resp == 590)
    
    def test_set_with_consecutive_singles_mixed(self):
        ok = project.Project(name='project1', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/1/15', '%m/%d/%y'))
        ok1 = project.Project(name='project2', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/1/15', '%m/%d/%y'))
        ok2 = project.Project(name='project3', cityType=cityInfo.CityType.high, dateStart=datetime.strptime('9/2/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/2/15', '%m/%d/%y'))
        ok3 = project.Project(name='project3', cityType=cityInfo.CityType.high, dateStart=datetime.strptime('9/2/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/3/15', '%m/%d/%y'))
        mySet = [ok, ok1, ok2, ok3]
        resp = project.Project.getReimbursement(projectSet=mySet)

        self.assertTrue(resp == 185)
    
    def test_consecutive_highs_mixed(self):
        ok = project.Project(name='project1', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/3/15', '%m/%d/%y'))
        ok1 = project.Project(name='project2', cityType=cityInfo.CityType.high, dateStart=datetime.strptime('9/5/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/7/15', '%m/%d/%y'))
        ok2 = project.Project(name='project3', cityType=cityInfo.CityType.high, dateStart=datetime.strptime('9/8/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/8/15', '%m/%d/%y'))
        mySet = [ok1, ok, ok2]
        resp = project.Project.getReimbursement(projectSet=mySet)
        
        self.assertTrue(resp == 445)

    def test_mixed_overlap_high_left(self):
        ok = project.Project(name='project1', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/1/15', '%m/%d/%y'))
        ok1 = project.Project(name='project2', cityType=cityInfo.CityType.high, dateStart=datetime.strptime('9/3/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/5/15', '%m/%d/%y'))
        ok2 = project.Project(name='project3', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/4/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/8/15', '%m/%d/%y'))
        mySet = [ok1, ok, ok2]
        resp = project.Project.getReimbursement(projectSet=mySet)
        
        self.assertTrue(resp == 465)

    def test_mixed_overlap_high_right(self):
        ok = project.Project(name='project1', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/1/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/1/15', '%m/%d/%y'))
        ok1 = project.Project(name='project2', cityType=cityInfo.CityType.low, dateStart=datetime.strptime('9/3/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/5/15', '%m/%d/%y'))
        ok2 = project.Project(name='project3', cityType=cityInfo.CityType.high, dateStart=datetime.strptime('9/4/15', '%m/%d/%y'), dateEnd=datetime.strptime('9/8/15', '%m/%d/%y'))
        mySet = [ok1, ok, ok2]
        resp = project.Project.getReimbursement(projectSet=mySet)
        
        self.assertTrue(resp == 485)


if __name__ == '__main__':
    unittest.main()
