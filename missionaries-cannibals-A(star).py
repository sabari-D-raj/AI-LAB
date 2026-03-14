import heapq

start=(3,3,1)
goal=(0,0,0)
moves=[(1,0),(2,0),(0,1),(0,2),(1,1)]

def valid(m,c):
    if m<0 or c<0 or m>3 or c>3:
        return False
    if m>0 and c>m:
        return False
    if (3-m)>0 and (3-c)>(3-m):
        return False
    return True
def heuristic_state(state):
    m,c,_=state
    return (m+c)//2
def astar():
    pq=[]
    heapq.heappush(pq,(0,start,[]))
    visited=set()
    while pq:
        f,state,path=heapq.heappop(pq)
        if state in visited:
            continue
        visited.add(state)
        path=path+[state]
        if state==goal:
            return path
        m,c,boat=state

        for dm,dc in moves:
            if boat==1:
                new=(m-dm,c-dc,0)
            else:
                new=(m+dm,c+dc,1)
            if valid(new[0],new[1]):
                g=len(path)
                h=heuristic_state(new)
                heapq.heappush(pq,(g+h,new,path))
    return None

solution=astar()
for step in solution:
    print(step)

    
