from base import NewSolution
class mySolution(NewSolution):
    def __init__(self) -> None:
        init = [0,4,7,2,
                0,0,0,3,5,8,
                0,0,1,9,6]
        # init = [1,1,1,1,1,1,1,0,0,0,0,0,0,0]
        # init = [0,0,0,0,0,0,0,1,1,1,1,1,1,1]
        dest = [0,1,2,3,
                0,0,0,4,5,6,
                0,0,7,8,9] 
        controls = [0,-1,(1,0,0,0,3,0,2,0,0,0,1,0,0,0,0)] # selected block counts,last button,colors(0:all,1:l;2:m;3:r)
        self.maps = [0,1,1,1,2,2,2,3,3,3] # maps[block] = color
        self.dims = [4,6,5]
        super().__init__(init,dest,controls)

    from typing import Tuple

    def countBlocks(self,state)->Tuple[int]:
        def count(state:list): # count blocks in a column
            cnt = 0
            for s in state:
                if s!=0:cnt+=1
            return cnt
        i1 = self.dims[0]
        i2 = sum(self.dims[:2])
        return count(state[:i1]),count(state[i1:i2]),count(state[i2:])
    
    def isSatisfied(self,state,controls)->bool:
        for i in range(len(self.dest)):
            if  controls[2][i] == 0 or self.maps[state[i]]==0 :continue
            if self.maps[state[i]] != controls[2][i]: return False
        return True
    
    def left(self,state,controls):
        destCol = 0
        selectBlocks,col =  controls[0],controls[1]
        cntBlocks = self.countBlocks(state)[destCol]
        restBlocks = self.dims[destCol]-cntBlocks

        if controls[1] == destCol :
            if controls[0]<cntBlocks:
                controls[0] += 1
        elif controls[1] == -1:
            if 0<cntBlocks:
                controls[0]+=1
                controls[1]=destCol
        else:
            originIndex = sum(self.dims[:col+1]) - self.countBlocks(state)[col]
            destIndex = sum(self.dims[:destCol]) + restBlocks -selectBlocks
            if restBlocks >= selectBlocks:   
                newState = state.copy()
                newState[destIndex:destIndex+selectBlocks] = state[originIndex:originIndex+selectBlocks]
                newState[originIndex:originIndex+selectBlocks] = [0]*selectBlocks
                if self.isSatisfied(newState,controls):
                    state = newState
                    controls[1] = -1
                    controls[0] = 0
        return state,controls

    def right(self,state,controls):
        destCol = 2
        selectBlocks,col =  controls[0],controls[1]
        cntBlocks = self.countBlocks(state)[destCol]
        restBlocks = self.dims[destCol]-cntBlocks

        if controls[1] == destCol :
            if controls[0]<cntBlocks:
                controls[0] += 1
        elif controls[1] == -1:
            if 0<cntBlocks:
                controls[0]+=1
                controls[1]=destCol
        else:
            originIndex = sum(self.dims[:col+1]) - self.countBlocks(state)[col]
            destIndex = sum(self.dims[:destCol]) + restBlocks -selectBlocks
            if restBlocks >= selectBlocks:   
                newState = state.copy()
                newState[destIndex:destIndex+selectBlocks] = state[originIndex:originIndex+selectBlocks]
                newState[originIndex:originIndex+selectBlocks] = [0]*selectBlocks
                if self.isSatisfied(newState,controls):
                    state = newState
                    controls[1] = -1
                    controls[0] = 0
        return state,controls
    
    def middle(self,state,controls):
        destCol = 1
        selectBlocks,col =  controls[0],controls[1]
        cntBlocks = self.countBlocks(state)[destCol]
        restBlocks = self.dims[destCol]-cntBlocks

        if controls[1] == destCol :
            if controls[0]<cntBlocks:
                controls[0] += 1
        elif controls[1] == -1:
            if 0<cntBlocks:
                controls[0]+=1
                controls[1]=destCol
        else:
            originIndex = sum(self.dims[:col+1]) - self.countBlocks(state)[col]
            destIndex = sum(self.dims[:destCol]) + restBlocks -selectBlocks
            if restBlocks >= selectBlocks:   
                newState = state.copy()
                newState[destIndex:destIndex+selectBlocks] = state[originIndex:originIndex+selectBlocks]
                newState[originIndex:originIndex+selectBlocks] = [0]*selectBlocks
                if self.isSatisfied(newState,controls):
                    state = newState
                    controls[1] = -1
                    controls[0] = 0
        return state,controls

if __name__ == '__main__':
    b = mySolution()
    step = b.init_step
    def render(step):
        s_list = list(step.state)
        s = [-1,-1]+s_list[0:10]+[-1]+s_list[10:]
        print(s)
        cases = ['︿','■■','﹀']
        res = ""
        col = 6
        for i in range(col):
            l,m,r = s[i],s[col+i],s[col*2+i]
            for _ in (l,m,r):
                if _ == -1 :res += '  '
                elif _ == 0 :res += '——'
                elif _<4 : res += '\033[033m'+cases[_-1]+'\033[0m'
                elif _<7 : res += '\033[031m'+cases[_-4]+'\033[0m'
                else : res += '\033[032m'+cases[_-7]+'\033[0m'
            res+='\n'
        print(res)
    render(step)
    render(b.move(step,'lm'))
    render(b.move(step,'rlmmmrrrrrrmmmmmrrrmllmlrlrmrmmllmrrl'))
    # step = b.move(step,'llllm')
    # render(step)
    c = mySolution()
    step = c.init_step
    # for s in 'lllmmmrrrrrl':
    #     step = c.move(step,s)
    #     render(step)
    a = mySolution()
    print(a.run(37)) # 37
    # [
    # 'r', 'l', 'm', 'm', 'm', 
    # 'r', 'r', 'r', 'r', 'r', 
    # 'r', 'm', 'm', 'm', 'm', 
    # 'm', 'r', 'r', 'r', 'm', 
    # 'l', 'l', 'm', 'l', 'r', 
    # 'l', 'r', 'm', 'r', 'm', 
    # 'm', 'l', 'l', 'm', 'r', 
    # 'r', 'l']