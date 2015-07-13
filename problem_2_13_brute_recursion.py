# Counts the frequency of symbol in position
# amongst the sequences in sequence list.
# The first symbol in the sequence is taken
# as position 1.
def CountFrequency(symbol, position, sequence_list):
    frequency = 0
    for sequence in sequence_list:
        if sequence[position - 1] == symbol:
            frequency += 1

    return frequency


allowedFollowers = {1 : [2, 3],
                    2 : [2, 5],
                    3 : [1],
                    4 : [2, 4, 5],
                    5 : [1, 3]
}

allowable_sequences_of_length_1 = [[1], [2], [3], [4], [5]]

def find_sequences(length):
    
    if(length == 1):
        return allowable_sequences_of_length_1
    
    else:
        
        parent_sequences = find_sequences(length - 1)
        child_sequences = []
        
        for parent_sequence in parent_sequences:            
            # A list of the symbols that can follow the last symbol in the 
            # parent sequence
            allowed_followers = allowedFollowers[parent_sequence[-1]]
        
            for follower in allowed_followers:
                # Initialize the child sequence as a copy of its parent
                child_sequence = list(parent_sequence)
                # Add the allowed follower to the child
                child_sequence.append(follower)
                # Add each child sequence to allowable_sequences
                child_sequences.append(child_sequence)
        
        return child_sequences

            

sequences_of_length_10 = find_sequences(10)

for symbol in range(1,6):
    frequency = CountFrequency(symbol, 7, sequences_of_length_10)
    print ("Frequency of symbol {0} in seventh position = {1}".format(symbol, frequency)) 





  