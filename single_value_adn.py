import math
import random
import numpy as np
import matplotlib.pyplot as plt

pop_size = 24
enzo = .99

def fitness(x):
    x = x[0]
    pos1 = x if x < 5 else 0
    pos2 = x - 7.5 if 10 <= x < 20 else 0
    neg1 = -x/2 + 7.5 if 5 <= x < 10 else 0
    neg2 = -x/2 + 22.5 if x >= 20 else 0
    return pos1 + pos2 + neg1 + neg2

def get_random_agent():
    return [random.gauss(-10, .01), []]

def mutate(agent):
    mutation_rate = 0

    if len(agent[1]):
        ancestors = [[np.sign(a[0] - agent[0]), a[1] - fitness(agent)] for a in agent[1]]
        mutation_rate = np.mean([a[0] * a[1] * enzo ** (len(ancestors) - i) for i, a in enumerate(ancestors)])

    mutation_rate = mutation_rate if mutation_rate > 1e-3 else np.sign(mutation_rate) * 1e-3
    mutation = random.gauss(mutation_rate, .01)
    print('mutation_rate:', mutation_rate)
    print('mutation:', mutation)

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
    new_agents = [mutate(a) for a in agents]

    while len(new_agents) < pop_size:
        new_agent = mutate(random.choice(agents))
        new_agents.append(new_agent)

    return new_agents

def get_avg_fitness(agents):
    return sum([fitness(agent) for agent in agents]) / len(agents)

def get_avg_value(agents):
    return sum([agent[0] for agent in agents]) / len(agents)

def main():
    agents = [get_random_agent() for i in range(pop_size)]

    # Plotting
    arr = [fitness([y]) for y in range(-10, 30)]
    plt.plot(list(range(-10, 30)), arr)
    last_point = None

    for i in range(512):
        # More plotting
        best_agent_i = np.argmax([fitness(a) for a in agents])
        random_agent = random.choice(agents)
        best_agent = agents[best_agent_i]
        last_point = plt.scatter(best_agent[0], fitness(best_agent))
        last_point = plt.scatter(random_agent[0], fitness(random_agent), c='#00FF00')
        plt.pause(0.05)
        last_point.remove()

        agents = select(agents)
        agents = reproduce(agents)

    plt.show()

main()
