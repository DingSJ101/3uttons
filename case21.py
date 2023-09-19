from base import BaseTask,Solution,NewSolution
import multiprocessing
class Task(BaseTask):
    def __init__(self) -> None:
        super().__init__()
    def init(self): 
        self.params = [6,3,5,2,4,1]
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
                self.params[self.index:self.index+3] = self.params[self.index+1:self.index+4]
                self.params[self.index+3] = begin
        else:
            self.index = max(self.index-1,0)

    def right(self):
        if self.selected:
            if self.index != 3:
                self.index += 1
                end = self.params[self.index+2]

                self.params[self.index:self.index+3] = self.params[self.index-1:self.index+2]
                self.params[self.index-1] = end
        else:
            self.index = min(self.index +1 ,3)
        
        
    def middle(self):
        self.selected = 1-self.selected

class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [6,3,5,2,4,1]
        dest = [1,2,3,4,5,6]
        controls = [0,2]
        super().__init__(init,dest,controls)
    def left(self, info) -> {}:
        if info['controls'][0]:
            if info['controls'][1] !=0:
                info['controls'][1] -= 1
                begin  = info['state'][info['controls'][1]]
                info['state'][info['controls'][1]:info['controls'][1]+3] = info['state'][info['controls'][1]+1:info['controls'][1]+4]
                info['state'][info['controls'][1]+3] = begin
        else:
            info['controls'][1] = max(info['controls'][1]-1,0)
        return info
    def right(self, info) -> {}:
        if info['controls'][0]:
            if info['controls'][1] !=3:
                info['controls'][1] += 1
                end = info['state'][info['controls'][1]+2]

                info['state'][info['controls'][1]:info['controls'][1]+3] = info['state'][info['controls'][1]-1:info['controls'][1]+2]
                info['state'][info['controls'][1]-1] = end
        else:
            info['controls'][1] = min(info['controls'][1] +1 ,3)
        return info
    def middle(self, info) -> {}:
        info['controls'][0] = 1-info['controls'][0]
        return info

if __name__ == '__main__':
    # multiprocessing.freeze_support()
    # a = Solution(Task)
    # # print(a.run(10))
    # a.run_with_processes(17)
    b = mySolution()
    print(b.run(17))