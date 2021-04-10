class Instructor:
    def __init__(self, Id, name, instructor_hours):
        self.id = Id
        self.name = name
        self.instructor_hours = instructor_hours

    def __str__(self):
        return self.name

    def getname(self):
        return self.name
    #def __getitem__(self, item):
        #return Instructor(self.name[item])

    def get_instructor_hours(self):
        return self.instructor_hours


