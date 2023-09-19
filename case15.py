from base import task
class solution(task):
    def __init__(self) -> None:
        super().__init__()
    def init(self): 
        self.params = [0,0,1,1,1,0,0]
        self.state = 0
        
    def judge(self):
        if self.params == [1,0,0,1,0,1,0]:
            return True
        return False
    # y,r,l

    def left(self):
        if self.state == 0:
            for i in range(1,7):
                if self.params[i-1]: continue
                self.params[i-1] = self.params[i]
                self.params[i] = 0
        else:
            begin = self.params[0]
            for i in range(1,7):
                self.params[i-1] = self.params[i]
            self.params[6] = begin

    def right(self):
        if self.state == 0:
            for i in range(6,0,-1):
                if self.params[i]: continue
                self.params[i] = self.params[i-1]
                self.params[i-1] = 0
        else:
            end = self.params[6]
            for i in range(6,0,-1):
                self.params[i] = self.params[i-1]
            self.params[0] = end
        
    def middle(self):
        self.state = 1-self.state

a = solution()
print(a.run(20))