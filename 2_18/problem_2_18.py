import numpy as np
import data
import node
import node_adjacency_matrix

reload(data)
reload(node)
reload(node_adjacency_matrix)

print "Output for Problem 2.18"
print "\n"

print "a)"
A = node_adjacency_matrix.NodeAdjacencyMatrix((20,20), buffer=np.array(data.A_data), dtype=int)
print "Shortest cycle:"
print A.find_shortest_cycles()
print "\n"

print "b)"
destination = node.Node(17, 1)
source = node.PathNode(13, 0, A, [], destination)
print "Shortest path between 13 and 17:"
print source.find_shortest_paths()
print "\n"


print "c)"
A_modified = A.cutoff_node(3)                                                            
source = node.PathNode(13, 0, A_modified, [], destination)
print "Shortest path between 13 and 17 that does not go through 3:"
print source.find_shortest_paths_excluding(3)
print "\n"

print "d)"
print "Shortest paths between 13 and 17 that go through 9:"
print source.find_shortest_paths_including(9)
print "\n"

print "e)"
print "The most common ending node for paths of length 10, starting at node 5:"
print A.find_most_common_ending_node(10, 5)
print "{0} paths start and end this way".format(A.count_paths(10, 5, A.find_most_common_ending_node(10, 5)))
print "\n"

print "f)"
print "The most common starting node for paths of length 10, that end at node 8:"
print A.find_most_common_starting_node(10, 8)
print "{0} paths start and end this way".format(A.count_paths(10, A.find_most_common_starting_node(10, 8), 8))
print "\n"

print "g)"
print "The most common node pair [starting, ending]:"
most_common_pair = A.find_most_common_node_pair(10)
print most_common_pair
print "{0} paths start and end this way".format(A.count_paths(10, most_common_pair[0], most_common_pair[1]))

print "\n"

#print len(A.list_paths(10, 16, 9))
#print A.count_paths(10, 16, 9)
#print A.list_paths(10, 16, 9)



#B = np.linalg.matrix_power(A,20)
#print B[7,:]
#print np.amax(B[7,:])
#print np.argmax(B[7,:])

#print np.amax(B)
#print np.argmax(B)
#
#print np.unravel_index(np.argmax(B), (20,20))


#
#shortest_cycles = FindShortestCycle()
#print shortest_cycles



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
                 
        
    
        
        
    