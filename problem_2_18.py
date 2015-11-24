import numpy as np
import problem_2_18_data
reload(problem_2_18_data)



#A = np.array([[0, 1, 1, 1],
#                 [1, 0, 1, 0],
#                 [1, 1, 0, 0],
#                 [0, 1, 0, 0]])

A = problem_2_18_data.A
                 
max_path_length_to_consider = 20

B = np.linalg.matrix_power(A,20)

def check_if_path_exists(source_index, destination_index):
    if B[destination_index - 1, source_index - 1] > 0:
        return True
    else:
        return False  
                 
def find_outgoing_connections(index):
    outgoing_connections = []
    outgoing_connection_statuses =  A[:, index - 1]
    # print outgoing_connection_statuses
    for possible_connection in range(1, len(outgoing_connection_statuses) + 1):
        if outgoing_connection_statuses[possible_connection - 1] == 1:
            outgoing_connections.append(possible_connection)
    
    return outgoing_connections

                                                            

class Node(object):
    def __init__(self, index, distance_from_source):
        self.index = index
        self.distance_from_source = distance_from_source
        
class PathNode(Node):
    
    maximum_path_length = 10
    
    def __init__(self, index, distance_from_source, ancestors, destination):
        Node.__init__(self, index, distance_from_source)
        self.ancestors = ancestors
        self.destination = destination
        self.outgoing_connections = find_outgoing_connections(self.index)
        
    
    def find_distance_to_destination(self):
        distance_to_destination = self.destination.distance_from_source - self.distance_from_source
        return distance_to_destination

    
    def check_existence_of_path_to_destination(self):
        distance_to_destination = self.find_distance_to_destination()
        # print "Checking existence of path from {0}, {1} long to destination".format(self.index, distance_to_destination)
	if distance_to_destination > 0:	    
            #B = np.linalg.matrix_power(A, distance_to_destination)
            #print B
            if B[self.destination.index - 1, self.index - 1]:
                return True
            else:
                return False
        elif distance_to_destination == 0 and self.index == self.destination.index:
            return True
        else:
            return False
        
    def check_for_identical_ancestor(self):
        
      # Override this check if the current node is the destination
      # this is done to allow cycles where the destination and the source
      # are the same node.
      if self.index == self.destination.index:
          return False
      else:          
        for ancestor in self.ancestors:
            if ancestor == self.index:
                return True
            
        return False    
    
    def print_ancestors(self):
        for ancestor in self.ancestors:
            print "Ancestor index = {0}".format(ancestor)
    
    
    def propagate(self):                
        self.paths = []
        
       
        if (self.index != self.destination.index and len(self.ancestors) < PathNode.maximum_path_length) or len(self.ancestors) == 0:            
            
            # print "my index = {0}, destination index = {1}, ancestor length = {2}".format(self.index, self.destination.index, len(self.ancestors))
            
            childs_ancestors = list(self.ancestors)                         
            childs_ancestors.append(self.index)
            
            for node_index in self.outgoing_connections:                
                potential_child = PathNode(node_index, self.distance_from_source + 1, childs_ancestors, self.destination)                
                if potential_child.check_existence_of_path_to_destination() and not potential_child.check_for_identical_ancestor():
                    child = potential_child
                    # print "Child of {0} with index {1}".format(self.index, child.index)
                    child.propagate()
                    self.paths += child.paths
                    #print self.paths
                
        else:                        
            path = list(self.ancestors)
            path.append(self.index)
            self.paths.append(path)            
        
        return True
                
        
class CycleEndpoint(PathNode):
    
    def __init__(self, index, cycle_length):
        self.cycle_length = cycle_length
        destination = Node(index, cycle_length)        
        PathNode.__init__(self, index, 0, [], destination)
        
    def check_if_cycle_exists(self):
        self.propagate()
        if len(self.paths) == 0:
            return False
        else:
            return True
                                      
                    
def FindShortestCycle():
    print "Hello"
    starting_guess_for_shortest_cycle = 30
    number_of_nodes = len(A)
    print number_of_nodes
    length_of_shortest_cycle = starting_guess_for_shortest_cycle
    shortest_cycles = list()
    for node_index in range(1,number_of_nodes + 1):
        print "Checking node {0}".format(node_index)
        path_length = 2
        while path_length <= length_of_shortest_cycle:
            endpoint = CycleEndpoint(node_index, path_length) 
            if endpoint.check_if_cycle_exists():
                if path_length == length_of_shortest_cycle:
                    print endpoint.paths
                    shortest_cycles += endpoint.paths
                else:
                    shortest_cycles = list(endpoint.paths)                
                    length_of_shortest_cycle = len(shortest_cycles[0]) - 1            
            print path_length
            path_length += 1
            
	  	    
    return shortest_cycles


#print CheckIfCycleExists(1, 3)


#shortest_cycles = FindShortestCycle()
#print shortest_cycles

test_node = CycleEndpoint(8, 7)
print test_node.check_if_cycle_exists()


#
## print test_node.check_existence_of_path_to_destination()
#
#
#test_node.propagate()
#print test_node.paths
#print test_node.check_if_cycle_exists()

#print "Test node index = {0} distance from source = {1}".format(test_node.index, test_node.distance_from_source)


#test_node.propagate()
#
#for child in test_node.children:
#    print "Child index = {0} distance from source = {1}".format(child.index, child.distance_from_source)
#    
#    print "Ancestors length = {0}".format(len(child.ancestors))
#    for ancestor in child.ancestors:
#        print "Ancestor Index = {0} distance from source = {1}".format(ancestor.index, ancestor.distance_from_source)
#    
#
#
#
#for child in test_node.children:
#    print "Child index = {0}".format(child.index)
#    child.propagate()
#    for grandchild in child.children:
#        print "grandchild index = {0} distance from source = {1}".format(grandchild.index, grandchild.distance_from_source)
#    
#        print "Grandchild's ancestors length = {0}".format(len(grandchild.ancestors))
#        for ancestor in grandchild.ancestors:
#            print "Grandchild's ancestor Index = {0} distance from source = {1}".format(ancestor.index, ancestor.distance_from_source)
#    
                 
        
    
        
        
    