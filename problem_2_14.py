import numpy
import ts_data
reload(ts_data)

numpy.set_printoptions(threshold=numpy.nan)

#A = numpy.array([[0, 0, 0, 1],
#                [2, 0, 1, 0],
#                [0, 0, 0, 2],
#                [0, 3, 0, 0]])
                
A = ts_data.A                
                
K = 3

max_frames_to_try = 40

def get_pseudonode(node, frame):
    index = (node - 1) * K + frame
    return index
    
def find_preceding_frame(k):
    preceding_frame = ((k - 2) % K ) + 1
    return preceding_frame

    
def get_expanded_matrix_element_value(source_node, frame_sent, 
                                      destination_node, frame_available):    
    preceding_frame = find_preceding_frame(frame_available)
    
    if frame_sent == preceding_frame:
        if A[destination_node - 1, source_node - 1] == frame_sent or \
           destination_node == source_node:               
               return 1
                
    return 0    
    
def check_if_path_exists_between_pseudonodes(source, destination, B):
    if B[destination - 1, source - 1] > 0:
        return True
    else:
        return False        

def find_associated_pseudonodes(node):
    associated_pseudonodes = []
    for frame in range(1, K + 1):
        associated_pseudonode = get_pseudonode(node, frame)
        associated_pseudonodes.append(associated_pseudonode)
    return associated_pseudonodes
    
def get_node_index(pseudonode_index):
    node_index = (pseudonode_index - 1) // K + 1
    return node_index

def get_frame(pseudonode_index):
    frame_index = pseudonode_index % K
    if frame_index == 0:
        frame_index = K
    return frame_index
    
# Define arrival frame as the first frame during which the destination
# pseudonode is able to transmit the signal.
def find_arrival_frame(path_length):
    frame = (path_length + 1) % K
    if frame == 0:
        frame = K
    return frame

def find_destination_pseudonode(path_length, destination_node):
    arrival_frame = find_arrival_frame(path_length)
    destination_pseudonode = get_pseudonode(destination_node, arrival_frame)
    return destination_pseudonode
    
def check_if_path_exists(source_node, destination_node, path_length, B):
    source_pseudonode = get_pseudonode(source_node, 1)
    destination_pseudonode = find_destination_pseudonode(path_length, destination_node)
    
    if(check_if_path_exists_between_pseudonodes(source_pseudonode, \
    destination_pseudonode, B)):
        return True
    else:
        return False
                    
def find_length_of_shortest_path(source, destination, E, path_count_arrays):
    N = E.shape[0]
    frame_count = 0
    B = numpy.eye(N, dtype=int)
    
    while True:
        frame_count += 1
        B = B.dot(E)
        path_count_arrays.append(B)
        
        if check_if_path_exists(source, destination, frame_count, B):
             return frame_count
        
        if frame_count == max_frames_to_try:
            print \
            "Was not able to find a path from node {0} to node {1} in {2} frames."\
            .format(source, destination, frame_count)
            
            return False
        
def find_immediate_source_pseudonodes(destination_pseudonode, E):
	immediate_source_pseudonodes =  []
	
	# A list of ones of zeros showing which pseudonodes can transmit
	# to the destination pseudonode
	incoming_connection_statuses = E[destination_pseudonode - 1]
	
	for possible_source in range(1, len(incoming_connection_statuses + 1)):
		if incoming_connection_statuses[possible_source - 1] == 1:
			immediate_source_pseudonodes.append(possible_source)
		
	return immediate_source_pseudonodes   
    
def find_parent(child, source, path_length, path_count_arrays):
    immediate_source_pseudonodes = find_immediate_source_pseudonodes(child, path_count_arrays[0])

    for potential_parent in immediate_source_pseudonodes:
        # The source must be a parent 
        if potential_parent == source:
	   return source
        else:
            B = path_count_arrays[path_length - 2] 
            if check_if_path_exists_between_pseudonodes(source, potential_parent, B):
	       return potential_parent	   	
    print "Error: could not find a parent for pseudonode {0}, {1} frames from source".format(child, path_length)
    return False 

def backtrack_to_source(source, destination, path_length, path_count_arrays, path):
    parent = find_parent(destination, source, path_length, path_count_arrays)
    if parent != source:
        backtrack_to_source(source, parent, path_length - 1, path_count_arrays, path)
        
    path.append(parent)
    return path
    
def convert_pseudonode_path_to_nodes(pseudonode_path, node_path, frames, timestamps):
    timestamp = 1
    for pseudonode in pseudonode_path:
        node = get_node_index(pseudonode)
        node_path.append(node)        
        
        frame = get_frame(pseudonode)
        frames.append(frame)
        
        timestamps.append(timestamp)
        timestamp += 1



def build_expanded_matrix(A):

    N = A.shape[0]
    E = numpy.zeros((N * K, N * K))

    for destination_node in range(1, N + 1):
            for frame_available in range(1, K + 1):
                for source_node in range(1, N + 1): 
                    for frame_sent in range(1, K + 1):
                        row_index = \
                        get_pseudonode(destination_node, frame_available)
                        col_index = \
                        get_pseudonode(source_node, frame_sent)
                        
                        E[row_index - 1, col_index - 1] = \
                        get_expanded_matrix_element_value(source_node, frame_sent, 
                                        destination_node, frame_available)
                    
    return E 

def print_routing_instructions(timestamps, frames, node_path):
    
    for timestamp in timestamps:
        frame = frames[timestamp - 1]
        starting_node = node_path[timestamp - 1]
        ending_node = node_path[timestamp]
        if starting_node == ending_node:
            store_or_send = "store it at"
        else:
            store_or_send = "transmit it to"
        
        print "During period t = {0} (time-slot k = {1}), {2} node {3}.".format(timestamp, frame, store_or_send, ending_node)                                        


def find_shortest_path(source_node, destination_node): 

    E = build_expanded_matrix(A)
    source_pseudonode = get_pseudonode(source_node, 1)
    
    path_count_arrays = []
    number_of_frames = find_length_of_shortest_path(source_node, destination_node, E, path_count_arrays)
    if not number_of_frames:
        return
    destination_pseudonode = find_destination_pseudonode(number_of_frames, destination_node) 
    #print number_of_frames
    #print destination_pseudonode

    path = []
    path = backtrack_to_source(source_pseudonode, destination_pseudonode, number_of_frames, path_count_arrays, path)
    #print path

    node_path = []
    frames = []
    timestamps = []
    convert_pseudonode_path_to_nodes(path, node_path, frames, timestamps)
    #Add the destination node to the end of the node path
    node_path.append(destination_node)
    
    #print timestamps
    #print frames
    #print node_path

    print "A shortest path between node {0} and node {1}:".format(source_node, destination_node)
    print_routing_instructions(timestamps, frames, node_path)


def check_if_flood_complete(source_node, elapsed_time, B):
    for destination_node in range(1, A.shape[0] + 1):
        if not check_if_path_exists(source_node, destination_node, elapsed_time, B):
			return False	
    return True
    
def time_flood(source_node, path_count_arrays):
    E = build_expanded_matrix(A)
    frame_count = 0
    B = numpy.eye(E.shape[0], dtype=int)

    while True:
        frame_count += 1
        B = B.dot(E)
        path_count_arrays.append(B)
        if check_if_flood_complete(source_node, frame_count, B):
            print "This network takes {0} frames to flood from node {1}".format(frame_count, source_node)
            return frame_count
        if frame_count == max_frames_to_try:
            print \
            "Was not able to complete flood from {0} in {1} frames."\
            .format(source_node, frame_count)
            return False
	


source_node = 5		
destination_node = 18

print ""
find_shortest_path(source_node, destination_node)
print ""

source_node = 7
path_count_arrays = []
time_to_flood = time_flood(source_node, path_count_arrays)	



            

    