class Department:
    def __init__(self, name, courses):
        self.name = name
        self.courses1 = []
        self.courses1.extend(courses)

    def get_courses(self):
        return self.courses1

    def __getitem__(self, item):
        return self.courses1[item]

    def number_sections(self):
        sum_dict = {}
        #selected i=0
        #j=0 instructors bto3 selected
        for i in range(len(self.courses1)):
            sum_dict[self.courses1[i].get_name()] = 0

        for i in range(len(self.courses1)):

            for j in range(len(self.courses1[i].get_instructors())):

                hours_list=[]
                hours_list.extend(self.courses1[i].get_instructors()[j].get_instructor_hours().keys()) #ahmed

                self.courses1[i].get_name() in hours_list
                if self.courses1[i].get_name() in hours_list:

                   sum_dict[self.courses1[i].get_name()]+=self.courses1[i].get_instructors()[j].get_instructor_hours().get(self.courses1[i].get_name())


        for l in range(len(self.courses1)):
             sum_dict[self.courses1[l].get_name()]=sum_dict.get(self.courses1[l].get_name())//2

        return sum_dict

    def get_course_instructor(self,name):
        for i in range(len(self.courses1)):

            if name == self.courses1[i].get_name():
                return self.courses1[i].get_instructors()








