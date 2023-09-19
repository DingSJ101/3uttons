from base import task
class solution(task):
    def __init__(self) -> None:
        super().__init__()
    def init(self): 
        self.params = [8,7,3]
        self.count = 0
        self.last = ''
        
    def judge(self):
        if self.params == [6,6,6]:
            return True
        return False
    # y,r,l

    def left(self):
        if self.last == 'l':
            self.count += 1
        else :
            if self.count > 0:
                r = min(self.count,self.params[1])
                g = min(self.count,self.params[2])
                self.params[0] = self.params[0] + r + g
                self.params[1] -= r
                self.params[2] -= g
                self.count = 0
            else : 
                self.count +=1
        self.last = 'l'

    def right(self):
        if self.last == 'r':
            self.count += 1
        else :
            if self.count > 0:
                y = min(self.count,self.params[0])
                r = min(self.count,self.params[1])
                self.params[2] = self.params[2] + y + r
                self.params[0] -= y
                self.params[1] -= r
                self.count = 0
            else : 
                self.count +=1
        self.last = 'r'
        
    def middle(self):
        if self.last == 'm':
            self.count += 1
        else :
            if self.count > 0:
                y = min(self.count,self.params[0])
                r = min(self.count,self.params[2])
                self.params[1] = self.params[1] + y + r
                self.params[0] -= y
                self.params[2] -= r
                self.count = 0
            else : 
                self.count +=1
        self.last = 'm'

a = solution()
result = a.run(20)
print(result)