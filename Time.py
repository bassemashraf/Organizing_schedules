class Time:
    def __init__(self, day, start,end):
        self.amOrPm="am"
        self.start=0
        self.day=day
        self.start = start
        self.end = end

        #if self.start>12:
        #    self.start=start-12
         #   self.amOrPm="pm"
        #if self.end > 12:
         #   self.end = end - 12

    def printdate(self):
        date=self.start.__str__()+":"+self.end.__str__()
        return date