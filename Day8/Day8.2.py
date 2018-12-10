from sys import getrecursionlimit, setrecursionlimit
rec_limit = getrecursionlimit()
setrecursionlimit(1000000)


class  TreeNode:
    nodes = []
    c_indexes = []
    value = 0

    def __init__(self):
        self.nodes = []
        self.c_indexes = []
        self.value = 0

    def __str__(self):
        return f'val: {self.value}, c_nodes: {[n.value for n in self.nodes]}, idx: {self.c_indexes}'

    def __repr__(self):
        return self.__str__()


global_i = 0
global_data = []
g_sum = 0
global_nodes = []


def interpret_nodes():
    global global_i
    global global_data
    global global_nodes
    global g_sum

    node_index = len(global_nodes)
    global_nodes.append(TreeNode())

    nodes_num = int(global_data[global_i])
    global_i += 1
    meta_num = int(global_data[global_i])
    global_i += 1

    for i in range(0, nodes_num):
        index_of_node_to_add = len(global_nodes)
        interpret_nodes()
        global_nodes[node_index].nodes.append(global_nodes[index_of_node_to_add])
    for i in range(0, meta_num):
        g_sum += int(global_data[global_i])

        if nodes_num == 0:
            global_nodes[node_index].value += int(global_data[global_i])
        elif int(global_data[global_i]) <= nodes_num:
            global_nodes[node_index].value += global_nodes[node_index].nodes[int(global_data[global_i]) - 1].value

        global_i += 1

#file_read = open("test.txt", "r")
file_read = open("input.txt", "r")

global_data = file_read.readline().split(' ')

interpret_nodes()

print(f'Value of root equals {global_nodes[0].value}.')
