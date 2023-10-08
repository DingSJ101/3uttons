from base import NewSolution,queue
from base import Step
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = []
        dest = [1,2,8] 
        controls = []
        super().__init__(init,dest,controls)

        
    def handle(self,state):
        if len(state)==0 : return state

        strs = queue.Queue()
        get_zero = 0
        l = []
        for num in state :
            if num == 0 :
                strs.put(l)
                l = []
                if get_zero == 0:
                    get_zero = 1
                    continue
                else :
                    strs.put([0])
            else:
                get_zero = 0
                l.append(num)
        strs.put(l)
        state = []
        while not strs.empty():
            l = strs.get()
            if len(l)==0 : continue
            
            for char in str(sum(l)):
                state.append(int(char))
        return state

    def left(self,state,controls):
        if (len(state)<8):
            state = state + [0]
        return state,controls

    def right(self,state,controls):
        state = self.handle(state)
        return state,controls
    def middle(self,state,controls):
        if (len(state)<8):
            state = state + [len(state)+1]
        return state,controls

if __name__ == '__main__':
    a = mySolution()
    print(a.handle([1,2,3,4,5,6,7,8,9,0]))
    print(a.handle([0,0,0,0,0,0,0]))
    print(a.handle([1,1,1,1,1,1]))
    print(a.handle([6,6,0,0,7,7,7,0,7,0,9,1]))
    def rander(state):
        print(''.join(str(state)))

    
    b = mySolution()
    step = b.init_step
    path = 'mmmmmmrmmlmmlmr'
    for s in path :
        step = b.move(step,s)
        rander(step.state)

    
    a.run(14)
    
    
