class Course:

    def __init__(self, id, name,  instructors = []):
        self.id = id
        self.name = name
        self.instructors = []

    def set_instructors(self,instructor):
        self.instructors.append(instructor)

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        return self.name[item]

    def __repr__(self):
        return str(self)

    def get_instructors(self):
        return self.instructors

    def get_name(self):
        return self.name
