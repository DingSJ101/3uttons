from base import task
class solution(task):
    def __init__(self) -> None:
        super().__init__()
    def init(self): 
        self.params = [2,5,4,6,1,3]
        self.selected = 0
        self.index = 2
        
    def judge(self):
        if self.params == [1,2,3,4,5,6]:
            return True
        return False
    # y,r,l

    def left(self):
        if self.selected:
            if self.index != 0: 
                self.index -= 1
                begin  = self.params[self.index]
                self.params[self.index:self.index+2] = self.params[self.index+1:self.index+3]
                self.params[self.index+2] = begin
        else:
            self.index = max(self.index-1,0)


    def right(self):
        if self.selected:
            if self.index != 4:
                self.index += 1
                end = self.params[self.index+1]

                self.params[self.index:self.index+2] = self.params[self.index-1:self.index+1]
                self.params[self.index-1] = end
        else:
            self.index = min(self.index +1 ,4)
        
        
    def middle(self):
        self.selected = 1-self.selected

a = solution()
print(a.run(20))

from base import NewSolution
class mySolution(NewSolution):
    def __init__(self): 
        init = [2,5,4,6,1,3]
        dest = [1,2,3,4,5,6]
        controls = [0,2]
        super().__init__(init,dest,controls)
        
    def left(self,info)->{}:
        selected = info['controls'][0]
        index = info['controls'][1]
        params = info['state']
        if selected:
            if index != 0: 
                index -= 1
                begin  = params[index]
                params[index:index+2] = params[index+1:index+3]
                params[index+2] = begin
        else:
            index = max(index-1,0)
        return {'state':params,'controls':[selected,index]}
    def right(self,info)->{}:
        selected = info['controls'][0]
        index = info['controls'][1]
        params = info['state']
        if selected:
            if index != 4:
                index += 1
                end = params[index+1]

                params[index:index+2] = params[index-1:index+1]
                params[index-1] = end
        else:
            index = min(index +1 ,4)
        return {'state':params,'controls':[selected,index]}
        
    def middle(self,info) -> {}:
        info['controls'][0] = 1- info['controls'][0]
        return info

if __name__ == '__main__':
    b = mySolution()
    print(b.run(8))