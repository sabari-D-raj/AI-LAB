import random

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
def path_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost += dist[path[i]][path[i+1]]
    cost += dist[path[-1]][path[0]]
    return cost
def get_neighbors(path):
    neighbors = []
    for i in range(len(path)):
        for j in range(i+1, len(path)):
            new_path = path[:]
            new_path[i], new_path[j] = new_path[j], new_path[i]
            neighbors.append(new_path)
    return neighbors
def hill_climbing():
    current = list(range(n))
    random.shuffle(current)

    current_cost = path_cost(current)

    while True:
        neighbors = get_neighbors(current)

        best_neighbor = current
        best_cost = current_cost

        for neighbor in neighbors:
            cost = path_cost(neighbor)
            if cost < best_cost:
                best_neighbor = neighbor
                best_cost = cost

        if best_cost >= current_cost:
            break

        current = best_neighbor
        current_cost = best_cost

    return current, current_cost


solution, cost = hill_climbing()

print("Best Tour:", solution)
print("Minimum Cost:", cost)