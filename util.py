class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"Item(name={self.name}, weight={self.weight}, value={self.value})"

    def __repr__(self):
        return self.__str__()

class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.dp = [] 

    def add_item(self, item):
        self.items.append(item)

    def add_all_items(self, itens):
        for item in itens:
            self.add_item(item)

    def solve(self):
        n = len(self.items)
        self.dp = [[0 for _ in range(self.capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, self.capacity + 1):
                if self.items[i - 1].weight <= w:
                    self.dp[i][w] = max(self.dp[i - 1][w], self.dp[i - 1][w - self.items[i - 1].weight] + self.items[i - 1].value)
                else:
                    self.dp[i][w] = self.dp[i - 1][w]

        return self.dp[n][self.capacity]

    def find_solution(self):
        solution = []
        self.solve()
        w = self.capacity
        n = len(self.items)

        for i in range(n, 0, -1):
            if w <= 0:
                break  

            if self.dp[i][w] != self.dp[i-1][w]:  
                solution.append(self.items[i-1])
                w -= self.items[i-1].weight  

        return solution
