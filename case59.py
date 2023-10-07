from base import NewSolution
from base import Step
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [2,1,-6,3]
        dest = [0,0,0,0] 
        controls = []
        super().__init__(init,dest,controls)

    def countMatchs(self,state):
        count = 0
        for i in range(len(state)):
            if state[i]==self.dest[i]:
                count+=1
        return count*2
        
    def left(self,state,controls):
        state[0]-=1
        state[1]-=1
        state[2]+=1
        state[3]+=1
        return state,controls

    def right(self,state,controls):
        state[0]+=1
        state[2]-=1
        return state,controls
    def middle(self,state,controls):
        state[1]+=1
        state[2]+=1
        state[3]-=2
        return state,controls

if __name__ == '__main__':
    a = mySolution()
    print(a.run(12))
    # ['r', 'r', 'l', 'l', 'r', 
    # 'm', 'l', 'm', 'm', 'l', 
    # 'm', 'l']