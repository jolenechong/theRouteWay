import random
import json

SPEED_M_PER_MIN = 20

class Edge:
    def __init__(self, to, length, label):
        self.weight = round(length/SPEED_M_PER_MIN, 2)  # length//SPEED_M_PER_MIN
        self.penalty = 0
        self.to = to
        self.label = label
    def __str__(self):
        return json.dumps({'weight': self.weight, 'to': self.to, 'label': self.label})

adj_list = []
mapping = {}

def add_vertex(edges_from):
    global adj_list
    adj_list.append([])
    for e in edges_from:
        edge = Edge(e[0], e[1], e[2])
        adj_list[-1].append(edge)
        if e[3]:
            bi_edge = Edge(len(adj_list)-1, e[1], e[4])
            adj_list[e[0]].append(bi_edge)

add_vertex([])
add_vertex([[0, 567.10, '4 2', True, '1 3']])
add_vertex([[1, 344.89, '16', True, '15'], [0, 387.14, '35 27', False]])
mapping['Y'] = [1, 0, 1]
add_vertex([[1, 305.90, '5', True, '6']])
add_vertex([[2, 310.98, '29', True, '30'], [3, 343.33, '18', True, '17']])
mapping['X'] = [3, 1, 2]
mapping['W'] = [3, 3, 4]
add_vertex([[3, 635.81, '7', True, '8']])
add_vertex([[4, 483.10, '31', True, '32'], [5, 54.15, '20', True, '19']])
add_vertex([[5, 261.15, '9', True, '10']])
add_vertex([[6, 232.72, '33', True, '34'], [7, 49.70, '36', False]])
add_vertex([[7, 339.67, '11', True, '12']])
mapping['U'] = [9, 8, 10]
add_vertex([[8, 523.11, '22', True, '21'], [9, 346.22, '24', True, '23']])
add_vertex([[9, 323.35, '13', True, '14'], [10, 540.41, '25', True, '26']])
mapping['T'] = [11, 9, 10]

# for v in adj_list:
#     print([str(x) for x in v])

test_delay = {}
for i in range(1, 37):
    test_delay['Road '+str(i)] = 0  # random.randint(0, 30)
# print(test_delay)