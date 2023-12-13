class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def min_operations_to_connect_cities(n, routes):
    """
    Find the minimum number of operations required to connect all cities in the network.

    Parameters:
    n (int): The number of cities.
    routes (list): List of connections between cities.

    Returns:
    int: The minimum number of operations to connect all cities, or -1 if not possible.
    """
    uf = UnionFind(n)

    # Count the number of successfully unioned pairs (i.e., unique connections)
    connected = sum(uf.union(city1, city2) for city1, city2 in routes)

    # Count the number of unique roots (i.e., connected components)
    components = len(set(uf.find(city) for city in range(n)))

    # We need (components - 1) operations to connect all components
    return components - 1

# User input handling
if __name__ == "__main__":
    n_input = int(input("Enter the number of cities: "))
    route_count = int(input("Enter the number of routes: "))

    routes_input = []
    for _ in range(route_count):
        route = list(map(int, input().split()))
        routes_input.append(route)

    result = min_operations_to_connect_cities(n_input, routes_input)
    print("Minimum operations to connect all cities:", result)

