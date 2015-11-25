import numpy 
import data
import node

reload(data)
reload(node)

class NodeAdjacencyMatrix(numpy.ndarray):
    
    def count_paths(self, path_length, starting_node, ending_node):
        B = numpy.linalg.matrix_power(self, path_length)
        return B[ending_node - 1, starting_node - 1]
        
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
        starting_guess_for_shortest_cycle = 30
        number_of_nodes = len(self)
        # print number_of_nodes
        length_of_shortest_cycle = starting_guess_for_shortest_cycle
        shortest_cycles = list()
        for node_index in range(1,number_of_nodes + 1):
            # print "Checking node {0}".format(node_index)
            path_length = 2
            while path_length <= length_of_shortest_cycle:
                endpoint = node.CycleEndpoint(node_index, path_length, self) 
                if endpoint.check_if_cycle_exists():
                    if path_length == length_of_shortest_cycle:
                        # print endpoint.paths
                        shortest_cycles += endpoint.paths
                    else:
                        shortest_cycles = list(endpoint.paths)
                        # print endpoint.paths                
                        length_of_shortest_cycle = len(shortest_cycles[0]) - 1            
                # print path_length
                path_length += 1
            
	  	    
        return shortest_cycles
 
  
