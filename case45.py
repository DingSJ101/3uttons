from base import NewSolution
from game.base import Step
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [0,1,1,0,0,1,1,0,0,1,0,1,1,0]
        # init = [1,1,1,1,1,1,1,0,0,0,0,0,0,0]
        # init = [0,0,0,0,0,0,0,1,1,1,1,1,1,1]
        dest = [] 
        controls = [4]
        super().__init__(init,dest,controls)

    def judge(self, step: Step) -> bool:
        if sum(step.state[:7]) == 0 or sum(step.state[:7]) == 7:
            print(step.path)
            return True
        return False
    def left(self,state,controls):
        state = [state[6]]+state[0:6]+state[7:]
        return state,controls

    def right(self,state,controls):
        state = state[:7]+[state[-1]]+state[7:-1]
        return state,controls
    def middle(self,state,controls):
        state[1],state[8] = state[8],state[1]
        state[2],state[9] = state[9],state[2]
        state[3],state[10] = state[10],state[3]
        state[4],state[11] = state[11],state[4]
        state[5],state[12] = state[12],state[5]
        return state,controls

if __name__ == '__main__':
    b = mySolution()
    step = b.init_step
    def render(step):
        res = ""
        print(step.state[:7])
        print(step.state[7:])
        print()
    render(step)
    # step = b.move(step,'rrrrlllrmrmrm')
    # render(step)
    # step = b.move(step,'llllm')
    # render(step)
    c = mySolution()
    step = c.init_step
    for s in 'rrrrlllrmrmrm':
        step = c.move(step,s)
        render(step)
    a = mySolution()
    print(a.run(20))