from Course import Course
from Instructor import Instructor
from Time import Time
from department import Department
from Section import Section
import department
import  department
from Course import Course
from Instructor import Instructor
import random


class Schedule:
    def __init__(self, data):
        self.data = data
        self.conflicts = 0
        self.sections = []
        self.mytimetable = {}
        self.sunday = []
        self.monday = []
        self.tuesday = []
        self.wednsday = []
        self.thursday = []
        self.allinstructors_hours=self.data.instructors_hours
        self.allinstructors_generatedhours={'ahmed':{"network": 0, "electronics": 0, "selected": 0},'mohamed': {"operating_system": 0, "database2": 0, "selected": 0},'ali': {"operating_system": 0, "network": 0, "ethics": 0}}
        self.instructor_names=self.data.instructors_names

    def generate_sample(self):

        hours = self.data.sum_hours
        departments=self.data.get_departments()
        #for i in range(len(departments)):
        for i in range(len(departments)): #3 dept
            #print(departments[i].number_sections())
            list_courses_names=[]
            list_courses=[]
            list_courses_names.extend(departments[i].number_sections().keys()) #selected, os
            list_courses.extend(departments[i].get_courses())

           # print(list_type)
            #print(departments[i].number_sections().get(list_type[i])
            #print(departments[i].number_sections().values())
            for j in range(len(departments[i].number_sections())):#courses
                instructors = []
                instructors.extend(departments[i].get_course_instructor(list_courses_names[j]))#bgeb instructor course
                for l in range(departments[i].number_sections().get(list_courses_names[j])): #3dd sections= bloop 3la value 2ly gowa coursename 2ly hyah 3dd sections
                    x = random.randint(0,len(instructors)-1)
                    #print(instructors[x])
                    #print(list_courses_names[j])
                    starttime=random.randint(8,16)
                    addorsubtract=random.randint(0,1)

                    day=random.randint(0,4)
                    if(day==0):
                        day='sunday'
                    if (day == 1):
                        day = 'monday'
                    if (day == 2):
                        day = 'tuesday'
                    if (day == 3):
                        day = 'wednsday'
                    if (day == 4):
                        day = 'thursday'

                    #0=add,1=subtract
                    if starttime<10:
                        endtime = starttime + 2
                        addorsubtract=2

                    elif addorsubtract==0:
                        endtime=starttime+2

                    elif addorsubtract==1:
                        temp=starttime
                        endtime=starttime
                        starttime=temp-2
                    time= Time(day,starttime,endtime)
                    section = Section(list_courses_names[j],time)
                    section.set_instructor(instructors[x])
                    self.sections.append(section)

        self.arrange_sections()
        self.calculate_conflicts()

    def print_sections(self):
        if(len(self.sunday) + len(self.monday) + len(self.wednsday) + len(self.tuesday) + len(self.thursday) > 0 ):
           self.arrange_existedsections()

        else:
         self.arrange_sections()

        print('SUNDAY')
        for i in range(len(self.sunday)):
          print(self.sunday[i])
        print('MONDAY')
        for j in range(len(self.monday)):
          print(self.monday[j])
        print('TUESDAY')
        for k in range(len(self.tuesday)):
          print(self.tuesday[k])
        print('WEDNSDAY')
        for l in range(len(self.wednsday)):
          print(self.wednsday[l])
        print('THURSDAY')
        for m in range(len(self.thursday)):
          print(self.thursday[m])

    def arrange_sections(self):

        for i in range(len(self.sections)):
            if(self.sections[i].get_day()=='sunday'):
                self.sunday.append(self.sections[i])

            if (self.sections[i].get_day() == 'monday'):
                self.monday.append(self.sections[i])

            if (self.sections[i].get_day() == 'tuesday'):
                self.tuesday.append(self.sections[i])

            if (self.sections[i].get_day() == 'wednsday'):
                self.wednsday.append(self.sections[i])

            if (self.sections[i].get_day() == 'thursday'):
                self.thursday.append(self.sections[i])

        self.mytimetable['sunday'] = self.sunday
        self.mytimetable['monday'] = self.monday
        self.mytimetable['tuesday'] = self.tuesday
        self.mytimetable['wednsday'] = self.wednsday
        self.mytimetable['thursday'] = self.thursday
        return self.mytimetable

    def calculate_conflicts(self):
        self.conflicts=0
        self.arrange_existedsections()
        self.calculate_generatedhoursIns()
        section_conflicts=0
        for j in range(len(self.sunday)):
            for k in range(len(self.sunday)):
                if(k!=j):
                    section1=self.sunday[j]
                    section2=self.sunday[k]
                    if(section1.get_instructor_name()==section2.get_instructor_name()  and abs(section1.time.start-section2.time.start)<2):
                        section_conflicts+=1

        for j1 in range(len(self.monday)):
            for k1 in range(len(self.monday)):
                if(k1!=j1):
                    section1=self.monday[j1]
                    section2=self.monday[k1]
                    if(section1.get_instructor_name()==section2.get_instructor_name()  and abs(section1.time.start-section2.time.start)<2):
                        section_conflicts+=1

        for j2 in range(len(self.tuesday)):
            for k2 in range(len(self.tuesday)):
                if(k2!=j2):
                    section1=self.tuesday[j2]
                    section2=self.tuesday[k2]
                    if(section1.get_instructor_name()==section2.get_instructor_name()  and abs(section1.time.start-section2.time.start)<2):
                        section_conflicts+=1

        for j3 in range(len(self.wednsday)):
            for k3 in range(len(self.wednsday)):
                if(k3!=j3):
                    section1=self.wednsday[j3]
                    section2=self.wednsday[k3]
                    if(section1.get_instructor_name()==section2.get_instructor_name() and abs(section1.time.start-section2.time.start)<2):
                        section_conflicts+=1

        for j4 in range(len(self.thursday)):
            for k4 in range(len(self.thursday)):
                if(k4!=j4):
                    section1=self.thursday[j4]
                    section2=self.thursday[k4]
                    if(section1.get_instructor_name()==section2.get_instructor_name()  and abs(section1.time.start-section2.time.start)<2):
                        section_conflicts+=1

        self.conflicts=section_conflicts//2+self.conflicts
        self.conflicts+=self.calculate_instructorconf()

        #print("Conflicts:"+str(self.conflicts))
       #     if (j != i):
         #       for j in range(len(self.sections)):





    def calculate_generatedhoursIns(self):

        self.allinstructors_generatedhours={'ahmed':{"network": 0, "electronics": 0, "selected": 0},'mohamed': {"operating_system": 0, "database2": 0, "selected": 0},'ali': {"operating_system": 0, "network": 0, "ethics": 0}}

        for i in range(len(self.sections)):
            section = self.sections[i]
            section.get_instructor_name()
            self.allinstructors_generatedhours[section.get_instructor_name()][section.course]+=2
        #print(self.allinstructors_generatedhours)


    def calculate_instructorconf(self):
        self.allinstructors_generatedhours
        self.allinstructors_hours
        self.instructor_names
        generatedlist = []
        originalist = []
        maxconflict=0
        for i in range(len(self.instructor_names)):
            originalist.clear()
            generatedlist.clear()
            originalist.extend(self.allinstructors_hours.get(self.instructor_names[i]).values())#ahmed original
            generatedlist.extend(self.allinstructors_generatedhours.get(self.instructor_names[i]).values())#ahmed generated
            for j in range(len(originalist)):
                if(abs(originalist[j]-generatedlist[j])>0):
                    maxconflict+=1

        #print(maxconflict)
        return maxconflict


    def get_sections(self):
        return self.sections

    def get_conflict(self):
        return self.conflicts

    def setsections(self,sections):
        self.sections=sections
        #self.print_sections()
        self.calculate_conflicts()

    def arrange_existedsections(self):
        self.sunday.clear()
        self.monday.clear()
        self.thursday.clear()
        self.tuesday.clear()
        self.wednsday.clear()
        self.arrange_sections()










