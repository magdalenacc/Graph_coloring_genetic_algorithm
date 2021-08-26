from abc import abstractmethod, ABC

class Element(ABC):

    def __init__(self):
        self.fitness = self.evaluate_function()

    def mutation(self):
        self._perform_mutation()
        self.fitness = self.evaluate_function()

    @abstractmethod
    def _perform_mutation(self):
        pass

    @abstractmethod
    def crossover(self, element2: 'Element') -> 'Element':
        pass

    @abstractmethod
    def evaluate_function(self):
        pass



