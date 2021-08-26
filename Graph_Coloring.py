from Element import Element
from random import randint

class Graph_Coloring(Element):

    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        super().__init__()

    def _perform_mutation(self):
        first = randint(1, len(self.colors)-2)
        seconds = randint(1, len(self.colors)-2)

        self.colors[first], self.colors[seconds] = self.colors[seconds], self.colors[first]

    def crossover(self, element2: 'Element') -> 'Element':
        length = int(randint(0, len(self.colors)-1))
        new_color = self.colors[:length] + element2.colors[length:]

        return Graph_Coloring(self.graph, new_color)


    def evaluate_function(self):
        violations = 0
        for i in self.graph.edges:
            if self.colors[i[0]] == self.colors[i[1]]:
                violations += 1

        if violations > 0:
            return violations, len(set(self.colors))
        else:
            return len(set(self.colors)), violations


    def __repr__(self):
        return str(self.colors)


