from base import NewSolution, Step
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [3,3]
        dest = [] 
        controls = [1,0,0,0]#location state,target states
        self.targets = [4,0,2,3,1,6]
        self.locations = [3,2,3,3,3,4]
        super().__init__(init,dest,controls)
    def judge(self, step: Step) -> bool:
        if sum(step.controls[1:]) == (len(step.controls)-1):
            print(step.path)
            return True
        return False
    def left(self,state,controls):
        controls[0] = (2 + controls[0] )%3
        return state,controls

    def right(self,state,controls):
        controls[0] = (1+controls[0]) %3
        return state,controls
    def middle(self,state,controls):
        len_target = len(self.targets)//2
        idx = controls[0]
        x , y = self.locations[idx*2],self.locations[idx*2+1]
        xx,yy = state
        state = [x+yy-y,y-xx+x]
        if state == [0,3]:
            state = [1,3]
        if state == [5,3]:
            state = [4,3]
        xx,yy = state
        for i in range(len_target):
            if xx == self.targets[2*i] and yy == self.targets[2*i+1]:
                controls[1+i] = 1
        return state,controls

if __name__ == '__main__':
    def render(step):
        print(step.state,step.controls,step.path)

    b = mySolution()
    step = b.init_step
    render(step)
    step = b.move(step,'lmrmmlm')
    render(step)
    step = b.move(step,'mmm')
    render(step)
    step = b.move(step,'m')
    render(step)
    step = b.move(b.init_step,'lmrrmlmmrmmlmmmlmm')
    print(b.judge(step))
    render(step)
    step = b.move(b.init_step,'r')
    render(step)
    step = b.move(b.init_step,'lll')
    render(step)
    step = b.move(b.init_step,'m')
    render(step)

    # c = mySolution()
    # step = c.move(c.init_step,'rrmlmlllmlmrrrmrr')
    # render(step)

    
    a = mySolution()
    print(a.run(21))
    # ['l', 'm', 'l', 'm', 'm', 'l', 'm', 'm', 'l', 'm', 'm', 'm', 'l', 'm', 'l', 'm', 'l', 'm', 'l', 'm', 'm']