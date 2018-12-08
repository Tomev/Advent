global_i = 0
global_data = []
global_meta_sum = 0

def interpret_nodes():
    global global_i
    global global_data
    global global_meta_sum


    nodes_num = int(global_data[global_i])
    global_i += 1
    meta_num = int(global_data[global_i])
    global_i += 1

    for i in range(0, nodes_num):
        interpret_nodes()
    for i in range(0, meta_num):
        global_meta_sum += int(global_data[global_i])
        global_i += 1


file_read = open("input.txt", "r")
# file_read = open("test.txt", "r")

global_data = file_read.readline().split(' ')

interpret_nodes()

print(f'Meta data sum equals {global_meta_sum}.')




