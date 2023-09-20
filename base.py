import queue,itertools,time
from  multiprocessing import Pool
from typing import List,Tuple,Dict,Union

class task:
    def __init__(self) -> None:
        self.params = {}
        self.init()
    def init(self):
        pass
    def left(self):
        pass
    def middle(self):
        pass
    def right(self):
        pass
    def judge(self):
        return False
    
    def run(self,k):
        for len in range(k):
            print("[============          start  k = %-2d           ============]"%(len + 1))
            iter = itertools.product(('l','m','r'),repeat=len)
            cnt=0
            for l in iter:
                cnt+=1
                for action in l:
                    if action =='l':
                        self.left()
                    if action =='m':
                        self.middle()
                    if action =='r':
                        self.right()
                if self.judge():
                    return l
            # print("[--   finish k = ",len," cnt = ",cnt,"   --]\n")
            print("[============   finish k = %-2d,cnt = %-10d ============]\n"%(len + 1,cnt))

class BaseTask:
    def __init__(self) -> None:
        self.params = {}
        self.init()
    def init(self):
        self.params['m1'] = 0
    
    def left(self):
        pass
    def middle(self):
        pass
    def right(self):
        pass
    def judge(self):
        return False
    
    def simulate(self,actions):
        self.init()
        for action in actions:
            if action =='l':
                self.left()
            if action =='m':
                self.middle()
            if action =='r':
                self.right()
        return self.judge()



class Solution:
    def __init__(self,taskClass) -> None:
        self.taskClass = taskClass
    def run(self,k):
        task = self.taskClass()
        for len in range(k):
            print("start k = ",len)
            iter = itertools.product(('l','m','r'),repeat=len)
            cnt=0
            for l in iter:
                cnt+=1
                if task.simulate(l):
                    return l
            print("finish k = ",len," cnt = ",cnt)

    # 重构run函数，使用多进程
    def run_with_processes(self,k):
        processes_count = 20
        def callback(result):
            print("in callback",result)
            # processes_count += 1
        for len in range(k):
            pool = Pool(processes_count)
            print("[============          start  k = %-2d           ============]"%(len + 1))
            start_time = time.time()
            iter = itertools.product(('l','m','r'),repeat=len)
            cnt = 0
            while(True):
                if processes_count:
                    try:
                        l = next(iter)
                        cnt +=1
                        task = self.taskClass()
                        pool.apply_async(task.simulate,args=(l,))
                    except StopIteration as e:
                        break
                    # processes_count -= 1
                else:
                    time.sleep(0.1)
            pool.close()
            pool.join()
            end_time = time.time()
            time_used = end_time - start_time
            print("[============   time = %-5fs,cnt = %-10d ============]\n"%(round(time_used,3),cnt))

class Step:
    def __init__(self,info = {'state':Union[Tuple,List],'controls':Union[Tuple,List]},path = []) -> None:
        if info == None:
            info = {'state':(),'controls':()}
        if isinstance(info['state'],list):
            info['state'] = tuple(info['state'])
        if isinstance(info['controls'],list):
            info['controls'] = tuple(info['controls'])
        self.info = info
        self.path = path
        self.__setattr__('state',self.info['state'])
        self.__setattr__('controls',self.info['controls'])
    def __eq__(self, other):
        return isinstance(other, Step) and self.info == other.info 

    def __hash__(self):
        # 使用info和path的哈希值来计算这个对象的哈希值
        return hash((frozenset(self.info.items())))
    

class NewSolution:
    def __init__(self,init_state =(),dest_state =(),controls = ()) -> None:
        if isinstance(dest_state,list):
            dest_state = tuple(dest_state)
        self.states:queue.Queue[Step] = queue.Queue()
        self.dest = dest_state
        self.map:Dict[Step,list] = {} # record the state
        self.addNewStep(init_state,controls)
        
        pass
    def addNewStep(self,state:Union[Tuple,List],controls:Union[Tuple,List],path=[]):
        newStep  = Step({'state':state,'controls':controls},path)
        if newStep not in self.map \
            or len(newStep.path) < len(self.map[newStep]):
            self.map[newStep] = newStep.path
            self.states.put(newStep)
        return newStep
        
    def left(self,state:List,controls:List)->Tuple[List,List]:
        state[0]+=1
        return state,controls
    def middle(self,state:List,controls:List)->Tuple[List,List]:
        state[1]+=1
        return state,controls
    def right(self,state:List,controls:List)->Tuple[List,List]:
        state[2]+=1
        return state,controls
    
    def judge(self,step:Step)->bool:
        if step.info['state'] == self.dest:
            print(step.path)
            return True
        return False
    
    def move(self,step:Step,actions:str)->Step:
        state = list(step.info['state'])
        controls = list(step.info['controls'])
        for action in actions:
            if action =='l':
                state,controls = self.left(state,controls)
            if action =='m':
                state,controls = self.middle(state,controls)
            if action =='r':
                state,controls = self.right(state,controls)
            step =  self.addNewStep(state,controls,step.path+[action])
        return step
    def run(self,k):
        length = 0
        cnt=0
        print("[============          start  k = %-2d           ============]"%(length))
        while(not self.states.empty()):
            cnt+=1
            step = self.states.get()
            if len(step.path)>length:
                print("[============   finish k = %-2d,cnt = %-10d ============]\n"%(length,cnt))
                length = len(step.path)
                print("[============          start  k = %-2d           ============]"%(length))
                cnt = 0
            if len(step.path)>k:
                break
            if self.judge(step):
                continue
            for action in ('l','m','r'):
                self.move(step,action)
        print("[============   finish k = %-2d,cnt = %-10d ============]\n"%(length,cnt))


if __name__ == "__main__":
    a = Step({'state':[1,2,3,4,5,6],'controls':[0,2]})
    b = Step({'controls':[0,2],'state':[1,2,3,4,5,6]})
    # print(a==b)
    # print(hash(a))
    # print(hash(b))
    # print(hash(a)==hash(b))
    # print(a.state)
    d = NewSolution([1,2,3,4,5,6,7],(1,2,3,4,5,6,7),[0,0,0])
    d.run(1)
    e = NewSolution((1,2,3,4,5,6),[1,2,3,4,5,6],[1,2,3])
    e.run(1)
    f = NewSolution((1,2,3,4,5,6),[2,4,3,4,5,6],[1,2,3])
    f.run(4)