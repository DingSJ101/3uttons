from base import NewSolution
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [2,3,3,3,0,3,3,2]
        dest = [1,2,1,2,3,1,0,1] # bad ui in game : <|<|><O< is the right destination
        controls = [4]
        super().__init__(init,dest,controls)
    def left(self,state,controls):
        if controls[0]!=0:
            idx = controls[0]
            state[idx-1],state[idx] = state[idx],state[idx-1]
            controls[0] = idx-1
        return state,controls

    def right(self,state,controls):
        if controls[0]!=7:
            idx = controls[0]
            state[idx],state[idx+1] = state[idx+1],state[idx]
            controls[0] = idx+1
        return state,controls
    def middle(self,state,controls):
        idx = controls[0]
        if idx<4:
            begin  = state[0:2*idx+1]
            begin  = [4-s for s in begin]
            begin.reverse()
            state = begin + state[2*idx+1:]
        else :
            end = state[2*idx-7:]
            end = [4-s for s in end]
            end.reverse()
            state  = state[0:2*idx-7] + end
        state[idx] = 0
        return state,controls

if __name__ == '__main__':
    b = mySolution()
    step = b.init_step
    def render(step):
        res = ""
        for s in step.state:
            if s==0:
                res+='O'
            if s==1:
                res+='<'
            if s==2:
                res+='|'
            if s==3:
                res+='>'
        print(res)
    render(step)
    step = b.move(step,'r')
    render(step)
    step = b.move(step,'r')
    render(step)
    step = b.move(step,'lll')
    render(step)
    step = b.move(step,'m')
    render(step)

    c = mySolution()
    step = c.move(c.init_step,'lllmrrmrmrrm')
    render(step)
    d = mySolution()
    step = d.move(c.init_step,'lllmrrrmrmrm') # this should be a right answer but it wasn't 
    render(step)

    
    a = mySolution()
    print(a.run(20))