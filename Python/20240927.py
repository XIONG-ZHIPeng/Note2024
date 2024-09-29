class MyCalendarTwo(object):

    def __init__(self):
        self.single = list()
        self.double = list()
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for event in self.single:
            if start >= event[1] or end <= event[0]:
                continue
            else:
                for devent in self.double:
                    if start >= devent[1] or end <= devent[0]:
                        continue
                    else:
                        return False
        else:
            for event in self.single:
                if start >= event[1] or end <= event[0]:
                    continue
                else:
                    self.double.append([max(start,event[0]),min(end,event[1])])
            self.single.append([start,end])
            self.single.sort()
            return True

obj = MyCalendarTwo()
Lists = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
for i in Lists:
    print(obj.book(i[0],i[1]))