# instructor,course,matrix lecture*course wi element hours array in array
from Course import Course
from Instructor import Instructor
from department import Department

instructors_hours = {'ahmed':{"network": 2, "electronics": 6, "selected": 4},'mohamed': {"operating_system": 2, "database2": 6, "selected": 4},'ali': {"operating_system": 4, "network": 4, "ethics": 4}}
instructor_names=['ahmed','ali','mohamed']
instructors_hours_empty = {'ahmed':{"network": 0, "electronics": 0, "selected": 0},'mohamed': {"operating_system": 0, "database2": 0, "selected": 0},'ali': {"operating_system": 0, "network": 0, "ethics": 0}}
ahmed = Instructor(0, "ahmed", instructors_hours.get("ahmed"))
mohamed = Instructor(1, "mohamed", instructors_hours.get("mohamed"))
ali = Instructor(2, "ali", instructors_hours.get("ali"))
network = Course(0, "network")
electronics = Course(1, "electronics")
database2 = Course(2, "database2")
ethics = Course(3, "ethics")
selected = Course(4, "selected")
operating_system = Course(5, "operating_system")

network.set_instructors(ahmed)
electronics.set_instructors(ahmed)
selected.set_instructors(ahmed)
operating_system.set_instructors(mohamed)
database2.set_instructors(mohamed)
selected.set_instructors(mohamed)
operating_system.set_instructors(ali)
network.set_instructors(ali)
ethics.set_instructors(ali)

sum_hours=sum(instructors_hours.get('ahmed').values())+sum(instructors_hours.get('mohamed').values())+sum(instructors_hours.get('ali').values())


class data:
    def __init__(self):
        self.sum_hours=sum_hours
        self.instructors_hours=instructors_hours
        self.instructors_names=instructor_names
        self.instructors_hours_empty=instructors_hours_empty
        self.cscourses =[]
        self.itcourses =[]
        self.iscourses =[]
        self.courses= []
        self.departments1=[]
        self.instructors = []
        self.instructors.append(ahmed)
        self.instructors.append(mohamed)
        self.instructors.append(ali)

        self.cscourses.append(selected)
        self.cscourses.append(operating_system)

        self.iscourses.append(ethics)
        self.iscourses.append(database2)

        self.itcourses.append(network)
        self.itcourses.append(electronics)

        self.courses.append(selected)
        self.courses.append(operating_system)
        self.courses.append(ethics)
        self.courses.append(database2)
        self.courses.append(network)
        self.courses.append(electronics)

        self.csdept = Department("cs", self.cscourses)
        self.isdept = Department("is", self.iscourses)
        self.itdept = Department("it", self.itcourses)
        self.departments1.append(self.csdept)
        self.departments1.append(self.isdept)
        self.departments1.append(self.itdept)


    def get_instructors(self):
        return self.instructors

    def get_departments(self):

        return self.departments1

    def get_courses(self):
        return self.courses

    def sum_ofhours(self):
        return self.sum_hours

    def instructor_hours(self):
        return self.instructors_hours


