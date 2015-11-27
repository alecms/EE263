import numpy 
import data
import node
import copy

reload(data)
reload(node)

class NodeAdjacencyMatrix(numpy.ndarray):
    
    def count_paths(self, path_length, starting_node, ending_node):
        B = numpy.linalg.matrix_power(self, path_length)
        return B[ending_node - 1, starting_node - 1]
        
    def find_most_common_ending_node(self, path_length, starting_node):
        B = numpy.linalg.matrix_power(self, path_length)
        ending_node_path_counts = B[:, starting_node - 1]
        return numpy.argmax(ending_node_path_counts) + 1
        
    def find_most_common_starting_node(self, path_length, ending_node):
        B = numpy.linalg.matrix_power(self, path_length)
        starting_node_path_counts = B[ending_node - 1, :]
        return numpy.argmax(starting_node_path_counts) + 1
        
    def find_most_common_node_pair(self, path_length):
        B = numpy.linalg.matrix_power(self, path_length)
        n = len(B)
        index_of_largest_element_of_B = numpy.unravel_index(numpy.argmax(B), (n,n))
        node_pair = [index_of_largest_element_of_B[1] + 1, index_of_largest_element_of_B[0] + 1]
        return node_pair
            
    def list_paths(self, path_length, starting_node, ending_node):
        destination = node.Node(ending_node, path_length)
        source = node.PathNode(starting_node, 0, self, [], destination)
        source.propagate(True)
        return source.paths
        
    def find_outgoing_connections(self, index):
        outgoing_connections = []
        outgoing_connection_statuses =  self[:, index - 1]
   
        for possible_connection in range(1, len(outgoing_connection_statuses) + 1):
            if outgoing_connection_statuses[possible_connection - 1] == 1:
                outgoing_connections.append(possible_connection)
        
        #print "Outgoing connections for node {0}:".format(index)
        #print outgoing_connection_statuses
        #print outgoing_connections
        return outgoing_connections 
        
    def find_shortest_cycles(self):
        number_of_nodes = len(self)
        # print number_of_nodes
        length_of_shortest_cycle = -1
        shortest_cycles = list()
        for node_index in range(1,number_of_nodes + 1):
            endpoint = node.CycleEndpoint(node_index, 2, self)
            shortest_paths = endpoint.find_shortest_paths() 
            if len(shortest_paths) > 0:
                path_length = len(shortest_paths[0])
                       
                if path_length == length_of_shortest_cycle:
                    # print endpoint.paths
                    shortest_cycles += endpoint.paths
                elif path_length < length_of_shortest_cycle or length_of_shortest_cycle < 0:
                    shortest_cycles = list(endpoint.paths)
                    # print endpoint.paths                
                    length_of_shortest_cycle = len(shortest_cycles[0]) - 1            
                    # print path_length
                	    
        return shortest_cycles
 
  
    # Returns a copy of the node adjacency matrix with all incoming connections 
    # to node_index cut
    def cutoff_node(self, node_index):
        a_mod = copy.copy(self)
        blank_row = numpy.zeros((len(self),), dtype=numpy.int)
        a_mod[node_index - 1] = blank_row
        return a_mod
