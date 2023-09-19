from base import task
class task17(task):
    def __init__(self) -> None:
        super().__init__()
    def init(self):
        self.params['y']=5
        self.params['r']=5
        self.params['g']=5
        
    def judge(self):
        if self.params['y']==self.params['r'] and self.params['y']==self.params['g'] and self.params['r']==0:
            return True
        return False
    # y,r,l

    def left(self):
        self.params['y'] = (self.params['y']+1) % 10
        self.params['r'] = (self.params['r']+1) % 10
    def right(self):
        self.params['r'] = (self.params['r']-1) % 10
        self.params['g'] = (self.params['g']-1) % 10
    def middle(self):
        self.params['r'] = 9-self.params['r']

a = task17()
result = a.run(20)
print(result)