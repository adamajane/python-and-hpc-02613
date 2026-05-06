import sys


def squarecubes(lst):
    squares = []
    cubes = []
    for no in lst:
        squares.append(no**2)
        cubes.append(no**3)
    return (squares, cubes)


if __name__ == "__main__":
    numbers = sys.argv[1:]  # skip script name
    numbers = [int(x) for x in numbers]  # optional conversion
    print(squarecubes(numbers))