import random

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt

from patterns import patterns


def generate_universe(size: int, num_patterns: int = 0) -> npt.NDArray:
    """
    Randomly generates a square universe based on input size,
    and places a randomly selected number of patterns on that
    generated universe.

    size: int
    num_patterns: int
    """
    initial_state = np.zeros((size, size))

    for i in range(0, num_patterns):
        ptrn = random.choice(list(patterns.values()))
        xlen = len(ptrn)
        ylen = len(ptrn[0])

        insert_coords = [random.randint(0, size), random.randint(0, size)]

        if insert_coords[0] + xlen > size:
            insert_coords[0] = size - xlen
        if insert_coords[1] + ylen > size:
            insert_coords[1] = size - ylen

        initial_state[
            insert_coords[0] : insert_coords[0] + xlen,
            insert_coords[1] : insert_coords[1] + ylen,
        ] = ptrn

    return initial_state


def evolve(x: int, y: int, universes: npt.NDArray) -> int:
    """
    Takes in a coordinate value and sums all neigboring cells
    to determine if the cell should remain alive based on game of
    life rules.

    x: int
    y: int
    universes: Numpy array
    """
    sum_neighbors = np.sum(universes[x - 1 : x + 2, y - 1 : y + 2]) - universes[x, y]

    if universes[x, y] and not 2 <= sum_neighbors <= 3:
        return 0
    elif sum_neighbors == 3:
        return 1
    else:
        return universes[x, y]


def generation(universes: npt.NDArray) -> npt.NDArray:
    """
    Loop over game of life array to calculate next generation.
    universes = Numpy array
    """
    new_universe = np.copy(universes)

    for x in range(universes.shape[0]):
        for y in range(universes.shape[1]):
            new_universe[x, y] = evolve(x, y, universes)

    return new_universe


def animate(universes: npt.NDArray, num_generations: int = 20) -> None:
    """
    Generate an animation of a set number of generations of the
    game of life.
    """
    fig, ax = plt.subplots(figsize=(7, 4))
    ims = []

    for i in range(num_generations):
        im = ax.imshow(universes, animated=True)
        universes = generation(universes)
        ims.append([im])

    ani = animation.ArtistAnimation(
        fig, ims, interval=300, blit=True, repeat_delay=1000
    )

    plt.show()


def main(size: int = 32, patterns: int = 12, generations: int = 20) -> None:
    """
    main entrypoint into program
    """
    universe = generate_universe(size, patterns)
    animate(universe, generations)


if __name__ == "__main__":
    main()
