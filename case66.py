from base import NewSolution,queue
from base import Step
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [2,0,8,2,2,6,6,8]
        dest = [0,0,8,0,4,4,6,8] 
        controls = [1,1,1,1] # 1:up, -1:down
        self.maps = [[1,1,1,1,1,0,0,0,0],
                     [1,0,0,0,1,0,0,0,0],
                     [1,0,0,0,1,1,1,0,0],
                     [1,0,0,0,1,0,1,0,0],
                     [1,1,1,1,1,1,1,1,1],
                     [1,0,0,0,1,0,0,0,1],
                     [1,0,0,0,1,0,0,0,1],
                     [1,0,0,0,1,0,0,0,1],
                     [1,1,1,1,1,1,1,1,1],
                     ]
        super().__init__(init,dest,controls)

        
    def judge(self, step: Step) -> bool:
        def eq(x1,y1,x2,y2):
            return x1==x2 and y1==y2
        state = self.dest
        target = step.state
        flag = len(state)//2
        while(len(state)):
            x,y,*state= state
            for i in range(len(target)):
                if i%2 !=0 :continue
                x2,y2 = target[i:i+2]
                if eq(x,y,x2,y2):
                    flag -= 1
                    break
        if flag :
            return False
        else:
            print(step.path)
            return True

    def left(self,state,controls):
        for i in range(len(state)):
            if i%2 !=0 :continue
            x,y = state[i:i+2]
            if y-2 >=0 and self.maps[x][y-2] == 1 and self.maps[x][y-1] == 1 :
                state[i:i+2] = x,y-2
        return state,controls

    def right(self,state,controls):
        for i in range(len(state)):
            if i%2 !=0 :continue
            x,y = state[i:i+2]
            if y+2 <len(self.maps[0]) and self.maps[x][y+2] == 1 and self.maps[x][y+1] == 1:
                state[i:i+2] = x,y+2
        return state,controls
    def middle(self,state,controls):
        for i in range(len(state)):
            if i%2 !=0 :continue
            x,y = state[i:i+2]
            if x+2*controls[i//2] >=0 and x+2*controls[i//2] <len(self.maps) \
                and self.maps[x+controls[i//2]][y] == 1 and self.maps[x+2*controls[i//2]][y] == 1:
                state[i:i+2] = x+2*controls[i//2],y
            else :
                controls[i//2] = 0-controls[i//2]
                if x+2*controls[i//2] >=0 and x+2*controls[i//2] <len(self.maps) \
                and self.maps[x+controls[i//2]][y] == 1 and self.maps[x+2*controls[i//2]][y] == 1:
                    state[i:i+2] = x+2*controls[i//2],y

        return state,controls

if __name__ == '__main__':
    # b= mySolution()
    # b.dest = [0,0,1,1,2,2,3,3]
    # step = b.init_step
    # step.state = [1,1,2,2,3,3,0,0]
    # print(b.judge(step))
    # step.state = [1,1,2,2,3,3,0,1]
    # print(b.judge(step))
    def rander(step):
        state = step.state
        solution =  mySolution()
        maps =solution.maps
        for i in range(len(state)): # draw points
            if i%2 !=0 :continue
            x,y = state[i:i+2]
            maps[x][y] = ' O '
        for i in range(len(solution.dest)): # draw targets
            if i%2 !=0 :continue
            x,y = solution.dest[i:i+2]
            if maps[x][y] == ' O ':
                maps[x][y] = ' ■ '
            else:
                maps[x][y] = ' □ '
        for i in range(len(maps)): # draw maps
            for j in range(len(maps[0])):
                ch = maps[i][j]
                if ch == 1:
                    print(' · ',end="")
                elif ch==0:
                    print('   ',end="")
                else :
                    print(ch,end='')
            print()
        print()
    d = mySolution()
    step = d.init_step
    rander(step)

    
    # e = mySolution()
    # step = e.init_step
    # path = 'lmlmrm'
    # for s in path :
    #     step = e.move(step,s)
    #     rander(step)
    # print(e.judge(step))

    a = mySolution()
    a.run(11)
    
    
