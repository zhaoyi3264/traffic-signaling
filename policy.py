from read_input import *
import numpy as np
import math
import sys
# total cars
cityplan = read_input(sys.argv[1])
duration = cityplan.D
scaling_factor = 1

def totalflow():
    flowdic = {}
    streetnames = cityplan.streets.keys()
    for name in streetnames:
        flowdic[name] = 0
    for car in cityplan.cars:
        path = car.path
        for street in path:
            flowdic[street.name] += 1

    return {k: v for k, v in flowdic.items() if v > 0}

def assigngreenlights(flowdic):
    # [{'a':2, 'b':1}, {'c':3, 'd':1}]
    green_light_time = [] # a list of dics
    nodes = cityplan.intersections
    for node in nodes:
        cycle ={}
        inflows = node.i
        inflows = [s for s in inflows if s.name in flowdic]
        if len(inflows) == 0:
            continue
        inflows.sort(key=lambda s: flowdic.get(s.name, 0), reverse=True)
        shortest = flowdic[inflows[-1].name]
        for s in inflows:
            cycle[s.name]= math.ceil(flowdic[s.name]/shortest) * scaling_factor

        green_light_time.append(cycle)
        
    return green_light_time

p = assigngreenlights(totalflow())

with open(sys.argv[1].replace('.', '_out.'), 'w') as f:
    f.write(f'{len(p)}\n')
    for i in range(len(p)):
        inter = cityplan.intersections[i]
        f.write(f'{i}\n{len(inter.i)}\n')
        for street in inter.i:
            f.write(f'{street.name} 1\n')