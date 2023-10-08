from base import NewSolution,LinearEquations
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
    # a = mySolution()
    # print(a.run(12))
    a = LinearEquations()
    a.addVars(['yellow','red','green'])
    # a.addEquations([[-1,1,0,-1],
    #                 [1,1,-1,6],
    #                 [1,-2,0,-3],
    #                 # [-1,0,1,-2]
    #                  ])
    a.addEquations(
        [[1,-3,1,0],
         [2,1,-1,21],
         [-2,1,0,-16]]
    )
    # a.addEquation([1,-1,0,0])
    print(a.solve())
    print(a)
    # ['r', 'r', 'l', 'l', 'r', 
    # 'm', 'l', 'm', 'm', 'l', 
    # 'm', 'l']