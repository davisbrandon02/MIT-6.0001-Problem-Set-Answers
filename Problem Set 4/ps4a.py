# Problem Set 4A
# Name: Brandon Davis

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) <= 1:
        return [sequence]
    else:
        permutations = []
        firstChar = sequence[0]
        otherChars = sequence[1:]
        otherCharsPerms = get_permutations(otherChars)
 
        for permutation in otherCharsPerms:
            for index in range(len(permutation) + 1):
                newPermutation = permutation[0:index] + firstChar + permutation[index:]
                permutations.append(newPermutation)
        
        return permutations

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations('xyz'))
    print(get_permutations('bat'))
    print(get_permutations('cow'))