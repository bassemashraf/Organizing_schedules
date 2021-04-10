from Schedule import  Schedule
import Data


class Population:
    def __init__(self ,size,data):
        self.schedules=[]
        self.data=data
        for i in range(size):
            x= Schedule(data)
            x.generate_sample()
            self.schedules.append(x)

    def get_schedules(self):
        return self.schedules