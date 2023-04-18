"""
Name: Derek Ellsworth
UVU ID: 10721093
Project: Random walk

Summary: This program simulates random walks from different individuals using different criteria for each individual.
It will then plot the points
This project uses lists, recursion, loops, dictionaries, and more!


"""
import subprocess
import tempfile
import textwrap
import traceback
import sys
import random
import math
import statistics
import turtle

def main(lengths, tests, name):
    """This is for testing"""
    simulate(lengths, tests, name)

def simulate(lengths, trials, name):
    """This simulates the runs"""
    pa_walks = []
    mi_ma_walks = []
    reg_walks = []
    origin = [0,0]
    if name == 'Pa':
        directions = {'N': 1, 'E': 1, 'S': -1, 'W': -1}
        for length in lengths:
            walks = []
            x_values = []
            y_values = []
            for_max_and_min = []
            sum_amount = 0
            c_v = 0
            std_dev = 0
            for _ in range(trials):
                x_val = 0
                y_val = 0
                for _ in range(length):
                    direction = random.choice(list(directions.keys()))
                    if direction in ['E', 'W']:
                        #x_values.append(directions[direction])
                        x_val += directions[direction]
                    elif direction in ['N', 'S']:
                       # y_values.append(directions[direction])
                        y_val += directions[direction]
                x_values.append(x_val)
                y_values.append(y_val)
                walks.append([x_val,y_val])
                distance_for_min_max = math.sqrt( ((origin[0]-x_val)**2) + ((origin[1] - y_val)**2))
                for_max_and_min.append(distance_for_min_max)
            distance_max = round(max(for_max_and_min), 1)
            distance_min = round(min(for_max_and_min),1)
            for num in for_max_and_min:
                sum_amount += num
            average = round(sum_amount/len(for_max_and_min), 1)
            std_dev = statistics.stdev(for_max_and_min)
            c_v = round(std_dev / average ,1 )
            print(f"Pa random walk of {length} steps")
            print(f"Mean = {average} CV = {c_v}")
            print(f"Max = {distance_max} Min = {distance_min}")
            pa_walks.append(walks)
    if name == 'Mi-Ma':
        directions = {'N': 1, 'E': 1, 'S1': -1, 'S': -1, 'W': -1}
        for length in lengths:
            walks = []
            x_values = []
            y_values = []
            for_max_and_min = []
            sum_amount = 0
            c_v = 0
            std_dev = 0
            for _ in range(trials):
                x_val = 0
                y_val = 0
                for _ in range(length):
                    direction = random.choice(list(directions.keys()))
                    if direction in ['E', 'W']:
                        #x_values.append(directions[direction])
                        x_val += directions[direction]
                    elif direction in ['N', 'S1','S']:
                       # y_values.append(directions[direction])
                        y_val += directions[direction]
                x_values.append(x_val)
                y_values.append(y_val)
                walks.append([x_val,y_val])
                distance_for_min_max = math.sqrt( ((origin[0]-x_val)**2) + ((origin[1] - y_val)**2))
                for_max_and_min.append(distance_for_min_max)
            distance_max = round(max(for_max_and_min), 1)
            distance_min = round(min(for_max_and_min),1)
            for num in for_max_and_min:
                sum_amount += num
            average = round(sum_amount/len(for_max_and_min), 1)
            std_dev = statistics.stdev(for_max_and_min)
            c_v = round(std_dev / average ,1 )
            print(f"Mi-Ma random walk of {length} steps")
            print(f"Mean = {average} CV = {c_v}")
            print(f"Max = {distance_max} Min = {distance_min}")
            mi_ma_walks.append(walks)
    if name == 'Reg':
        directions = {'E': 1, 'W': -1}
        for length in lengths:
            walks = []
            x_values = []
            y_values = []
            for_max_and_min = []
            sum_amount = 0
            c_v = 0
            std_dev = 0
            for _ in range(trials):
                x_val = 0
                y_val = 0
                for _ in range(length):
                    direction = random.choice(list(directions.keys()))
                    if direction in ['E', 'W']:
                        x_val += directions[direction]
                x_values.append(x_val)
                y_values.append(y_val)
                walks.append([x_val,y_val])
                distance_for_min_max = math.sqrt( ((origin[0]-x_val)**2) + ((origin[1] - y_val)**2))
                for_max_and_min.append(distance_for_min_max)
            distance_max = round(max(for_max_and_min), 1)
            distance_min = round(min(for_max_and_min),1)
            for num in for_max_and_min:
                sum_amount += num
            non_rounded_average = round(sum_amount/len(for_max_and_min), 1)
            average = round(sum_amount/len(for_max_and_min), 1)
            std_dev = statistics.stdev(for_max_and_min)
            c_v = round(std_dev / non_rounded_average ,1 )
            print(f"Reg random walk of {length} steps")
            print(f"Mean = {average} CV = {c_v}")
            print(f"Max = {distance_max} Min = {distance_min}")
            reg_walks.append(walks)
    if name == 'all':
        directions = {'N': 1, 'E': 1, 'S': -1, 'W': -1}
        for length in lengths:
            walks = []
            x_values = []
            y_values = []
            for_max_and_min = []
            sum_amount = 0
            c_v = 0
            std_dev = 0
            for _ in range(trials):
                x_val = 0
                y_val = 0
                for _ in range(length):
                    direction = random.choice(list(directions.keys()))
                    if direction in ['E', 'W']:
                        #x_values.append(directions[direction])
                        x_val += directions[direction]
                    elif direction in ['N', 'S']:
                       # y_values.append(directions[direction])
                        y_val += directions[direction]
                x_values.append(x_val)
                y_values.append(y_val)
                walks.append([x_val,y_val])
                distance_for_min_max = math.sqrt( ((origin[0]-x_val)**2) + ((origin[1] - y_val)**2))
                for_max_and_min.append(distance_for_min_max)
            distance_max = round(max(for_max_and_min), 1)
            distance_min = round(min(for_max_and_min),1)
            for num in for_max_and_min:
                sum_amount += num
            average = round(sum_amount/len(for_max_and_min), 1)
            std_dev = statistics.stdev(for_max_and_min)
            c_v = round(std_dev / average ,1 )
            print(f"Pa random walk of {length} steps")
            print(f"Mean = {average} CV = {c_v}")
            print(f"Max = {distance_max} Min = {distance_min}")
            pa_walks.append('Pa')
            pa_walks.append(walks)
        directions = {'N': 1, 'E': 1, 'S1': -1, 'S': -1, 'W': -1}
        for length in lengths:
            walks = []
            x_values = []
            y_values = []
            for_max_and_min = []
            sum_amount = 0
            c_v = 0
            std_dev = 0
            for _ in range(trials):
                x_val = 0
                y_val = 0
                for _ in range(length):
                    direction = random.choice(list(directions.keys()))
                    if direction in ['E', 'W']:
                        #x_values.append(directions[direction])
                        x_val += directions[direction]
                    elif direction in ['N', 'S1','S']:
                       # y_values.append(directions[direction])
                        y_val += directions[direction]
                x_values.append(x_val)
                y_values.append(y_val)
                walks.append([x_val,y_val])
                distance_for_min_max = math.sqrt( ((origin[0]-x_val)**2) + ((origin[1] - y_val)**2))
                for_max_and_min.append(distance_for_min_max)
            distance_max = round(max(for_max_and_min), 1)
            distance_min = round(min(for_max_and_min),1)
            for num in for_max_and_min:
                sum_amount += num
            average = round(sum_amount/len(for_max_and_min), 1)
            std_dev = statistics.stdev(for_max_and_min)
            c_v = round(std_dev / average ,1 )
            print(f"Mi-Ma random walk of {length} steps")
            print(f"Mean = {average} CV = {c_v}")
            print(f"Max = {distance_max} Min = {distance_min}")
            mi_ma_walks.append('Mi-Ma')
            mi_ma_walks.append(walks)

            directions = {'E': 1, 'W': -1}
        for length in lengths:
            walks = []
            x_values = []
            y_values = []
            for_max_and_min = []
            sum_amount = 0
            c_v = 0
            std_dev = 0
            for _ in range(trials):
                x_val = 0
                y_val = 0
                for _ in range(length):
                    direction = random.choice(list(directions.keys()))
                    if direction in ['E', 'W']:
                        x_val += directions[direction]
                x_values.append(x_val)
                y_values.append(y_val)
                walks.append([x_val,y_val])
                distance_for_min_max = math.sqrt( ((origin[0]-x_val)**2) + ((origin[1] - y_val)**2))
                for_max_and_min.append(distance_for_min_max)
            distance_max = round(max(for_max_and_min), 1)
            distance_min = round(min(for_max_and_min),1)
            for num in for_max_and_min:
                sum_amount += num
            non_rounded_average = round(sum_amount/len(for_max_and_min), 1)
            average = round(sum_amount/len(for_max_and_min), 1)
            std_dev = statistics.stdev(for_max_and_min)
            c_v = round(std_dev / non_rounded_average ,1 )
            print(f"Reg random walk of {length} steps")
            print(f"Mean = {average} CV = {c_v}")
            print(f"Max = {distance_max} Min = {distance_min}")
            reg_walks.append('Reg')
            reg_walks.append(walks)
    all_walks = [pa_walks, mi_ma_walks, reg_walks]
    #print(all_walks)
    return all_walks

def plot():
    """This plots the data"""
    walks = simulate([100], 50, 'all')
    screen = turtle.Screen()
    screen.setup(300,400)
    turtle.penup()
    for walker in walks:
        #print('New Walker')
        if walker[0] == 'Pa':
            turtle.shape('circle')
            turtle.speed(1)
            turtle.shapesize(0.5, 0.5)
            turtle.color('black')
            #print(walker)
            for dataset in walker:
                for point in dataset:
                    if isinstance(point, list):
                       # print(point)
                        turtle.goto(point[0]*5, point[1]*5)
                        turtle.stamp()
        if walker[0] == 'Mi-Ma':
            turtle.shape('square')
            turtle.speed(9)
            turtle.shapesize(0.5, 0.5)
            turtle.color('green')
            for dataset in walker:
                for point in dataset:
                    if isinstance(point, list):
                       # print(point)
                        turtle.goto(point[0]*5, point[1]*5)
                        turtle.stamp()
        if walker[0] == 'Reg':
            turtle.shape('triangle')
            turtle.speed(9)
            turtle.shapesize(0.5, 0.5)
            turtle.color('red')
            for dataset in walker:
                for point in dataset:
                    if isinstance(point, list):
                        #print(point)
                        turtle.goto(point[0]*5, point[1]*5)
                        turtle.stamp()
    save_to_image()
        #each walker is a set of coordinates from the runs. Plot the coordinates
def save_to_image(dest='random_walk.png'):
    '''Saves the turtle canvas to dest. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        command = ['gs',
                   '-dSAFER',
                   '-o',
                   dest,
                   '-r200',
                   '-dEPSCrop',
                   '-sDEVICE=png16m',
                   tmp.name]
        try:
            subprocess.run(command,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           check=True)
        except Exception as exp:
            message = f'''\
            There was an error running ghostscript.

            If you are seeing this error in Codio, please report it to your instructor.
            If you are seeing this error elsewhere, consider installing ghostscript or
            replacing the call to `save_to_image()' with `turtle.done()' in your local
            copy. Be sure not to change run_doodles.py in Codio!

            The system was attempting to run the following command:
            {' '.join(command)}

            Error details:
            '''
            print(textwrap.dedent(message), file=sys.stderr)
            [_, minor, _] = sys.version.split()[0].split('.')
            minor = int(minor)
            # python version >= 3.10
            if minor >= 10:
                # pylint: disable=E1120
                traceback.print_exception(exp)
            # python version < 3.10
            else:
                traceback.print_exception(None, exp, None)
