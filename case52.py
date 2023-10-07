from base import NewSolution
from base import Step
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [0,2,0,0,2,5,5,5,2,0,5,2]
        # init = [1,1,1,1,1,1,1,0,0,0,0,0,0,0]
        # init = [0,0,0,0,0,0,0,1,1,1,1,1,1,1]
        dest = [0,0,0,0,0,0,0,0,0,0,0,0] 
        controls = [4]
        super().__init__(init,dest,controls)
    def check(self,state):
        s = sum(state[:4])
        if s==8 or s==20:
            state[0],state[1],state[2],state[3] = 0,0,0,0
        s = sum(state[3:7])
        if s==8 or s==20:
            state[4],state[5],state[6],state[3] = 0,0,0,0
        s = sum(state[6:10])
        if s==8 or s==20:
            state[7],state[8],state[9],state[6] = 0,0,0,0
        s = sum(state[9:12])+state[0]
        if s==8 or s==20:
            state[10],state[11],state[0],state[9] = 0,0,0,0
        return state
        
    def left(self,state,controls):
        state[1],state[2],state[8],state[7] = state[8],state[7],state[1],state[2]
        return self.check(state),controls

    def right(self,state,controls):
        state[4],state[5],state[11],state[10] = state[11],state[10],state[4],state[5]
        return self.check(state),controls
    def middle(self,state,controls):
        state = state[1:]+[state[0]]
        return self.check(state),controls

if __name__ == '__main__':
    a = mySolution()
    print(a.run(20))