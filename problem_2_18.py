import numpy as np

A = np.array([[0, 0, 1, 1],
                 [1, 0, 1, 0],
                 [1, 1, 0, 0],
                 [0, 1, 0, 0]])
                 
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
    for possible_connection in range(1, len(outgoing_connection_statuses) + 1):
        if outgoing_connection_statuses[possible_connection - 1] == 1:
            outgoing_connections.append(possible_connection)
    
    return outgoing_connections

                                                            

class Node(object):
    def __init__(self, index, distance_from_source):
        self.index = index
        self.distance_from_source = distance_from_source
        
class PathNode(Node):
    
    maximum_path_length = 25
    
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
	if distance_to_destination > 0:	    
            B = np.linalg.matrix_power(A, distance_to_destination)
            if B[self.destination.index - 1, self.index - 1]:
                return True
            else:
                return False
        else:
            return True
        
    def check_for_identical_ancestor(self):
        for ancestor in self.ancestors:
            if ancestor == self.index:
                return True
            else:
                return False    
    
    def print_ancestors(self):
        for ancestor in self.ancestors:
            print "Ancestor index = {0}".format(ancestor)
    
    
    def propagate(self):                
        if self.index != destination.index:
            self.children = []
            childs_ancestors = list(self.ancestors)                         
            childs_ancestors.append(self.index)
            
            for node_index in self.outgoing_connections:                
                potential_child = PathNode(node_index, self.distance_from_source + 1, childs_ancestors, self.destination)                
                if potential_child.check_existence_of_path_to_destination() and not potential_child.check_for_identical_ancestor():
                    self.children.append(potential_child)
                    return potential_child.propagate()
                    
        else:                        
            path_nodes = list(self.ancestors)
            path_nodes.append(self.index)
            return path_nodes
                    
                    
ancestors = list()

destination = Node(4, 2)

test_node = PathNode(3, 0, ancestors, destination)

test_node.propagate()

print "Test node index = {0} distance from source = {1}".format(test_node.index, test_node.distance_from_source)


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
                 
        
    
        
        
    