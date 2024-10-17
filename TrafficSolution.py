import networkx as nx
import dimod
from dwave.system import DWaveSampler, EmbeddingComposite
from dwave.samplers import SimulatedAnnealingSampler

graph = nx.DiGraph()
graph.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])  

n_intersections = len(graph.nodes)
n_modes = 6  

num_cars = {
    0: 20,  
    1: 15,  
    2: 30,  
    3: 10   
}

# Penalty for activating more than one mode at an intersection
penalty_for_multiple_modes = 100  
# Penalty for conflicting signals between connected intersections
penalty_for_conflicting_signals = 100  

# Conflict matrix defines which modes should not be active simultaneously across adjacent intersections
conflict_matrix = {
    0: [2, 5],  
    1: [4, 3],  
    2: [0, 4],  
    3: [1, 5], 
    4: [1, 2], 
    5: [0, 3]   
}

bqm = dimod.BinaryQuadraticModel('BINARY')

for i in range(n_intersections):
    for j1 in range(n_modes):
        weight = -num_cars[i]  # Prioritize intersections with more cars by reducing penalty
        bqm.add_variable(f'x_{i}_{j1}', weight)  
        
        # Preventing multiple modes at a single intersection
        for j2 in range(j1 + 1, n_modes):
            bqm.add_interaction(f'x_{i}_{j1}', f'x_{i}_{j2}', penalty_for_multiple_modes)

#checking for conflicting modes
for u, v in graph.edges:
    for mode_u in range(n_modes):
        for mode_v in conflict_matrix.get(mode_u, []):  
            bqm.add_interaction(f'x_{u}_{mode_u}', f'x_{v}_{mode_v}', penalty_for_conflicting_signals)

use_quantum_annealer = True

if use_quantum_annealer:
    sampler = EmbeddingComposite(DWaveSampler())
else:
    sampler = SimulatedAnnealingSampler()

sampleset = sampler.sample(bqm, num_reads=100)

best_solution = sampleset.first.sample
print(f"Best solution: {best_solution}")
print(f"Energy: {sampleset.first.energy}")

for i in range(n_intersections):
    for j in range(n_modes):
        if best_solution[f'x_{i}_{j}'] == 1:
            print(f"Intersection {i} is in mode {j} (green signal)")
