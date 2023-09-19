import queue,itertools,time
from  multiprocessing import Pool

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

class State:
    def __init__(self,info = {},path = []) -> None:
        self.info = info
        self.path = path

class NewSolution:
    def __init__(self,init =[],dest =[],controls = []) -> None:
        init_state = State({'state':init,'controls':controls})
        self.states = queue.Queue()
        self.states.put(init_state)
        self.dest = dest
        pass
    def left(self,info)->{}:
        pass
    def middle(self,info)->{}:
        pass
    def right(self,info)->{}:
        pass
    def judge(self,state)->bool:
        if state.info['state'] == self.dest:
            print(state.path)
            return True
        return False
    def move(self,state:State,action)->State:
        if action =='l':
            new_info = self.left(state.info)
        if action =='m':
            new_info = self.middle(state.info)
        if action =='r':
            new_info = self.right(state.info)
        return State(new_info,state.path+[action])
        
        
    def run(self,k):
        for _len in range(k):
            print("start k = ",_len)
            cnt=0
            while(not self.states.empty()):
                cnt+=1
                state = self.states.get()
                if len(state.path)>_len:
                    break
                if self.judge(state):
                    break
                for action in ('l','m','r'):
                    new_state = self.move(state,action)
                    self.states.put(new_state)
            print("finish k = ",_len+1," cnt = ",cnt)

