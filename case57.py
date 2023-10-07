from base import NewSolution
from base import Step
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [0,1,2,2,2,2,1,1,2,1,2,2,
                1,2,0,2,1,0,2,0,
                1,2,2,1]
        dest = [2,2,2,2,2,2,2,2,2,2,2,2,
                1,1,1,1,1,1,1,1,
                0,0,0,0] 
        controls = []
        self.dims = [12,8,4]
        super().__init__(init,dest,controls)

    def countMatchs(self,state):
        count = 0
        for i in range(len(state)):
            if state[i]==self.dest[i]:
                count+=1
        return count*2
        
    def left(self,state,controls):
        i1 = self.dims[0]
        i2 = sum(self.dims[:2])
        state = state[1:i1]+[state[0]]\
            +state[i1+1:i2]+[state[i1]] \
            +state[i2+1:]+[state[i2]]
        return state,controls

    def right(self,state,controls):
        i1 = self.dims[0]
        i2 = sum(self.dims[:2])
        state = [state[i1-1]]+state[:i1-1] \
                +[state[i2-1]]+state[i1:i2-1] \
                +[state[-1]]+state[i2:-1]
        return state,controls
    def middle(self,state,controls):
        state[0],state[12],state[20],state[22],state[16],state[6] = \
            state[12],state[20],state[22],state[16],state[6],state[0]
        return state,controls

if __name__ == '__main__':
    a = mySolution()
    print(a.run(11))
    # [
    # 'l', 'm', 'm', 'l', 'l', 
    # 'm', 'l', 'l', 'l', 'm', 
    # 'm']
