from base import NewSolution
from base import Step
class mySolution(NewSolution):
    def __init__(self) -> None:
        # yellow:1,red:6,green:31
        init = [1,1,6,31,1,6,1,31,0,6,31,1,31,31,6,6]
        # init = [1,1,1,1,1,1,1,0,0,0,0,0,0,0]
        # init = [0,0,0,0,0,0,0,1,1,1,1,1,1,1]
        dest = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
        controls = []
        super().__init__(init,dest,controls)
    def check(self,state):
        s = sum(state[:5])
        if s==5 or s==30 or s==31*5:
            state[0],state[1],state[2],state[3],state[4] = 0,0,0,0,0
        s = sum(state[4:9])
        if s==5 or s==30 or s==31*5:
            state[5],state[6],state[7],state[8],state[4] = 0,0,0,0,0
        s = sum(state[8:13])
        if s==5 or s==30 or s==31*5:
            state[9],state[10],state[11],state[12],state[8] = 0,0,0,0,0
        s = sum(state[12:16])+state[0]
        if s==5 or s==30 or s==31*5:
            state[13],state[14],state[15],state[0],state[12] = 0,0,0,0,0
        return state
        
    def left(self,state,controls):
        state[1],state[3],state[11] ,state[9] = state[11],state[9],state[1],state[3]
        return self.check(state),controls

    def right(self,state,controls):
        state[5],state[7],state[15],state[13] = state[15],state[13],state[5],state[7]
        return self.check(state),controls
    def middle(self,state,controls):
        state = state[1:]+[state[0]]
        return self.check(state),controls

if __name__ == '__main__':
    a = mySolution()
    print(a.run(20))