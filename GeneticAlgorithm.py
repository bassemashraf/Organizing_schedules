import Schedule
from Data import data
from random import random
data=data()


class GenticAlgo:
    def __init__(self,population): #list gdwal
        self.population = population
        self.selected_schedule = []
        self.mutate_rate=1
        self.schedules_conflict=[]

    def selection(self):
        schedules = self.population
        schedules_conflicts = []

        for i in range(len(schedules)):
            schedules[i].calculate_conflicts()
            schedules_conflicts.append(schedules[i].get_conflict())

        schedules_conflicts.sort()
        selection1=schedules_conflicts[0]
        selection2=schedules_conflicts[1]
        #print(schedules_conflicts)
        self.selected_schedule.clear()
        for i in range (len(schedules)):
            if schedules[i].get_conflict() == selection1 or schedules[i].get_conflict() == selection2:
                self.selected_schedule.append(schedules[i])
        self.schedules_conflict.clear()
        self.schedules_conflict.extend(schedules_conflicts)

    def crossover(self):
        self.selection()
        sectionschedule1=[]
        #print("selected schedule conflict parent 1")
        #print(self.selected_schedule[0].conflicts)
        sectionschedule1=self.selected_schedule[0].sections
        #print("selected schedule conflict parent 2")
        #print(self.selected_schedule[1].conflicts)
        sectionschedule2=self.selected_schedule[1].sections
        half1=0
        half2=0
        if len(sectionschedule2)%2!=0:
            half1=len(sectionschedule1)//2
            half2=half1+1
        if len(sectionschedule2) % 2 == 0:
                half1=half2=len(sectionschedule2)//2
        crossover_section=[]
        crossover_section2 = []
        for i in range(half1):
            crossover_section.append(sectionschedule1[i])
        for j in range (half2,len(sectionschedule2)):
            crossover_section.append(sectionschedule2[j])
        crossover_scheduale=Schedule.Schedule(data)
        crossover_scheduale.setsections(crossover_section)
        #print("cross_over1 :"+str(crossover_scheduale.conflicts))


        #
        for k in range(half1):
            crossover_section2.append(sectionschedule2[k])
        for l in range (half2,len(sectionschedule2)):
            crossover_section2.append(sectionschedule1[l])


        crossover_scheduale2=Schedule.Schedule(data)
        crossover_scheduale2.setsections(crossover_section2)
        #print("cross_over2 :"+str(crossover_scheduale2.conflicts))

        if(crossover_scheduale2.conflicts>crossover_scheduale.conflicts):

            self.mutate_schedule(crossover_scheduale)

        else:

            self.mutate_schedule(crossover_scheduale2)

        self.population.append(crossover_scheduale2)
        self.population.append(crossover_scheduale)





    def mutate_schedule(self,schedule):
        mutate_schedule=Schedule.Schedule(data)
        mutate_schedule.generate_sample()
        for i in range(len(schedule.sections)):
            if(self.mutate_rate>random()):
                schedule.sections[i]=mutate_schedule.sections[i]
        schedule.calculate_conflicts()
        #print(schedule.print_sections())
        #print("after mutate :"+str(schedule.conflicts))

    def loopfornumber(self,number):
        for i in range (0,number):
            self.crossover()
        self.printrighttable()

    def loopuntilnumber(self,number):
        while number not in self.schedules_conflict:
            self.crossover()
            if self.schedules_conflict[0] < number:
                break
        self.printrighttable()


    def printrighttable(self):
        schedules = self.population
        schedules_conflicts = []

        for i in range(len(schedules)):
            schedules_conflicts.append(schedules[i].get_conflict())

        schedules_conflicts.sort()
        selection1 = schedules_conflicts[0]
        for i in range (len(schedules)):
            if schedules[i].get_conflict() == selection1:
                result=schedules[i]
        print(result.print_sections())
        result.calculate_conflicts()
        print("Conflict :"+str(result.conflicts))