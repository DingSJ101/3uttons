from base import NewSolution
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [5,2,8,1,9,4,3,6,7]
        dest = [1,2,3,4,5,6,7,8,9]
        controls = []
        super().__init__(init,dest,controls)
    def left(self,state,controls):
        state = state[1:-1]+[state[0]]+[state[-1]]
        return state,controls
    def right(self,state,controls):
        state = [state[-2]]+state[0:-2]+[state[-1]]
        return state,controls
    def middle(self,state,controls):
        _state = state.copy()
        state = [_state[1]]+[_state[2]]+[_state[0]]\
                +[_state[7]]+[_state[6]]+[_state[4]]\
                +[_state[5]]+[_state[8]]+[_state[3]]
        return state,controls

if __name__ == '__main__':
    
    a = mySolution()
    print(a.run(17))