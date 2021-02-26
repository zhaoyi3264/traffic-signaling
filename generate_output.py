from read_input import *


# schedule 1 second for each incoming street
def generate_output_simple(file):
    cp = read_input(file)
    with open(file.replace('.', '_out.'), 'w') as f:
        f.write(f'{len(cp.intersections)}\n')
        for i in range(len(cp.intersections)):
            inter = cp.intersections[i]
            f.write(f'{i}\n{len(inter.i)}\n')
            for street in inter.i:
                f.write(f'{street.name} 1\n')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.exit()
    generate_output_simple(sys.argv[1])