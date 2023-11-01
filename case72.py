from base import NewSolution,queue
from base import Step
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [1,6,4,3,8,5,2,7]
        dest = [5,6,7,8,1,2,3,4] 
        controls = []
        super().__init__(init,dest,controls)


    def left(self,state,controls):
        state = state[1:4]+[state[0]]+state[4:]
        return state,controls

    def right(self,state,controls):
        state = state[0:4]+state[5:]+[state[4]]
        return state,controls
    def middle(self,state,controls):
        state[2],state[6],state[1],state[5] = state[6],state[2] ,state[5],state[1]
        return state,controls

if __name__ == '__main__':
    # def rander(step):
    #     state = step.state
    #     solution =  mySolution()
    #     maps =solution.maps
    #     for i in range(len(state)): # draw points
    #         if i%2 !=0 :continue
    #         x,y = state[i:i+2]
    #         maps[x][y] = ' O '
    #     for i in range(len(solution.dest)): # draw targets
    #         if i%2 !=0 :continue
    #         x,y = solution.dest[i:i+2]
    #         if maps[x][y] == ' O ':
    #             maps[x][y] = ' ■ '
    #         else:
    #             maps[x][y] = ' □ '
    #     for i in range(len(maps)): # draw maps
    #         for j in range(len(maps[0])):
    #             ch = maps[i][j]
    #             if ch == 1:
    #                 print(' · ',end="")
    #             elif ch==0:
    #                 print('   ',end="")
    #             else :
    #                 print(ch,end='')
    #         print()
    #     print()
    # d = mySolution()
    # step = d.init_step
    # rander(step)
    # # rander(d.move(step,'r'))
    # # rander(d.move(step,'l'))
    # # rander(d.move(step,'m'))

    # # rander(d.move(step,'mmmmmmmmmmmmmmmmmmmm'))
    # # rander(d.move(step,'lmmlmmlmrr'))
    # # rander(d.move(step,'lmmlmmlmrrrmllmmmml'))
    
    # e = mySolution()
    # step = e.init_step
    # path = 'lmmlmmlmrrrmllmmmml'
    # for s in path :
    #     step = e.move(step,s)
    #     rander(step)

    a = mySolution()
    a.run(11)
    # ['m', 'l', 'm', 'l', 'm', 'r', 'r', 'm', 'l', 'l', 'l']
