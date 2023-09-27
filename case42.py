from base import NewSolution
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [0,0,0,0,0,0,0,0,0]
        dest = [1,1,1,1,1,1,1,1,1] 
        controls = [4]
        super().__init__(init,dest,controls)
    def left(self,state,controls):
        q,w,e,a,s,d,z,x,c = state[:9]
        state = [e,q,w,d,a,s,z,x,c]
        return state,controls

    def right(self,state,controls):
        q,w,e,a,s,d,z,x,c = state[:9]
        state = [z,x,e,q,w,d,a,s,c]
        return state,controls
    def middle(self,state,controls):
        state[0] = 1-state[0]
        state[4] = 1-state[4]
        state[8] = 1-state[8]
        return state,controls

if __name__ == '__main__':
    b = mySolution()
    step = b.init_step
    def render(step):
        res = ""
        cnt = 0
        for s in step.state:
            cnt+=1
            if s == 0:print('X',end="")
            else :print('O',end="")
            if cnt % 3 ==0:
                print()
        print()
    render(step)
    step = b.move(step,'m')
    render(step)
    step = b.move(step,'r')
    render(step)
    a = mySolution()
    print(a.run(20))