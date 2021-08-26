from time import perf_counter
from GeneticAlgorithm import GeneticAlgorithm
from Graph_Coloring import Graph_Coloring
from selection_models import elite_selection_model
from random import randint, choice, sample, randrange
import matplotlib.pyplot as plt

import networkx as nx
import numpy as np
import pandas as pd
import os
TARGET = 'Czesc, tu Magda :D'

count_nodes = 10
count_edges = 15
started_colors_count = 3
population_size = 10
mutation_probability = 0.9
crossover_probability = 0.1
iteration_size = 10
def plotGraph(G, colorArrangement, fig, text):

    if len(colorArrangement) != len(G.graph):
        raise ValueError("size of color list should be equal to ", len(G.graph))

    # create a list of the unique colors in the arrangement:
    colorList = list(set(colorArrangement))

    # create the actual colors for the integers in the color list:
    colors = plt.cm.rainbow(np.linspace(0, 1, len(colorList)))

    # iterate over the nodes, and give each one of them its corresponding color:
    colorMap = []
    for i in range(len(G.graph)):
        color = colors[colorList.index(colorArrangement[i])]
        colorMap.append(color)

    # plot the nodes with their labels and matching colors:
    # fig.clear()

    fig.canvas.set_window_title(text)
    nx.draw_kamada_kawai(G.graph, node_color=colorMap, with_labels=True)
    #plt.title(text, fontsize=20)
    # nx.draw_circular(self.graph, node_color=color_map, with_labels=True)
    # fig.canvas.flush_events()
    return plt





def first_generation_generator(population_size, started_colors_count):
    G = nx.petersen_graph()

    return [Graph_Coloring(G, [(randint(0, started_colors_count)) for k in range(count_nodes)]) for _ in
            range(population_size)]

fig = plt.figure(figsize=(30, 10))


def stop_condition(graph, current_fitness, i, colors, text):
    fig.clear()
    plotGraph(graph, colors, fig, text)

    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.show(block=False)
    return i == iteration_size


results = pd.DataFrame(columns=['i', 'started_colors_count', 'population_size', 'mutation_probability', 'crossover_probability',
                                'fitness', 'n_colors', 'time'])


for scc in range(5, 51,5): #start color counts
    for ps in range(100, 501, 50):    #population size
        for mp in np.arange(0.1, 1.0, 0.2): #mutation_probability
            for cp in np.arange(0.1, 1.0, 0.2): #crossover_probability
                for i in range(1, 100):
                    print('############################', i)
                    print('----------------------------', scc)
                    print('++++++++++++++++++++++++++++', ps)
                    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<', mp)
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>', cp)
                    start = perf_counter()
                    ga = GeneticAlgorithm(first_generation_generator, ps, scc, elite_selection_model, stop_condition,
                                          mutation_probability=mutation_probability, crossover_probability=crossover_probability)

                    result = ga.run()
                    end = perf_counter()
                    delta_time = round((end-start),2)
                    print(delta_time)
                    new_row = {'i':i,
                               'started_colors_count':scc, 'population_size':ps, 'mutation_probability':mutation_probability,
                               'crossover_probability':crossover_probability, 'fitness':result[0], 'n_colors':result[1], 'time':delta_time}
                    results = results.append(new_row, ignore_index=True)

print(results)



