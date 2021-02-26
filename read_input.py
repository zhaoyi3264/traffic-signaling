from itertools import islice

class Car:
    def __init__(self, i,  P, path):
        self.i = i # index
        self.P = P # number of streets on the path
        self.path = path # list of Street Objects
    
    def __repr__(self):
        return f'Car {self.i}'

# Node
class Intersection:
    def __init__(self):
        # list of Street objects
        self.i = [] # incoming streets
        self.o = [] # outgoing streets

    def __repr__(self):
        res = f'Intersection\n'
        res += '  Incoming\n'
        for incoming in self.i:
            res += (f'    {str(incoming)}\n')
        res += '  Outgping\n'
        for outgoing in self.o:
            res += (f'    {str(outgoing)}\n')
        return res

# Edge
class Street:
    def __init__(self, start, end, L, name):
        self.start = start
        self.end = end
        self.L = L # length in seconds
        self.name = name
        self.queue = [] # list of Car objects
        self.state = False
    
    def __repr__(self):
        return f'{self.name} ({str(self.state):5}): {str(self.queue)}'

class CityPlan:
    def __init__(self, D, I, S, V, F):
        self.D = D # duration
        self.I = I # number of intersections
        self.S = S # number of streets
        self.V = V # number of vechiles
        self.F = F # bonus
        self.streets = {} # street name, Street(start, end, L, name) object pairs
        self.intersections = [Intersection() for _ in range(I)]
        self.cars = []

    def print(self, limit=10):
        for i, inter in enumerate(islice(self.intersections, 0, limit)):
            print(f'#{i}')
            print(inter)

def read_input(file):
    with open(file, 'r') as f:
        cp = CityPlan(*[int(i) for i in f.readline()[:-1].split(' ')])
        for i in range(cp.S):
            values = f.readline()[:-1].split(' ')
            street_name = values.pop(2)
            values = [int(v) for v in values] + [street_name]
            street = Street(*values)
            cp.streets[street_name] = street
            cp.intersections[values[1]].i.append(street)  # end is the incomming
            cp.intersections[values[0]].o.append(street) # start is the outgoing
        for i in range(cp.V):
            values = f.readline()[:-1].split(' ')
            car = Car(i, values[0], [cp.streets[v] for v in values[1:]])
            cp.streets[values[1]].queue.append(car)
            cp.cars.append(car)
    return cp

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.exit()
    cp = read_input(sys.argv[1])
    cp.print()