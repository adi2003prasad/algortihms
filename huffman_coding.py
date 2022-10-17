'''
Huffman coding is an algorithm which gives input's different unique characters like encrypting the message
This is also a type of greedy algorithm.
'''
import heapq


class huffman_coding():

    def __init__(self, dictionary_of_inputs_count) -> None:
        '''init here is initializing this class with the input of dictionaries , 
        creating a heap with it which will further help us to find the encoding criterion'''
        self.heap_list = []  # data type -> [frequency, index]
        self.dictionary_of_nodes = []  # data type -> [parent, left, right]
        self.encoded = []  # data type ->  (term, code)
        for x in dictionary_of_inputs_count.items():
            '''we are flipping the values so that heapq can sort them easily'''
            heapq.heappush(self.heap_list, (x[1], x[0]))
        print(self.heap_list)
        self.tree_creator()
        self.huffman_encoding()
        # print(self.encoded)

    def tree_creator(self):
        '''this function takes a heap list and for each 2 lowest terms it 
        makes a node and appends it into the nodes dictionary in the form of 
        [parentadress, leftaddress, rightaddress]'''
        while len(self.heap_list) > 1:
            left = heapq.heappop(self.heap_list)
            right = heapq.heappop(self.heap_list)
            parent_frequency = left[0]+right[0]
            parent_name = left[1]+right[1]
            self.dictionary_of_nodes.append(
                [(parent_frequency, parent_name), left, right])
            heapq.heappush(self.heap_list, (parent_frequency, parent_name))
        self.dictionary_of_nodes.reverse()
        print(self.dictionary_of_nodes)

    def huffman_encoding(self, parent_node_address=(), text=''):
        '''this is a recursive cycle which goes on until it reaches the terminal node'''
        if (len(parent_node_address) == 0):
            parent_node_address = self.dictionary_of_nodes[0][0]
        else:
            pass
        # print(parent_node_address)
        for x in self.dictionary_of_nodes:
            if(x[0] == parent_node_address):
                if((len(x[1][1]) == 1) and (len(x[2][1]) == 1)):
                    self.encoded.append((x[1][1], text+'0'))
                    self.encoded.append((x[2][1], text+'1'))
                elif(len(x[1][1]) == 1):
                    self.encoded.append((x[1][1], text+'0'))
                    self.huffman_encoding(x[2], text+'1')
                elif(len(x[2][1]) == 1):
                    self.encoded.append((x[2][1], text+'1'))
                    self.huffman_encoding(x[1], text+'0')
                else:
                    self.huffman_encoding(x[1], text+'0')
                    self.huffman_encoding(x[2], text+'1')


a = huffman_coding({'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45})
print(a.encoded)
