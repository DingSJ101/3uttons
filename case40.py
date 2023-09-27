from base import NewSolution
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [0,0,0,1,1,1,0,0,0]
        dest = [1,1,1,1,1,1,1,1,1] 
        controls = [4]
        super().__init__(init,dest,controls)
    def left(self,state,controls):
        state[0:3] = [state[2]]+state[0:2]
        state[3:6] = [state[5]]+state[3:5]
        state[6:9] = [state[8]]+state[6:8]
        return state,controls

    def right(self,state,controls):
        first_line = state[0:3]
        state = state[3:9]+first_line
        return state,controls
    def middle(self,state,controls):
        state[3] = 1-state[3]
        state[5] = 1-state[5]
        state[7] = 1-state[7]
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