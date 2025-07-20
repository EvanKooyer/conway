import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import patterns

def generate_universe(size, num_patterns=0):
    initial_state = np.zeros((size,size))
    return initial_state

universe = generate_universe(128)

seed = patterns.patterns['glider']

universe[1:4, 1:4] = seed

def evolve(x, y, universes):
    sum_neighbors = np.sum(universes[x-1:x+2, y-1:y+2]) - universes[x,y]

    if universes[x,y] and not 2<= sum_neighbors <= 3:
        return 0
    elif sum_neighbors == 3:
        return 1
    else:
        return universes[x,y]

def generation(universes):
    new_universe = np.copy(universes)

    for x in range(universes.shape[0]):
        for y in range(universes.shape[1]):
            new_universe[x,y] = evolve(x,y,universes)

    return new_universe

def animate(universes, num_generations=20):
    fig, ax = plt.subplots(figsize=(7,4))
    ims = []

    for i in range(num_generations):
        im = ax.imshow(universes, animated=True)
        universes = generation(universes)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=300, blit=True, repeat_delay = 1000)

    plt.show()

if __name__ == '__main__':
    animate(universe)
