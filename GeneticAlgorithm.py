from random import random, choice

class GeneticAlgorithm:
    def __init__(self, first_population_generator: callable,
                 population_size,
                 start_color_counts,
                 selection_model: callable,
                 stop_condition: callable,
                 mutation_probability: float = 0.1,
                 crossover_probability: float = 0.1):
        self.first_generation_func = first_population_generator
        self.population_size = population_size
        self.start_color_counts = start_color_counts
        self.selection_model = selection_model
        self.stop_condition = stop_condition
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability

    def run(self):
        population = self.first_generation_func(self.population_size, self.start_color_counts)
        print(population)
        population.sort(key = lambda x : x.fitness)
        print(population)
        population_len = len(population)
        i = 0
        while True:
            selected = self.selection_model(population)
            new_population = selected.copy()
            while len(new_population) != population_len:
                if random() <= self.crossover_probability:
                    child = choice(population).crossover(choice(population))
                else:
                    child = choice(population)
                if random() <= self.mutation_probability:
                    child.mutation()
                new_population.append(child)

            population = new_population
            print("new population: ", population)
            the_best_match = min(population, key = lambda x: x.fitness)
            print("Generation: {} S: {} \nfitness: {}\ncolors: {}".format(i, the_best_match.colors, the_best_match.fitness[0], the_best_match.fitness[1]))
            i += 1
            text = 'started_colors_count:',  self.start_color_counts , 'population_size:' , self.population_size , 'mutation_probability:' , \
                   self.mutation_probability , 'crossover_probability:', self.crossover_probability

            if self.stop_condition(the_best_match, the_best_match.fitness, i, the_best_match.colors, text):
                break
        return the_best_match.fitness[0], the_best_match.fitness[1]
