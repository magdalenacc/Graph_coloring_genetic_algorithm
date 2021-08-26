def elite_selection_model(generation):
    max_selected = int(len(generation)/10)
    sorted_by_assess = sorted(generation, key = lambda x: x.fitness)
    return sorted_by_assess[:max_selected]
