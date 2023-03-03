import math
import numpy as np
import matplotlib.pyplot as plt
import random

from tqdm import tqdm

sq2 = math.sqrt(2)
intercepts = [
    -50 + 25 * sq2,
    -50 + 15 * sq2,
    -50 + 5 * sq2,
    -50 - 5 * sq2,
    -50 - 15 * sq2,
    -50 - 25 * sq2,
]

xs = np.linspace(0, 100, 10_000)


def lin(intercept, xs):
    ys = []
    for x in xs:
        ys.append(intercept + x)
    return ys


def draw_problem():
    plt.plot(xs, lin(intercepts[0], xs))
    plt.plot(xs, lin(intercepts[1], xs))
    plt.plot(xs, lin(intercepts[2], xs))
    plt.plot(xs, lin(intercepts[3], xs))
    plt.plot(xs, lin(intercepts[4], xs))
    plt.plot(xs, lin(intercepts[5], xs))
    plt.plot(0, 0, "bo")
    plt.plot(100, 0, "bo")


# draw_problem()
def create_line(start, slope, intercept, draw=None):
    x_intercept = (intercept + slope * start[0] - start[1]) / (slope - 1)
    new_xs = np.linspace(start[0], x_intercept, 10_000)
    new_ys = lambda x: x * slope - start[0] * slope + start[1]
    if draw:
        plt.plot(new_xs, [new_ys(x) for x in new_xs])
    return (
        x_intercept,
        new_ys(x_intercept),
        np.linalg.norm([x_intercept - start[0], new_ys(x_intercept) - start[1]]),
    )


def line_to_end(start, draw=None):
    new_xs = np.linspace(start[0], 100)
    slope = -start[1] / (100 - start[0])
    new_ys = lambda x: (slope) * (x - start[0]) + start[1]
    if draw:
        plt.plot(new_xs, [new_ys(x) for x in new_xs])
    return np.linalg.norm([100 - start[0], start[1]])


def draw_from_slopes(slopes):
    draw_problem()
    x, y, dist = create_line((0, 0), slopes[0], intercepts[0], draw=True)
    x, y, dist = create_line((x, y), slopes[1], intercepts[1], draw=True)
    x, y, dist = create_line((x, y), slopes[2], intercepts[2], draw=True)
    x, y, dist = create_line((x, y), slopes[3], intercepts[3], draw=True)
    x, y, dist = create_line((x, y), slopes[4], intercepts[4], draw=True)
    x, y, dist = create_line((x, y), slopes[5], intercepts[5], draw=True)
    dist = line_to_end((x, y), draw=True)


def time_from_slopes(slopes):
    total = 0
    x, y, dist = create_line((0, 0), slopes[0], intercepts[0])
    total += dist / 10
    x, y, dist = create_line((x, y), slopes[1], intercepts[1])
    total += dist / 9
    x, y, dist = create_line((x, y), slopes[2], intercepts[2])
    total += dist / 8
    x, y, dist = create_line((x, y), slopes[3], intercepts[3])
    total += dist / 7
    x, y, dist = create_line((x, y), slopes[4], intercepts[4])
    total += dist / 6
    x, y, dist = create_line((x, y), slopes[5], intercepts[5])
    total += dist / 5
    dist = line_to_end((x, y))
    total += dist / 10
    return total


print(time_from_slopes([0, 0, 0, 0, 0, 0]))


def create_population(pop_size):
    gen = []
    for i in range(pop_size):
        new_dude = []
        for j in range(6):
            new_dude.append(random.random() * 2 - 1)
        gen.append(new_dude)
    return gen


def make_children(parents):
    child = [parents[0][i] for i in range(3)]
    child.extend(parents[1][i] for i in range(3, 6))
    for i, j in enumerate(child):
        if random.random() < 0.01:
            child[i] = random.random() * 2 - 1
    return child


def genetic_alg(gen0, generations):
    gen = gen0
    same_counter = 0
    last_gen = 0
    for i in range(generations):
        next_gen = []
        fitnesses = [time_from_slopes(x) for x in gen]
        best = fitnesses.index(min(fitnesses))
        next_gen.append(gen[best])
        score = [1 / (1 + x) for x in fitnesses]
        tot_score = sum(score)
        score = [x / tot_score for x in score]
        for j in range(len(gen) - 1):
            parents = random.choices(gen, weights=score, k=2)
            next_gen.append(make_children(parents))
        gen = next_gen
        if min(fitnesses) == last_gen:
            same_counter += 1
        else:
            same_counter = 0
        if same_counter >= 10:
            break
        last_gen = min(fitnesses)
    return (min(fitnesses), next_gen[0])


mins = []
for i in range(1000):
    gen0 = create_population(1000)
    mins.append(genetic_alg(gen0, 1000))
    print(min(mins))

best = min(mins, key=lambda x: x[0])
print(best[0])
draw_from_slopes(best[1])
plt.show()
