from base import task
class solution(task):
    def __init__(self) -> None:
        super().__init__()
    def init(self): 
        self.params = [0,0,0,0,0]
        
    def judge(self):
        if self.params == [1,1,1,1,1]:
            return True
        return False
    # y,r,l

    def left(self):
        begin = self.params[0]
        self.params[:4] = self.params[1:]
        self.params[4] = begin
    def right(self):
        end = self.params[4]
        self.params[1:] = self.params[:4]
        self.params[0] = end
    def middle(self):
        for i in range(1,4):
            self.params[i] = 1-self.params[i]

a = solution()
result = a.run(20)
print(result)