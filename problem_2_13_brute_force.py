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

allowable_sequences_for_different_lengths = []

allowable_sequences_of_length_1 = [[1], [2], [3], [4], [5]]

allowable_sequences_for_different_lengths.append(allowable_sequences_of_length_1)

length_ten = 10

for length in range(2,length_ten + 1):
    allowable_sequences_for_different_lengths.append([])
    for sequence in allowable_sequences_for_different_lengths[length - 2]:            
        allowed_followers = allowedFollowers[sequence[length - 2]]
        for follower in allowed_followers:
            new_sequence = list(sequence)
            new_sequence.append(follower)
            allowable_sequences_for_different_lengths[length - 1].append(new_sequence)
        

sequences_of_length_10 = allowable_sequences_for_different_lengths[length_ten - 1]

for symbol in range(1,6):
    frequency = CountFrequency(symbol, 7, sequences_of_length_10)
    print ("Frequency of symbol {0} in seventh position = {1}".format(symbol, frequency)) 





  