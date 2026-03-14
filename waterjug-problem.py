
def dfs(a,b,target):
    stack=[(0,0)]
    visited=set()
    while stack:
        x,y=stack.pop()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        print(x,y)
        if x==target or y==target:
            print("target achieved")
            return
        next_state=[]
        next_state.append((a,y))
        next_state.append((x,b))
        next_state.append((0,y))
        next_state.append((x,0))

        pour=min(x,b-y)
        next_state.append((x-pour,y+pour))
        pour=min(y,a-x)
        next_state.append((x+pour,y-pour))

        for state in next_state:
            if state not in visited:
                stack.append(state)
    print("NO target")

a=int(input("enter the first jug:"))
b=int(input("enter the second jug:"))
target=int(input("enter the target:"))

dfs(a,b,target)
