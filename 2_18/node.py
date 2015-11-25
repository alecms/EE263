import numpy as np
import problem_2_18
import data

class Node(object):
    def __init__(self, index, distance_from_source):
        self.index = index
        self.distance_from_source = distance_from_source
        
class PathNode(Node):
    
    maximum_path_length = 20
    
    def __init__(self, index, distance_from_source, node_adjacency_matrix, ancestors, destination):
        Node.__init__(self, index, distance_from_source)
        self.A = node_adjacency_matrix
        self.ancestors = ancestors
        self.destination = destination
        self.outgoing_connections = self.A.find_outgoing_connections(self.index)
        
    
    def find_distance_to_destination(self):
        distance_to_destination = self.destination.distance_from_source - self.distance_from_source
        return distance_to_destination

    
    def check_existence_of_path_to_destination(self):
        distance_to_destination = self.find_distance_to_destination()
        # print "Checking existence of path from {0}, {1} long to {2}".format(self.index, distance_to_destination, self.destination.index)
	if distance_to_destination > 0:	    
            if self.A.count_paths(distance_to_destination, self.index, self.destination.index):
                #print "Path exists"
                return True
            else:
                #print "Path does not exist"
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
                potential_child = PathNode(node_index, self.distance_from_source + 1, self.A, childs_ancestors, self.destination)                
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
        
    def find_shortest_path(self):
        path_length = 1
        self.paths = list()
        while len(self.paths) == 0 and path_length < PathNode.maximum_path_length:
            self.destination.distance_from_source = path_length
            self.propagate()            
            
            path_length += 1
            	  	    
        return self.paths
                
        
class CycleEndpoint(PathNode):
    
    def __init__(self, index, cycle_length, node_adjacency_matrix):
        self.cycle_length = cycle_length
        destination = Node(index, cycle_length)        
        PathNode.__init__(self, index, 0, node_adjacency_matrix, [], destination)
        
    def check_if_cycle_exists(self):
        self.propagate()
        if len(self.paths) == 0:
            return False
        else:
            return True
                                      