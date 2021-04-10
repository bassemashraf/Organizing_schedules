class Section:
    def __init__(self,course,time,ID=0):
        self.id = ID
        self.course = course
        self.time=time
        self.instructor=None
    def set_instructor(self, instructor):
        self.instructor = instructor

   # def set_room(self,room):
     #   self.room=room

   # def set_time(self,time):
    #    self.time=time
    def __str__(self):
        return self.course+":"+self.time.printdate()+"  by  "+self.instructor.getname()

    def get_day(self):
        return self.time.day

    def get_instructor_name(self):
        return self.instructor.getname()

    def getcoursename(self):
        return self.course
