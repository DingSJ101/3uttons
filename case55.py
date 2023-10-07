from base import NewSolution
from base import Step
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [1,0,1,0,0,1,0,0,0,0,0,1]
        dest = [0,0,0,0,0,0,0,0,1,1,1,1] 
        controls = []
        self.dims = [8]
        super().__init__(init,dest,controls)
        
    def left(self,state,controls):
        i = self.dims[0]
        state = state[1:i]+[state[0]]+state[i+1:]+[state[i]]
        return state,controls

    def right(self,state,controls):
        i = self.dims[0]
        state = [state[i]]+state[:i]+[state[-1]]+state[i:]
        return state,controls
    def middle(self,state,controls):
        state[0],state[self.dims[0]] = state[self.dims[0]],state[0]
        return state,controls

if __name__ == '__main__':
    a = mySolution()
    print(a.run(8))