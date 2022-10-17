'''
Minimum spanning tree is the way to create a path of a weighted edge graph 
that is if we have a graph of vertices 0-6 and we have weights for going from each vertices
i.e. weight for going from 0-1 is 2, 0-2 is 4, 2-3 is 5 and so on 
'''

'''
Aditya prasad
minimum spanning tree aplication with graph implementation and also different brute force algo's like 
prim's method and kruskal's algo'''

# The data structure is as follows :-
# [starting vertex, ending vertex, weight]




from copy import copy
def dictionary_search(dictionary, value):
    '''
    Assuming that you have a dictionary of the form 
    index:(value)
    where value is a tuple of two elements end and weights'''
    for x in dictionary:
        if(dictionary[x] == value):
            return x
        else:
            continue
    return False


class graph():
    def __init__(self, vertices) -> None:
        # items(alltree, alltreeInverse) --> is a list of dictionary [{index:(ending vertex, weight)}] and no of dictionaries is equal to starting vertex
        self.alltree = []
        self.alltreeInverse = []
        for _ in range(vertices):
            self.alltree.append({})
            self.alltreeInverse.append({})
        self.weights = []  # item --> integer list
        # items(vertexindex, vertexindexInverse) --> [vertex, index of weight in the alltree[vertex] list]
        self.vertexindex = []
        self.vertexIndexInverse = []

    def add(self, start, end, weight):
        '''
        I have added a completely inverse array of all the paths for checking and the keys to both of them is that 
        weights array which connects them both'''
        a = len(self.alltree[start])
        b = len(self.alltreeInverse[end])
        self.alltree[start][a] = (end, weight)
        self.alltreeInverse[end][b] = (start, weight)
        # Now i have created a weights list for all the weights findings
        self.weights.append(weight)
        # Because i may have to find the weights corresponding to the index in alltree i have created
        # vertexindex list which has items of type
        # [startindex, index of this weight in the alltree[startindex]]
        # by this way we can track the index of a particular weight to its index in alltree
        self.vertexindex.append([start, a])
        self.vertexIndexInverse.append([end, b])
        return 0

    def delete(self, edge, weight, whichlistisitcomingfrom):
        # print(self.alltree[edge[0]])
        # print(self.alltreeInverse, 'inverse list ')
        # print(self.alltree, 'straight list')
        # print(edge, weight, whichlistisitcomingfrom)
        # print('before delete')
        # print(self.alltree)
        # print(self.alltreeInverse)
        if(whichlistisitcomingfrom == 0):
            a = self.alltree[edge[0]]
            ax = dictionary_search(a, (edge[1], weight))
            del self.alltree[edge[0]][ax]
            b = self.alltreeInverse[edge[1]]
            bx = dictionary_search(b, (edge[0], weight))
            del self.alltreeInverse[edge[1]][bx]

        else:
            a = self.alltreeInverse[edge[0]]
            ax = dictionary_search(a, (edge[1], weight))
            del self.alltreeInverse[edge[0]][ax]
            b = self.alltree[edge[1]]
            bx = dictionary_search(b, (edge[0], weight))
            del self.alltree[edge[1]][bx]

        c = self.weights.index(weight)
        # print(c, self.vertexindex, self.weights)
        self.vertexindex.pop(c)
        self.vertexIndexInverse.pop(c)
        self.weights.pop(c)
        # print('after delete')
        # print(self.alltree)
        # print(self.alltreeInverse)
        return 0


'''
The first is the prim's method
in prim's method we choose the most minimum weighted weight first 
and then we continue by choosing the minimum weighted weight which is connected to the previous selected edges
and also deleting the weights which will form a loop
'''


def checkLoop(graph, current_tree, input_edge):
    if(len(current_tree) == 0):
        return False
    else:
        pass
    '''if there are more than one vertex which the input edge already has connection than its making a loop'''
    a = graph.alltree[input_edge[0]]
    all_vertices = []
    # all_vertices.append(input_edge[0])
    for x in a:
        all_vertices.append(a[x][0])
    counter = 0
    print(all_vertices)
    for x in current_tree:
        # print(x)
        if(x[0] in all_vertices):
            counter += 1
        elif(x[1] in all_vertices):
            counter += 1
        elif(counter > 1):
            return True
        else:
            continue

    b = graph.alltree[input_edge[1]]
    all_vertices = []
    # all_vertices.append(input_edge[1])
    for x in b:
        all_vertices.append(b[x][0])
    counter = 0
    for x in current_tree:
        if(x[0] in all_vertices):
            counter += 1
        elif(x[1] in all_vertices):
            counter += 1
        elif(counter > 1):
            return True
        else:
            continue

    c = graph.alltreeInverse[input_edge[0]]
    all_vertices = []
    for x in c:
        all_vertices.append(c[x][0])
    counter = 0
    for x in current_tree:
        if(x[0] in all_vertices):
            counter += 1
        elif(x[1] in all_vertices):
            counter += 1
        elif(counter > 1):
            return True
        else:
            continue
    d = graph.alltreeInverse[input_edge[1]]
    all_vertices = []
    for x in d:
        all_vertices.append(d[x][0])
    counter = 0
    for x in current_tree:
        if(x[0] in all_vertices):
            counter += 1
        elif(x[1] in all_vertices):
            counter += 1
        elif(counter > 1):
            return True
        else:
            continue
    return False


def primsMethod(input_graph: graph):
    visited_path = []  # each item -->  [startvertex, endvertex, weight]
    visited_Vertices = []  # each item --> vertex
    # discarded = []
    min_weight = min(input_graph.weights)
    a = input_graph.weights.index(min_weight)
    point = input_graph.vertexindex[a]
    # print(input_graph.vertexindex)
    # print(len(input_graph.alltree[point[0]]))
    # print(input_graph.alltree[point[0]][point[1]][0])
    visited_path.append(
        [point[0], input_graph.alltree[point[0]][point[1]][0], min_weight])
    visited_Vertices.append(point[0])
    visited_Vertices.append(input_graph.alltree[point[0]][point[1]][0])
    # print(visited_path)
    # print(visited_Vertices)
    # print([point[0], input_graph.alltree[point[0]][point[1]][0]], "delete check")
    input_graph.delete(
        [point[0], input_graph.alltree[point[0]][point[1]][0]], min_weight, 0)
    while(len(visited_path) != vertices-1):
        weights_for_visited_vertices_Edges_straight = []  # item --> integervariable
        weights_for_visited_vertices_Edges_inverse = []  # item -->

        # item --> [edge, index, which list is it coming from boolean no]
        index_of_weights_straight = []
        # item --> [edge, index, which list is it coming from boolean no]
        index_of_weights_inverse = []
        for x in visited_Vertices:
            # looping for the straight tree
            edges_for_vertex_x = input_graph.alltree[x]
            for all_weights in edges_for_vertex_x:
                weights_for_visited_vertices_Edges_straight.append(
                    edges_for_vertex_x[all_weights][1])
                index_of_weights_straight.append([x, all_weights, 0])
        print(weights_for_visited_vertices_Edges_straight, index_of_weights_straight,
              'all weights for straight tree')
        cur_min_straight = min(weights_for_visited_vertices_Edges_straight)
        for x in visited_Vertices:
            # looping for the inverse list
            edges_for_vertex_x = input_graph.alltreeInverse[x]
            # print(edges_for_vertex_x)
            for all_weights in edges_for_vertex_x:
                # print(all_weights)
                # print(edges_for_vertex_x[all_weights][1])
                weights_for_visited_vertices_Edges_inverse.append(
                    edges_for_vertex_x[all_weights][1])
                index_of_weights_inverse.append([x, all_weights, 1])
        print(weights_for_visited_vertices_Edges_inverse, index_of_weights_inverse,
              'all tree weights in inverse')
        cur_min_inverse = min(weights_for_visited_vertices_Edges_inverse)

        # print(index_of_weights_straight, index_of_weights_inverse, 'index of all weights')
        print(cur_min_inverse, '--> inverse', cur_min_straight, '--> straight')
        if(cur_min_straight <= cur_min_inverse):
            '''now we are going for the min from straight tree'''
            a = weights_for_visited_vertices_Edges_straight.index(
                cur_min_straight)
            print(a, 'printing the edge"s index ')
            other_edge = input_graph.alltree[index_of_weights_straight[a]
                                             [0]][index_of_weights_straight[a][1]][0]
            print(other_edge, 'other edge')
            if(checkLoop(input_graph, visited_path, [index_of_weights_straight[a][0], other_edge])):
                print('decision taken deleting the edge', [
                      index_of_weights_inverse[a][0], other_edge], cur_min_straight)
                input_graph.delete(
                    [index_of_weights_straight[a][0], other_edge], cur_min_straight, 0)
            else:
                print('decision taken this is the edge')  # , [
                #   index_of_weights_inverse[a][0], other_edge], cur_min_straight)
                visited_path.append(
                    [index_of_weights_straight[a][0], other_edge, cur_min_straight])
                if(other_edge not in visited_Vertices):
                    visited_Vertices.append(other_edge)
                input_graph.delete(
                    [index_of_weights_straight[a][0], other_edge], cur_min_straight, 0)
        else:
            '''now we are going for the min from inverse tree'''
            a = weights_for_visited_vertices_Edges_inverse.index(
                cur_min_inverse)
            other_edge = input_graph.alltreeInverse[index_of_weights_inverse[a]
                                                    [0]][index_of_weights_inverse[a][1]][0]
            # print([index_of_weights_inverse[a][0], other_edge, cur_min_inverse])
            if(checkLoop(input_graph, visited_path, [index_of_weights_inverse[a][0], other_edge])):
                print('decision taken deleting the edge', [
                      index_of_weights_inverse[a][0], other_edge], cur_min_inverse)
                input_graph.delete(
                    [index_of_weights_inverse[a][0], other_edge], cur_min_inverse, 1)
            else:
                print('decision taken this is the edge', [
                      index_of_weights_inverse[a][0], other_edge], cur_min_inverse)
                visited_path.append(
                    [index_of_weights_inverse[a][0], other_edge, cur_min_inverse])
                if(other_edge not in visited_Vertices):
                    visited_Vertices.append(other_edge)
                input_graph.delete(
                    [index_of_weights_inverse[a][0], other_edge], cur_min_inverse, 1)
            print(visited_path, 'the current path ')

    print(visited_path, 'the final path')


def kruskals_method(input_graph: graph):
    '''
    in kruskals method we directly find the smallest weights and go on adding the edges 
    one by one until we have (vertex-1) edges'''
    visited_path = []  # each item -->  [startvertex, endvertex, weight]
    visited_Vertices = []  # each item --> vertex int object
    '''
    we just have to sort the weights and then one by one add the smallest 
    edges while checking if they make a loop or not 

    sorting the edges
    '''
    print(input_graph.alltree)

    def sort_using_main_list(main_list_to_sort_with, list_of_all_affecting_lists):
        '''
        in this method we are actually just sorting a single list but 
        we are making the affect of sort applicable on the other lists connected to it 
        as the indexofvertex list in our program is connected to the weights through index-index'''
        for x in range(len(main_list_to_sort_with)):
            for y in range(x, len(main_list_to_sort_with)):
                if(main_list_to_sort_with[x] <= main_list_to_sort_with[y]):
                    continue
                else:
                    subs = main_list_to_sort_with[x]
                    main_list_to_sort_with[x] = main_list_to_sort_with[y]
                    main_list_to_sort_with[y] = subs
                    for list_n in list_of_all_affecting_lists:
                        '''the same process as above on each list of list_of_all_affecting_lists'''
                        nth_sub = list_n[x]
                        list_n[x] = list_n[y]
                        list_n[y] = nth_sub

    sort_using_main_list(input_graph.weights, [
                         input_graph.vertexindex, input_graph.vertexIndexInverse])
    print(input_graph.weights)
    for x in range(len(input_graph.weights)):
        while(len(visited_path) != vertices-1):
            if(checkLoop(input_graph, visited_path, [input_graph.vertexindex[x][0], input_graph.alltree[input_graph.vertexindex[x][0]][input_graph.vertexindex[x][1]][0]])):
                print('decision taken this edge is deleeted', [input_graph.vertexindex[x][0], input_graph.alltree[input_graph.vertexindex[x]
                                                                                                                  [0]][input_graph.vertexindex[x][1]][0], input_graph.weights[x]])
                input_graph.delete([input_graph.vertexindex[x][0], input_graph.alltree[input_graph.vertexindex[x]
                                                                                       [0]][input_graph.vertexindex[x][1]][0]], input_graph.weights[x], 0)
            else:
                print('decision taken taking this edge', [input_graph.vertexindex[x][0], input_graph.alltree[input_graph.vertexindex[x]
                                                                                                             [0]][input_graph.vertexindex[x][1]][0], input_graph.weights[x]])
                visited_path.append([input_graph.vertexindex[x][0], input_graph.alltree[input_graph.vertexindex[x]
                                    [0]][input_graph.vertexindex[x][1]][0], input_graph.weights[x]])
                input_graph.delete([input_graph.vertexindex[x][0], input_graph.alltree[input_graph.vertexindex[x]
                                                                                       [0]][input_graph.vertexindex[x][1]][0]], input_graph.weights[x], 0)
    print(visited_path)


vertices = 0
with open("coding practice/graph.txt", "r") as f:
    vertices = int(f.readline())
    input_graph = graph(vertices)
    for x in f.readlines():
        z = x.split()
        input_graph.add(int(z[0]), int(z[1]), int(z[2]))
    # print(input_graph.alltree)
    # print(input_graph.alltreeInverse)
    f.close()


# primsMethod(input_graph)
kruskals_method(input_graph)
