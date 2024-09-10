class Item:
    def __init__(self, name, weight, value):
        self.name = name     # name
        self.weight = weight # time
        self.value = value   # rate

class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.memorization = [] 

    def add_items(self, itens):
        for item in itens:
            self.items.append(item)

    def solve(self):
        n = len(self.items)

        # Inicializando a matriz de memorizacao
        self.memorization = [[0 for _ in range(self.capacity + 1)] for _ in range(n + 1)]

        # Preenche iterativamente o "meio" da matriz
        for i in range(1, n + 1):
            for w in range(1, self.capacity + 1):
                # Verifica se ainda cabe na mochila 
                if self.items[i - 1].weight <= w:
                    self.memorization[i][w] = max(self.memorization[i - 1][w], self.memorization[i - 1][w - self.items[i - 1].weight] + self.items[i - 1].value)
                else:
                    self.memorization[i][w] = self.memorization[i - 1][w]

        return self.memorization[n][self.capacity]

    def find_solution(self):
        solution = []
        self.solve()
        w = self.capacity
        n = len(self.items)
        
        for i in range(n, 0, -1):
            # Encheu a mochila
            if w <= 0:
                break

            if self.memorization[i][w] != self.memorization[i-1][w]:
                solution.append(self.items[i-1]) # Adiciona na solucao o item levado
                w -= self.items[i-1].weight

        return solution
