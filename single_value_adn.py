import math
import random
import numpy as np

pop_size = 64

def fitness(x):
    #x[0] = 0 if x[0] < 0 else x[0]
    #return math.pow(x[0], math.sin(math.pow(x[0], 0.6)))
    #print(x[0])
    #f = -x[0] if -1 < x[0] < 1 else -1 * math.pow(x[0] - 2, 2) + 5
    x = x[0]
    pos1 = x if x < 5 else 0
    pos2 = x - 7.5 if 10 <= x < 20 else 0
    neg1 = -x/2 + 7.5 if 5 <= x < 10 else 0
    neg2 = -x/2 + 22.5 if x >= 20 else 0
    return pos1 + pos2 + neg1 + neg2

def get_random_agent():
    return [random.gauss(-10, .01), []]

def mutate(agent):
    # Bug: divides by zero.
    mutation_rate = 0

    if len(agent[1]):
        avg_fitness = sum([a[1] for a in agent[1]]) / len(agent[1])
        ancestors = [[np.sign(agent[0] - a[0]), a[1] - avg_fitness] for a in agent[1]]

        mutation_rate = sum([a[0] * a[1] for a in ancestors])

    #print('moy grande', mutation_rate)
    mutation = random.gauss(mutation_rate, .01)

    new_ancestors = [*agent[1], [agent[0], fitness(agent)]]
    new_agent = [agent[0] + mutation, new_ancestors]
    return new_agent

def select(agents):
    scores = [fitness(agent) for agent in agents]
    scored_agents = list(zip(agents, scores))
    survivors = []

    for agent in scored_agents:
        if agent[1] > sum(scores) / len(scores):
            survivors.append(agent[0])

    return survivors

def reproduce(agents):
    new_agents = agents

    while len(new_agents) < pop_size:
        new_agent = mutate(random.choice(agents))
        new_agents.append(new_agent)

    return new_agents

def get_avg_fitness(agents):
    return sum([fitness(agent) for agent in agents]) / len(agents)

def main():
    agents = [get_random_agent() for i in range(pop_size)]

    #while len(agents):
    for i in range(10000000000):
        #print(get_avg_fitness(agents))
        agents = select(agents)
        agents = reproduce(agents)

main()
